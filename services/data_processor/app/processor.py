import pandas as pd
import json
import sys

if len(sys.argv) < 3:
    print('Usage: processor.py input.csv output.json')
    exit(0)

input_file = sys.argv[1]
output_file = sys.argv[2]

types_a_appliquer = {
    'classe' : 'category',
    'code_departement' : 'category',
    'code_region' : 'category',
    'unite_de_compte' : 'category'
}
crimes_par_region = pd.read_csv(input_file, dtype = types_a_appliquer)

# créer json à destination du dash
faits_par_annee_par_departement = crimes_par_region[['annee', 'code_departement', 'faits']].groupby(['annee', 'code_departement']).agg('sum')
pop_par_annee_par_departement = crimes_par_region[['annee', 'code_departement', 'pop']].groupby(['annee', 'code_departement']).agg('first')

statistiques = {}
for année in crimes_par_region['annee'].unique():
    statistiques[str(année)] = {}
    filter = crimes_par_region['annee'] == année
    for dep in crimes_par_region['code_departement'].unique():
        statistiques[str(année)][str(dep)] = {
            'crimes': {},
            'taux_par_pop': faits_par_annee_par_departement.loc[année, dep].iloc[0] / pop_par_annee_par_departement.loc[année, dep].iloc[0]
        }
        filter_par_dep = filter & (crimes_par_region['code_departement'] == dep)
        for crime in crimes_par_region['classe'].unique():
            filter_par_crime = filter_par_dep & (crimes_par_region['classe'] == crime)
            statistiques[str(année)][str(dep)]['crimes'][str(crime)] = int(crimes_par_region[filter_par_crime]['faits'].iloc[0])

with open(output_file, 'w') as file:
    file.write(json.dumps(statistiques))
    file.close()
