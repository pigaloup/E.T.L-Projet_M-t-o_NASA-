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

A- **Graphique comparatif des températures sur 24 heures. Il illustre clairement les écarts entre la température de l'air, la température humide et la température du point de rosée.**


**Explications :** 

🌡️ 1. Température de l’air (temperature_air)
Définition : C’est la température mesurée à 2 mètres du sol dans des conditions normales, sans influence directe du rayonnement solaire ou du vent.
Utilité : Elle représente la température ambiante ressentie et est utilisée pour les prévisions météo classiques.
Dans les données NASA : C’est le paramètre T2M.

💧 2. Température humide (temperature_humide)
Définition : C’est la température mesurée par un thermomètre dont le bulbe est humidifié et exposé à l’air. Elle tient compte de l’évaporation, donc de l’humidité de l’air.
Utilité :
Elle est toujours inférieure ou égale à la température de l’air.
Elle est utilisée pour calculer l’indice de chaleur et pour évaluer le stress thermique.
Dans les données NASA : C’est le paramètre T2MWET.

🌫️ 3. Température du point de rosée (temperature_point_rosee)
Définition : C’est la température à laquelle l’air doit être refroidi pour que la vapeur d’eau qu’il contient commence à se condenser (formation de rosée ou de buée).
Utilité :
Elle indique le niveau de saturation de l’air en humidité.
Si le point de rosée est proche de la température de l’air, cela signifie que l’humidité relative est élevée.
Dans les données NASA : C’est le paramètre T2MDEW.
  
📈 Interprétation du graphique
- Température de l’air (rouge) : suit une courbe classique, montant en journée et descendant la nuit.

- Température humide (bleu) : toujours inférieure à la température de l’air, elle reflète l’effet de l’humidité sur la sensation thermique.

- Température du point de rosée (vert) : reste la plus basse, indiquant le seuil de condensation de la vapeur d’eau.

👉 Ces trois courbes permettent de visualiser :

- Le niveau de confort thermique (écart entre air et humide)

- Le risque de condensation ou de brouillard (écart entre air et rosée)

- L’influence de l’humidité sur la température ressentie

B- **Graphique comparatif qui illustre clairement la différence entre l’humidité relative et l’humidité spécifique sur 24 heures**

**Explications :** 

📊 Interprétation du graphique

-Humidité relative (courbe bleue) :

Elle est plus élevée la nuit et tôt le matin (jusqu’à 94 %), car l’air est plus froid et donc plus proche de la saturation.

Elle diminue en journée (jusqu’à 53 %) lorsque la température augmente, même si la quantité d’eau reste stable.

-Humidité spécifique (courbe verte) :

Elle varie peu sur la journée, car elle mesure la quantité réelle de vapeur d’eau dans l’air.

Elle augmente légèrement en journée, probablement à cause de l’évaporation.

👉 Conclusion visuelle :

L’humidité relative varie fortement selon l’heure (influencée par la température) tandis que l’humidité spécifique reste plus stable (quantité réelle de vapeur d’eau)

Ce graphique est idéal pour expliquer pourquoi on peut ressentir un air “sec” en journée même s’il contient beaucoup d’humidité.


  


## Conclusion

Ce projet met en œuvre un processus ETL complet de collecte, transformation, et stockage des données météorologiques.
Il offre un pipeline efficace et automatisé pour analyser des données complexes et en tirer des insights pertinents.

## Auteurs

- **Nom** : El Hadji Ablaye Galoup DIOP  
- **Email** : elhadjiablayegaloupdiop@gmail.com


