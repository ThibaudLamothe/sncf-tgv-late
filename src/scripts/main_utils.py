import string as __string
import os as __os
import pickle as __pickle
import numpy as __np
import pandas as __pd
import json as __json
from sklearn.preprocessing import LabelEncoder



def encode_serie(serie):
    lbl = LabelEncoder()
    lbl.fit(serie.apply(str).values)
    serie =lbl.transform(list(serie.apply(str).values)) # Ajout du str (sinon fonctionne pas sur nombre)
    return serie, lbl


def slicer(min_date, max_date):
    step = 1
    if 5 < max_date - min_date <= 10:
        step = 2
    elif 10 < max_date - min_date <= 50:
        step = 5
    elif max_date - min_date > 50:
        step = 10
    marks_data = {}
    for i in range(int(min_date), int(max_date) + 1, step):
        if i > int(max_date):
            marks_data[i] = str(int(max_date))
        else:
            marks_data[i] = str(i)

    if i < int(max_date):
        marks_data[int(max_date)] = str(max_date)

    return marks_data
    




def transfoCol(ancien, ponctuation=None, accent=None, replacer='_'):
    """Description : simplifie une chaine de caractère en supprimant les majuscules, la ponctuation, les accents et les espaces
    inputs :
        - ancien as string : chaine à modifier
        - ponctuation as list : liste des caractères à retirer
        - accent as dict : dictionnaire des caractères à modifier par un autre
    outputs:
        - string : chaine de caractère modifiée (simplifiée)
    """  
    
    if not ponctuation:
        caracters_to_remove = list(__string.punctuation) + [' ','°']
        ponctuation = {initial:replacer for initial in caracters_to_remove}

    if not accent:
        avec_accent = ['é', 'è', 'ê', 'à', 'ù', 'ç', 'ô', 'î', 'â']
        sans_accent = ['e', 'e', 'e', 'a', 'u', 'c', 'o', 'i', 'a']
        accent = {sans:avec for sans, avec in zip(avec_accent, sans_accent)}
    
    ancien = ancien.lower()
    ancien = ancien.translate(str.maketrans(ponctuation))
    ancien = ancien.translate(str.maketrans(accent))
    double_replacer = replacer + replacer
    while double_replacer in ancien:
        ancien = ancien.replace(double_replacer, replacer)
    
    if ancien[0] ==replacer:
        ancien = ancien[1:]
        
    if ancien[-1] == replacer:
        ancien = ancien[:-1]
    
    return ancien
