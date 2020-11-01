# Dashboard_Python_V2
Lien entre accidents de voiture chez les jeunes et consommation d'alcool chez les jeunes dans le monde

User's Guide :

Liste des librairies/packages utilisés :
- dash
- dash_bootstrap_components
- pandas
- dash_html_components
- dash_core_components
- dash.dependencies
- plotly.express
- base64
- datetime
- io
- dash_table

Afin d'exécuter sans erreur ce code, il faudra installer tous ces packages dans votre invité de commande en tapant ceci : pip install le_nom_du_package.

URL du dashboard : http://127.0.0.1:5000



Developer's Guide :

Rapport d'analyse :

Les résultats obtenus montrent une nette diminution du nombre d'accidents de la route de la route chez les jeunes.
C'est en Europe et en Amérique du Sud que les jeunes consomment le plus d'alcool (53% des jeunes en consomment en Europe, et 36% en Amérique du Sud).

En Europe, la limité légale de concentration d'alcool dans le sang pour les jeunes conducteurs est d'environ 0.03g (en moyenne). 
Or, on voit qu'au fil du temps, le nombre d'accidents de la route baisse beaucoup dans tous les pays. 
Le nombre maximal d'accidents par pays passe de plus de 8000 à moins de 3500.

Cette tendance peut se constater en Europe, mais aussi dans la quasi totalité des pays du monde que nous avons pu étudier.

Aux Etats-Unis cependant, nous observons que le nombre d'accidents reste stable chez les jeunes. En effet, les jeunes américains peuvent conduire en moyenne dès l'âge de 16 ans.
Ne pouvant consommer légalement de l'alcool avant l'age de 21 ans, ce n'est pas un facteur qui impacte significativement le nombre d'accidents de la route.


Lien vers les datasets :

Base de données "youth" : https://apps.who.int/gho/data/node.main.A1206?lang=en

Le préprocessing des bases de données est dans le dossier nettoyage_bdd.



Instructions d'exécution :

- Télécharger le dossier "ProjetV1-master"
- Le dézipper
- Ouvrir l'invité de commande
- Se déplacer dans les répertoires afin que le répertoire courant soit ProjetV1-master
- Rentrer cette ligne de commande dans l'invité : python main.py

