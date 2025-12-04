# 🌍 Projet E.T.L Météo NASA avec Airflow, Spark, MySQL et Analyse Météorologique

## 📌 Description : 

Ce projet met en place un **pipeline ETL automatisé** pour collecter, transformer et charger des données météorologiques issues de l’API **NASA POWER**.  
L’objectif est de construire une base de données exploitable pour l’analyse climatique de plusieurs pays d’Afrique de l’Ouest (Sénégal, Mali, Côte d’Ivoire, Guinée, Nigeria, Ghana, Burkina Faso).
Le pipeline est orchestré avec **Apache Airflow**, utilise **Apache Spark** pour la transformation des données, et stocke les résultats dans une base **MySQL**.

Le projet comprend également des étapes d'analyse statistique et de visualisation des données dans **Power BI**.

---


## 🛠️ Compétences acquises
En réalisant ce projet, j’ai développé les compétences suivantes :

**Python avancé** :connexion avec la base de donnée Mysql, gestion des exceptions, logging, multithreading.

**API REST** : Pour la collecte des données météorologiques de la NASA POWER.

**Pandas & PySpark** : manipulation et transformation de données massives.

**SQL/MySQL** : création de tables, insertion par batch, gestion des transactions.

**Airflow** : orchestration de pipeline ETL, gestion des dépendances, planification.

**Power BI** : analyse statistique et visualisation interactive des données.

**Bonnes pratiques ETL** : modularité du code, robustesse, logs détaillés.


## ⚙️ Architecture du projet

### Étapes ETL
1. **Extraction**
   - Requête API NASA POWER (paramètres météo : température, humidité, vent, précipitations, etc.).
   - Données collectées pour plusieurs villes par pays.
   - Utilisation de **multithreading** (`concurrent.futures`) pour accélérer les appels API.
   - Sauvegarde initiale en **CSV**.

2. **Transformation et nettoyage des données**
   - Chargement des données brutes dans **PySpark**.
   - Nettoyage : suppression des doublons, gestion des valeurs manquantes, filtrage des anomalies.
   - Conversion des dates en colonnes distinctes pour la date et l'heure.
   - Renommage des colonnes pour plus de lisibilité (`temperature_air`, `pression`, `humidite_relative`, etc.).
   - Export des données nettoyées en **CSV**.

3. **Chargement**
   - Connexion à une base **MySQL**.
   - Création automatique de la base et de la table si elles n’existent pas.
   - Insertion des données par **batchs** pour optimiser les performances.
   - Gestion des erreurs et rollback en cas d’échec.

4. **Visualisation des données** :
Utilisation de **Power BI** pour créer des visualisations interactives les données météorologiques, en analysant les variables telles que :


## 📂 Structure du DAG Airflow

Le DAG `nasa_etl_pipeline` orchestre les 3 étapes :

- **Task 1 : `extract_data`** → Appelle la fonction `get_data` et sauvegarde le CSV brut.  
- **Task 2 : `transform_data`** → Nettoie et transforme les données avec Spark.  
- **Task 3 : `load_data`** → Charge les données dans MySQL.


🖼️ Schéma d’architecture du pipeline ETL

    API[NASA POWER API] --> |Extraction| Airflow[Apache Airflow]
    Airflow --> |Orchestration| Spark[PySpark]
    Spark --> |Transformation| CSV[CSV Nettoyé]
    CSV --> |Chargement| MySQL[(Base MySQL)]
    MySQL --> |Analyse & Visualisation| PowerBI[Power BI]


👉 Conclusion visuelle :

L’humidité relative varie fortement selon l’heure (influencée par la température) tandis que l’humidité spécifique reste plus stable (quantité réelle de vapeur d’eau)

Ce graphique est idéal pour expliquer pourquoi on peut ressentir un air “sec” en journée même s’il contient beaucoup d’humidité.

**C- Graphique en barres groupées pour comparer visuellement l’humidité relative moyenne entre plusieurs villes, tout en distinguant les pays auxquels elles appartiennent.**

🔍 1. Comparaison intra-pays
Vous pouvez observer les différences d’humidité entre les villes d’un même pays.

Exemple : Si Dakar et Saint-Louis (Sénégal) ont des barres très différentes, cela indique une variation climatique régionale.

🌍 2. Comparaison inter-pays
Grâce à la légende par pays, vous pouvez comparer les niveaux d’humidité entre pays.

Exemple : Si les villes de la Guinée ont des barres plus hautes que celles du Sénégal, cela suggère que le climat Guinéen est plus humide.

📈 3. Identification des zones les plus humides ou les plus sèches

-Les barres les plus hautes indiquent les villes avec une humidité relative moyenne élevée (air saturé, climat humide).

-Les barres les plus basses révèlent les villes avec une humidité plus faible (air sec, climat aride).

🧭 4. Analyse géographique et climatique

Ce graphique peut révéler des tendances climatiques régionales :

Les villes côtières ont souvent une humidité plus élevée.

Les villes en altitude ou en zone désertique ont une humidité plus faible.

---

## Conclusion

Ce projet met en œuvre un processus ETL complet de collecte, transformation, et stockage des données météorologiques.
Il offre un pipeline efficace et automatisé pour analyser des données complexes et en tirer des insights pertinents.

## Auteurs

- **Nom** : El Hadji Ablaye Galoup DIOP  
- **Email** : elhadjiablayegaloupdiop@gmail.com


