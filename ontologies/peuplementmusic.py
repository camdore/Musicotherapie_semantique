from owlready2 import *
import types
onto = get_ontology("file://C:/Users/alice/Downloads/musique-emotions.owl").load()

onto_individus = get_ontology("http://www.semanticweb.org/alice/ontologies/2023/3/untitled-ontology-24")
onto_individus.imported_ontologies.append(onto)
import csv
f = open("C:/Users/alice/Downloads/infoschansons.csv")
identifiant=0
reader = csv.reader(f)
next(reader)
with onto_individus:
  for ligne in reader:
    emotion,song_id,song_name,artist_name,album_name,release_date,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature = ligne
    
    emotion = onto[emotion]()
      
    
    individu = onto.Music(identifiant,
                             provoque = emotion,
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
                             instrumentalness=instrumentalness,# string pour l'instant car ça n'arrive pas à convertir les puissances écrites avec "e"
                             liveness=float(liveness),
                             valence=float(valence),
                             tempo=float(tempo),
                             duration_ms=int(duration_ms),
                             time_signature=int(time_signature),
                             )
    identifiant+=1
      
onto_individus.save("music_individus.owl")