from utils import nettoyer_nom_des_colonnes
import pandas as pd
import sys

if len(sys.argv) < 3:
    print('Usage: integrator.py input.csv output.csv')
    exit(0)

input_file = sys.argv[1]
output_file = sys.argv[2]

# lecture du csv
# types
types_a_appliquer = {
    'classe' : 'category',
    'Code.département' : 'category',
    'Code.région' : 'category',
    'unité.de.compte' : 'category'
}
crimes_par_region = pd.read_csv(input_file, sep=';', decimal=',', dtype = types_a_appliquer)

print(crimes_par_region.columns)
# drop la colonne LOG (ie le nombre de logements issu du recensement de la commune (LOG) pour l’année précisée par une variable millésime (millLOG))
crimes_par_region = crimes_par_region.drop('LOG', axis=1)

# nettoyage
# corriger année
crimes_par_region['annee'] = crimes_par_region['annee']+2000
# supprimer les éventuels doubons purs
crimes_par_region = crimes_par_region.drop_duplicates()
# nom des colonnes
nettoyer_nom_des_colonnes(crimes_par_region)

# sauvegarder le DataFrame au format csv
crimes_par_region.to_csv(output_file)

print(crimes_par_region.isna().sum())
print(crimes_par_region.shape)
print(crimes_par_region.head())
print(crimes_par_region.dtypes)
