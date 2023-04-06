# WP1 - Données

Ce Work Package a pour but de récupérer des données musicales qui vont nous aider à faire des liens avec les sentiments, l'état des auditeurs. 
Pour ce faire, nous avons décidé de nous appuyer sur l'API Spotify.
Le fichier _spotify.csv_ regroupe des url de playlist Spotify et le 'mood' attribué à chaque playlist. 

### Prérequis

* Python 3.11
* Les packages suivants : 
    - spotipy
    - pandas
    - requests
    - numpy
que vous pouvez installer à l'aide de la commande `pip install -r requirements.txt`

### Utilisation de l'API Spotify

Pour pouvoir utiliser l'API, il faut tout d'abord créer une application Spotify sur le Dashboard en se connectant avec son compte. Cela va permettre de récupérer un _Client ID_ et un _Client Secret_ qui sont utilisés pour s'authentifier auprès de l'API dans le code python. On peut ainsi utiliser les requêtes de l'API pour récupérer les informations suivantes : 
* song_id
* song_name
* artist_name
* album_name
* release_date
* danceability
* energy
* key
* loudness
* mode
* speechiness
* acousticness
* instrumentalness
* liveness
* valence
* tempo
* duration_ms
* time_signature

### Création du tableau de données

Le tableau de données est créé avec les informations sur les musiques récupérées à l'aide des requêtes de l'API Spotify (vu précédemment). Il contient également une colonne _emotion_ créée à partir du 'mood' attribué à la playlist contenant la musique (dans notre fichier _spotify.csv_). Enfin, nous avons récupéré des genres pour les musiques à l'aide de l'API Last.fm.