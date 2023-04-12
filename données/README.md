# WP1 - Données

Ce Work Package a pour but de récupérer des données musicales qui vont nous aider à faire des liens avec les sentiments, l'état des auditeurs. 
Pour ce faire, nous avons décidé de nous appuyer sur l'API Spotify ainsi que l'API Lastfm.
Le fichier _spotify.csv_ regroupe des url de playlist Spotify et le 'mood' attribué à chaque playlist. 

### Prérequis

* Python 3.11
* Les packages suivants : 
    - spotipy
    - pandas
    - requests
    - numpy
    
Vous les retrouverez dans le fichier requirements.txt et vous pouvez les installer à l'aide de la commande `pip install -r requirements.txt`

### Utilisation des l'API
##### API Spotify
Pour pouvoir utiliser l'API, il faut tout d'abord créer une application Spotify sur le Dashboard en se connectant avec son compte. Cela va permettre de récupérer un _Client ID_ et un _Client Secret ID_ qui sont utilisés pour s'authentifier auprès de l'API dans le code python. On peut ainsi utiliser les requêtes faites à l'API pour récupérer les informations suivantes : 
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

##### API LastFm
Nous avons utilisé une seconde API afin de récupérer le genre des musiques, information qui n'était pas disponible via l'API spotify. Pour cela nous avons procédé de la même manière que pour l'API Spotify afin de récupérer un _Client ID_. Nous allons ensuite faire une requête directement sur l'url du site LastFm avec nos identifiants, le nom de la musique et l'artiste/groupe. Une fois récupéré, on compare les genres renvoyés par LastFm et les genres des artistes récupérés via Spotify. Si un genre apparait dans les deux alors on attribut ce genre à la musique.

### Création du tableau de données

Le tableau de données est créé avec les informations sur les musiques récupérées à l'aide des requêtes des API (vu précédemment). Il contient également une colonne _emotion_ créée à partir du 'mood' attribué à la playlist contenant la musique (dans notre fichier _spotify.csv_). Enfin, nous avons récupéré des genres pour les musiques à l'aide de l'API Last.fm.