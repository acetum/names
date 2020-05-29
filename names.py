from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

#import files from csv
#Data recovered from :
#https://www.donneesquebec.ca/recherche/fr/dataset/banque-de-prenoms-filles
#https://www.donneesquebec.ca/recherche/fr/dataset/banque-de-prenoms-garcons
GARS = pd.read_csv('gars1980-2018.csv', encoding='utf-8')
FILLES = pd.read_csv('filles1980-2018.csv', encoding='utf-8')


#Add a total column for each name
GARS['total'] = GARS.sum(axis=1)
FILLES['total'] = FILLES.sum(axis=1)

#Get Dataframe row by name
def get_row_by_name(df, name):
    return df[df.prenom == name.upper()]

#Plot graph of evolution of number of people with name by year
def plot_name_by_year(df, *names):
    
    columns = df.columns[1:-1]

    for name in names:
        name_series = get_row_by_name(df, name)
        label_name = '{} Total: {}'.format(name.upper(), name_series['total'].values)
        plt.plot(columns, name_series.iloc[0][1:-1], label=label_name)

    plt.title('Évolution chronologique des prénoms (1980-2018)')
    plt.xticks(rotation=45)
    plt.xlabel('Année')
    plt.legend()
    plt.show()


#plot_name_by_year(GARS, '')

populaire_garcon = GARS[GARS.total == GARS.total.max()]
populaire_fille = FILLES[FILLES.total == FILLES.total.max()]
print(populaire_garcon)
print(populaire_fille)
