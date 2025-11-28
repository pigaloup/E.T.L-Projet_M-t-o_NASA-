from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from pyspark.sql import SparkSession

# === Importer tes fonctions depuis ton module ===
from ETL_METEO.Mon_module_etl import get_data, transformer_header, insert_connector_data

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='nasa_etl_pipeline',
    default_args=default_args,
    description='Pipeline ETL NASA automatisé avec Airflow',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@weekly',  # Exécution chaque semaine
    catchup=False,
    tags=['ETL', 'NASA', 'Spark', 'MySQL']
) as dag:

    # === Étape 1 : Extraction ===
    def extract_data():
        date_actuelle = datetime.today()
        date_delay = date_actuelle - timedelta(days=8)
        end_date = date_delay.strftime("%Y%m%d")
        start_date = (date_delay - timedelta(days=75)).strftime("%Y%m%d")
        pays_list = ["Senegal", "mali", "cote_d_ivoire", "guinee", "nigeria", "ghana", "burkina faso"]

        df = get_data(pays_list, start_date, end_date)  # retourne un DataFrame Pandas
        df.to_csv("/home/papidiop7/airflow/dags/ETL_METEO/Nasa_Power_data_PAYS.csv", index=False)

    # === Étape 2 : Transformation ===
    def transform_data():
        spark = SparkSession.builder.appName("Météo").getOrCreate()
        # Charger le CSV en Spark DataFrame
        df_spark = spark.read.csv("/home/papidiop7/airflow/dags/ETL_METEO/Nasa_Power_data_PAYS.csv", header=True, inferSchema=True)
        df_cleaned = transformer_header(df_spark)  # applique la transformation
        # Sauvegarder en CSV via Pandas
        df_cleaned.toPandas().to_csv("/home/papidiop7/airflow/dags/ETL_METEO/Nasa_Power_data_cleaned_PAYS.csv", index=False)
        spark.stop()

    # === Étape 3 : Chargement ===
    def load_data():
        df = pd.read_csv("/home/papidiop7/airflow/dags/ETL_METEO/Nasa_Power_data_cleaned_PAYS.csv")  # DataFrame Pandas
        insert_connector_data(df, batch_size=200)

    # === Définition des tâches Airflow ===
    t1 = PythonOperator(task_id='extract_data', python_callable=extract_data)
    t2 = PythonOperator(task_id='transform_data', python_callable=transform_data)
    t3 = PythonOperator(task_id='load_data', python_callable=load_data)

    # Dépendances
    t1 >> t2 >> t3
