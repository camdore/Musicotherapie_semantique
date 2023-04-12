# Musicotherapie_semantique
OUAP-4329

## Contexte du projet  

Avec notre équipe de sémantique, nous avons décidé de travailler sur le bien-être des individus à travers la musique.  
Notre projet répond à un enjeu important puisque cela concerne le bien-être. Pour cela, nous avons travaillé sur la mise en place d’une application permettant aux utilisateurs d’obtenir une playlist de musique qui permettra d’atteindre un état émotionnel souhaité. Nous utilisons donc la musique comme un outil thérapeutique accessible et pratique pour améliorer la qualité de vie émotionnelle des utilisateurs.

## Etapes clés :
Pour mettre en place notre application, plusieurs étapes ont été nécessaires. 
- Une base de données de 3061 chansons qui ont chacune 14 paramètres à été créée. 
- Une ontologie à été mise en place pour modéliser les différentes relations qui lient la chanson à ces paramètres ainsi que les émotions. 
- Les graphes permettent d’identifier les motifs dans la base de données entre les chansons associées à chaque émotion. Ils s’appuient sur la modélisation avec l’ontologie et les données d’ou l'importance de la qualité de celles-ci. C’est donc les algorithmes qui permettent concrètement de créer les recommandations pour l’utilisateur. 

## Structure du projet 

Musicotherapie_semantique/ 

    |-- données
        |--informations_chansons.csv
        |--requirements.txt
        |--spotify.csv
        |--spotify.ipynb
        |-- README.md

    |-- ontologies
        |-- informations_chansons(1).csv
        |-- infoschansons.csv
        |-- music-ontology.owl
        |-- musique-emotionsv4.owl     
        |-- musicontopeuple.owl
        |-- README.md
        |-- peuplementmusic.py
        |-- PeupOnto.ipynb
        |-- test_ontologie.owl
    |-- README.md

- Le sous dossier "données" contient tous le notebook "spotify.ipynb" utilisé pour extraire des api les informations nécessaire dans le csv "informations_chansons.csv". Le fichier requirement.txt permet quand à d'avoir les librairies nécessaires.  

- Le sous dossier "ontologies" contient le fichier "peuplementmusic.py" qui permet de ajouter des individus de manière automatique à des ontologies. On retrouve ensuite toutes les versions des ontologies avec les fichiers .owl