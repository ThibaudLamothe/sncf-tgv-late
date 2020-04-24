
import string as __string
import os as __os
import pickle as __pickle
import numpy as __np
import pandas as __pd
import json as __json
from sklearn.preprocessing import LabelEncoder

from scripts.main_utils import encode_serie


def transform_category_to_color(df, col_name, colors=None):
    if colors == None:
        colors = ['red', 'blue', 'green', 'yellow', 'orange'] * 50
    ser = df[col_name]
    ser, _ = encode_serie(ser)
    ser = __pd.Series(ser).apply(lambda x : colors[int(x)])
    return ser

def get_gare(df, nb=1, print_gare=False):
    gares = df['gare_depart'].unique()
    gares.sort()
    gare = gares[nb]
    if print_gare : print(gare)
    return gare

def get_gares(df):
    return df['gare_depart'].unique()

def get_gare_complement(df, gare):
    tmp = df[['gare_depart', 'gare_arrivee']].drop_duplicates()
    tmp = tmp[tmp['gare_depart']==gare]
    gares_cplmt = tmp['gare_arrivee'].unique()
    return gares_cplmt

# A retravailler par unité (la moyenne n'est pas pondérée dans ce calcul)
def get_root_cause(df):
    extern = __np.round(df['retard_causes_externes'].mean())
    infra = __np.round(df['retard_infrastructure_ferroviaire'].mean())
    trafic = __np.round(df['retard_gestion_trafic'].mean())
    matos = __np.round(df['retard_materiel_roulant'].mean())
    gare = __np.round(df['retard_gestion_en_gare_et_reutilisation_de_materiel'].mean())
    voyageurs = __np.round(df['retard_prise_en_compte_voyageurs'].mean())

    # Tests
    # root_cause = df_liaison.pipe(get_root_cause)
    # np.sum(list(root_cause.values()))
    return {'extern':extern, 'infra':infra, 'trafic':trafic, 'matos':matos, 'gare':gare, 'voyageurs':voyageurs}


# A retravailler par unité (la moyenne n'est pas pondérée dans ce calcul)
def get_quantite_retard(df):
    extern = __np.round(df['retard_causes_externes'].mean())
    infra = __np.round(df['retard_infrastructure_ferroviaire'].mean())
    trafic = __np.round(df['retard_gestion_trafic'].mean())
    matos = __np.round(df['retard_materiel_roulant'].mean())
    gare = __np.round(df['retard_gestion_en_gare_et_reutilisation_de_materiel'].mean())
    voyageurs = __np.round(df['retard_prise_en_compte_voyageurs'].mean())

    # Tests
    # root_cause = df_liaison.pipe(get_root_cause)
    # np.sum(list(root_cause.values()))
    return {'extern': extern, 'infra': infra, 'trafic': trafic, 'matos': matos, 'gare': gare, 'voyageurs': voyageurs}
