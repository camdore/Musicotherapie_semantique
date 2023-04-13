# # Peuplement de l'ontologie
#### Objectif : ajouter des individus à l'ontologie de manière automatique à partir d'un csv

### 1- Préparation des données

#### 1-1 Importation des librairies et ontologie

Pour peupler notre ontologie nous allons avoir besoin de plusieurs bibliothèques, notamment :

-   owlready2 : Il s'agit d'une bibliothèque puissante et flexible qui nous fournit une interface simple pour lire, écrire, manipuler et raisonner sur des ontologies OWL
    
-   csv : Cela va nous permettre de manipuler notre csv
    

Ensuite nous récupérons notre ontologie grâce à la bibliotèque owlready2 en utilisant la fonction get_ontology() en lui fournissant le chemin de l'ontologie en argument et nous la chargeons avec la fonction load().

    from owlready2 import *
    import types
	import csv
	import pandas as pd
	onto = get_ontology("musique-emotionsv4.owl").load() #Chargement de l'ontologie
	print(onto)

#### 1-2 Nettoyage des données

Avant de pouvoir commencer à ajouter des instances à notre ontologie, il est important de s'assurer que les données que nous utilisons sont propres et correctement formatées. Si des erreurs de format existent, elles peuvent causer des problèmes dans le processus de peuplement de l'ontologie, comme par exemple l'impossibilité de traiter les caractères avec accent.

Pour cette raison, la première étape consiste souvent à importer les données à partir du fichier CSV source, puis à effectuer une vérification et un nettoyage des données si nécessaire.

    df = pd.read_csv("informations_chansons.csv") #importer le csv
	df = df.dropna() #Enlever les valeurs manquantes
	df = df.replace({"old nostalgic songs":"old_nostalgic_songs"}) #Meme format que l'ontologie
	df = df.replace({"sad nostalgic songs":"sad_nostalgic_songs"}) #Meme format que l'ontologie

On peut maintenant passer à la deuxième étape qui est de peupler l'ontologie. Pour ce faire on utilise la bibliothèque owlready2 pour modifier directement les instances de l'ontologie. On commence par parcourir notre csv ligne par ligne et on associe chaque valeur de ce dernier aux classes de nos ontologies et dataproperties/objectproperties correspondant. Et enfin on sauvegarde notre ontologie dans une nouvelle ontologie pour éviter les erreurs.

    for i in range(0,df.shape[0]):
    emotion,song_id,song_name,artist_name,album_name,genre,release_date,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature = df.iloc[i]
    emotion = onto[emotion]()
    #Genre = onto[genre]() à ajouter lorsque le csv sera fonctionnel
    
    individu = onto.Music(provoque = emotion,
                             song_id = song_id,
                             song_name=song_name,
                             artist_name=artist_name,
                             album_name=album_name,
                             release_date=release_date,
                             danceability=float(danceability),
                             energy=float(energy),
                             key=int(key),
                             loudness=float(loudness),
                             mode=int(mode),
                             speechiness=float(speechiness),
                             acousticness=float(acousticness),
                             instrumentalness=float(instrumentalness),
                             liveness=float(liveness),
                             valence=float(valence),
                             tempo=float(tempo),
                             duration_ms=int(duration_ms),
                             time_signature=int(time_signature),
                             )

	onto.save(file = "musicontopeuple.owl")

On peut grâce à la fonction instance() voir tous nos nouveaux individus rajouter.

    for i in onto.Music.instances(): print(i)

