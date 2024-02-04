import pandas as pd
import numpy as np

# création du Dataframe
exam_data = {'nom': ['Anastassia','Omar','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
             'note': [12.5,9,16.5,np.nan,8,19,np.nan,10,15,np.nan],
             'tentatives':[1,3,2,3,2,3,1,1,2,1],
             'qualifié':['oui','non','oui','non','non','oui','oui','non','non','oui']}
etiquettes = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(exam_data, index=etiquettes)

#Affichage des trois premières lignes en utilisant la méthode head()
print("Trois premières lignes:")
print(df.head(3))

#Suppression des lignes contenant des valeurs NaN
df = df.dropna()

#Extraction des colonnes 'nom' et 'note'
nom_note_df = df[['nom','note']]
print("\nColonnes 'nom' et 'note' :")
print(nom_note_df)

#Ajout une nouvelle ligne 'k'
nouvelle_ligne = pd.Series({'nom':'Suresh','note':15.5,'tentatives':1,'qualifié':'oui'}, name='k')
df = df.append(nouvelle_ligne)

#Suppression de la colonne 'tentatives'
df = df.drop('tentatives', axis=1)

#Ajout d'une nouvelle colonne 'succès'
df['succès'] = np.where(df['note'] > 10, 1, 0)

#Afficher le Dataframe final
print("\nDataFrame final :")
print(df)

#Exporter le Dataframe dans un fichier CSV nommé "mes_données"
df.to_csv("mes_données_csv", index_label = 'Etiquettes')