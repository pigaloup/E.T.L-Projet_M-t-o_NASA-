# Projet ETL - Analyse Météorologique

## Description du projet

Ce projet consiste à collecter, transformer, et analyser des données météorologiques en utilisant un pipeline ETL (Extract, Transform, Load). Les données sont récupérées via l'API de NASA Power, nettoyées et transformées à l'aide de **Apache Spark** pour ensuite être stockées dans une base de données **MySQL workbench**. Le projet comprend également des étapes d'analyse statistique et de visualisation des données dans **Power BI**.

## Technologies utilisées

- **API NASA Power** : Pour la collecte des données météorologiques.
- **Apache Spark** : Pour le traitement et la transformation des données.
- **MySQL workbench** : Pour la gestion de la base de données et le stockage des données..
- **Power BI** : Pour la visualisation des données.
- **Python** : Pour le traitement des données, la gestion du pipeline ETL et la connexion avec PostgreSQL.

## Structure du projet

Le projet est divisé en plusieurs étapes clés :

1. **Collecte des données** :
- Les données météorologiques sont collectées via l'API de **NASA Power** à l'aide de Python, en utilisant des coordonnées géographiques spécifiques à divers pays et villes.
   
2. **Transformation et nettoyage des données** :
- Utilisation de **Apache Spark** pour transformer et nettoyer les données :
- Conversion des dates en colonnes distinctes pour la date et l'heure.
- Suppression des valeurs nulles et des doublons.
- Renommage des colonnes pour plus de clarté.

3. **Création et Chargement de la base de donnée dans MySQL workbench** :
- Insertion des données nettoyées dans **MySQL workbench** via un processus de batch pour accélérer l'insertion.

4. **Visualisation des données** :
Utilisation de **Power BI** pour créer des visualisations interactives les données météorologiques, en analysant les variables telles que :
  
- Température de l'air (`temperature_air`)
- Humidité relative (`humidite_relative`)
- Temps (`date`, `heure`, `mois`, `année`, etc.)
- Température humide (`temperature_humide`)
- Localisation (pays, ville)

## Conclusion

Ce projet met en œuvre un processus ETL complet de collecte, transformation, et stockage des données météorologiques.
Il offre un pipeline efficace et automatisé pour analyser des données complexes et en tirer des insights pertinents.

## Auteurs

- **Nom** : El Hadji Ablaye Galoup DIOP  
- **Email** : elhadjiablayegaloupdiop@gmail.com


