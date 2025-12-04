**📈 EXPLICATIONS DETAILLEES DES DIFFERNTES VISUELLES DANS POWER BI:**

1- **Graphique comparatif des températures sur 24 heures. Il illustre clairement les écarts entre la température de l'air, la température humide et la température du point de rosée.**

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

**2- Graphique comparatif qui illustre clairement la différence entre l’humidité relative et l’humidité spécifique sur 24 heures**

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

**3- Graphique en barres groupées pour comparer visuellement l’humidité relative moyenne entre plusieurs villes, tout en distinguant les pays auxquels elles appartiennent.**

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
