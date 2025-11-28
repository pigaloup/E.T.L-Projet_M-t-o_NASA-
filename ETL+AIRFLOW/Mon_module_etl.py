import logging
import requests
import pandas as pd
from datetime import datetime, timedelta
import concurrent.futures
import mysql.connector
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, substring, to_date, concat_ws, lit

# === CONFIGURATION LOGGING ===
logging.basicConfig(
    filename='etl_execution.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# === COORDONNÉES ===
pays_coordinee = {
    "senegal": {
        "dakar": (14.6928, -17.4467),
        "thies": (14.7894, -16.926),
        "saint-louis": (16.0333, -16.5),
        "kaolack": (14.151, -16.0726),
        "ziguinchor": (12.5833, -16.2667),
        "tambacounda": (13.77, -13.6672),
        "kedougou": (12.5535, -12.1743),
    },
    "mali": {
        "bamako": (12.6392, -8.0029),
        "segou": (13.4317, -6.2157),
        "timbuktu": (16.7666, -3.0026),
        "mopti": (14.4843, -4.1827),
    },
    "cote_d_ivoire": {
        "abidjan": (5.3364, -4.0261),
        "bouake": (7.6833, -5.0333),
        "yamoussoukro": (6.8161, -5.2742),
        "san_pedro": (4.7485, -6.6363),
    },
    "guinee": {
        "conakry": (9.6412, -13.5784),
        "kankan": (10.3842, -9.3057),
        "n_zerekore": (7.7594, -8.8174),
        "labé": (11.3167, -12.2833),
    },
    "nigeria": {
        "lagos": (6.5244, 3.3792),
        "abuja": (9.0579, 7.4951),
        "kano": (12.0022, 8.5919),
    },
    "ghana": {
        "accra": (5.6037, -0.187),
        "kumasi": (6.6666, -1.6163),
        "tamale": (9.4075, -0.8531),
        "takoradi": (4.8975, -1.7603),
    },
    "burkina faso": {
        "ouagadougou": (12.3714, -1.5197),
        "bobo dioulasso": (11.1786, -4.2979),
        "koudougou": (12.2542, -2.3625),
    },
}

# === EXTRACTION ===
def get_data(pays_list, start_date, end_date):
    dfs = []
    def __get_url__(lat, long, start_date, end_date):
        return f"https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=T2M,RH2M,T2MWET,PRECTOTCORR,WS10M,WD10M,T2MDEW,V10M,PS,QV2M,U10M&community=AG&longitude={long}&latitude={lat}&start={start_date}&end={end_date}&format=json"

    def __convert_to_df_optimized__(parameters, city, county):
        dates = list(parameters['T2M'].keys())
        n_dates = len(dates)
        data = {
            'date': dates,
            'ville': [city] * n_dates,
            'pays': [county] * n_dates
        }
        for param in parameters:
            data[param] = [parameters[param].get(date, None) for date in dates]
        return pd.DataFrame(data)

    def fetch_city_data(pays, ville, coordonate):
        lat, long = coordonate
        url = __get_url__(lat, long, start_date, end_date)
        try:
            response = requests.get(url)
            data = response.json()["properties"]["parameter"]
            return __convert_to_df_optimized__(data, ville, pays)
        except Exception as e:
            logging.error(f"Erreur pour {ville}, {pays}: {e}")
            return None

    tasks = []
    for pays_loop in pays_list:
        if pays_loop.lower() not in [p.lower() for p in pays_coordinee.keys()]:
            logging.warning(f"Ce pays n'est pas pris en compte: {pays_loop}")
            continue
        villes = pays_coordinee[pays_loop.lower()]
        for ville, coordonate in villes.items():
            tasks.append((pays_loop, ville, coordonate))

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_city_data, pays, ville, coord) for pays, ville, coord in tasks]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result is not None:
                dfs.append(result)

    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

# === TRANSFORMATION ===
def transformer_header(df):
    df = df.withColumn("date_str", col("date").cast("string"))
    df = df.withColumn("date_formatted", to_date(substring(col("date_str"), 1, 8), "yyyyMMdd")) \
           .withColumn("heure_formatted", concat_ws(":", substring(col("date_str"), 9, 2), lit("00"), lit("00")))

    colonnes_a_exclure = ["date_str", "heure_str", "date", "heure", "date_formatted", "heure_formatted"]
    all_columns = [c for c in df.columns if c not in colonnes_a_exclure]
    df = df.select(*all_columns, col("date_formatted").alias("date"), col("heure_formatted").alias("heure"))

    df = df.dropna().dropDuplicates()
    df = df.filter((col("T2MWET") >= -30) & (col("RH2M") >= -30))

    header_map = {
        'date': 'date',
        'heure': 'heure',
        'ville': 'ville',
        'pays': 'pays',
        'T2M': 'temperature_air',
        'PS': 'pression',
        'WS10M': 'intensite_vent',
        'QV2M': 'humidite_specifique',
        'T2MDEW': 'temperature_point_rosee',
        'U10M': 'composante_est_ouest_vent',
        'V10M': 'vitesse_vent',
        'RH2M': 'humidite_relative',
        'WD10M': 'direction_vent',
        'T2MWET': 'temperature_humide',
        'PRECTOTCORR': 'precipitations_corrigees'
    }

    for old_col, new_col in header_map.items():
        df = df.withColumnRenamed(old_col, new_col)

    return df

# === CHARGEMENT ===
def insert_connector_data(dataframe, batch_size=200):
    DB_NAME = "meteo_db_PAYS_AIRFLOW"
    TABLE_NAME = "meteo_data_PAYS_AIRFLOW"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "MYCCA"
    MYSQL_HOST = "localhost"

    if not isinstance(dataframe, pd.DataFrame):
        dataframe = dataframe.toPandas()

    conn = mysql.connector.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()
    conn.close()

    conn = mysql.connector.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=DB_NAME)
    cursor = conn.cursor()

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            heure VARCHAR(255),
            ville VARCHAR(255),
            pays VARCHAR(255),
            temperature_air FLOAT,
            pression FLOAT,
            intensite_vent FLOAT,
            humidite_specifique FLOAT,
            temperature_point_rosee FLOAT,
            composante_est_ouest_vent FLOAT,
            vitesse_vent FLOAT,
            humidite_relative FLOAT,
            direction_vent FLOAT,
            temperature_humide FLOAT,
            precipitations_corrigees FLOAT
        );
    """)
    conn.commit()

    expected_columns = [
        'date', 'heure', 'ville', 'pays', 'temperature_air', 'pression', 'intensite_vent',
        'humidite_specifique', 'temperature_point_rosee', 'composante_est_ouest_vent',
        'vitesse_vent', 'humidite_relative', 'direction_vent',
        'temperature_humide', 'precipitations_corrigees'
    ]

    missing = [col for col in expected_columns if col not in dataframe.columns]
    if missing:
        logging.warning(f"Colonnes manquantes : {missing}")
        return

    dataframe = dataframe[expected_columns]

    batch = []
    for _, row in dataframe.iterrows():
        row_tuple = tuple(row.values)
        batch.append(row_tuple)

        if len(batch) >= batch_size:
            try:
                cursor.executemany(
                    f"""INSERT INTO {TABLE_NAME} ({', '.join(expected_columns)}) 
                        VALUES ({', '.join(['%s'] * len(expected_columns))})""",
                    batch
                )
                conn.commit()
                logging.info(f"Inserted batch of {len(batch)} rows")
                batch = []
            except Exception as e:
                logging.error(f"Error inserting batch: {e}")
                conn.rollback()

    if batch:
        try:
            cursor.executemany(
                f"""INSERT INTO {TABLE_NAME} ({', '.join(expected_columns)}) 
                    VALUES ({', '.join(['%s'] * len(expected_columns))})""",
                batch
            )
            conn.commit()
            logging.info(f"Inserted final batch of {len(batch)} rows")
        except Exception as e:
            logging.error(f"Error inserting final batch: {e}")
            conn.rollback()

    cursor.close()
    conn.close()
    logging.info("✅ Insertion des données terminée")
