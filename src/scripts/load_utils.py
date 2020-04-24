import string as __string
import os as __os
import pickle as __pickle
import numpy as __np
import pandas as __pd
import json as __json
from sklearn.preprocessing import LabelEncoder


############################################################################################
########################################## PATHS ###########################################
############################################################################################

    
# Create specific path values
DATA_PATH_tla = '/Users/thibaud/Documents/Python_scripts/02_Projects/SNCF/tgv-late/data/'
DATA_PATH_dok = '/data/'

# Local or docker
if 'DEPLOYED' in __os.environ:
    DATA_PATH = DATA_PATH_dok
else:
    DATA_PATH = DATA_PATH_tla

# Similar path
FIG_PATH = DATA_PATH.replace('data', 'fig')
WIKI_PATH =  DATA_PATH.replace('data', 'wiki')

# Sub-data folder
PICKLE_PATH = DATA_PATH + 'pickle/'
JSON_PATH =  DATA_PATH + 'json/'

############################################################################################
######################################### FUNCTIONS ########################################
############################################################################################


def load_pickle(file_name):
    file_path = PICKLE_PATH + file_name
    with open(file_path, 'rb') as pfile:
        my_pickle = __pickle.load(pfile)
    return my_pickle

def save_pickle(object_, file_name):
    file_path = PICKLE_PATH + file_name
    with open(file_path, 'wb') as pfile:
        __pickle.dump(object_, pfile, protocol=__pickle.HIGHEST_PROTOCOL)

def list_pickle():
    file_list = __os.listdir(PICKLE_PATH)
    pickle_list = [i for i in file_list if '.p' in i]
    print(pickle_list)


def parse_json(file_name):
    """Given a json_file =path loading it and sending a dictionary back"""
    file_path = JSON_PATH + file_name
    with open(file_path) as f:
        data = __json.load(f)
    return data


def save_json(data, file_name):
    """Saving as a json file in one line"""
    file_path = JSON_PATH + file_name
    with open(file_path, 'w') as fp:
        __json.dump(data, fp, indent=4, separators=(',', ': '), sort_keys=True)


# def get_token(path):
#     with open(path, 'r') as file:
#         api_key= file.read()
#     return api_key

def get_token(token):
    CONFIG = parse_json('config.json')
    return CONFIG['tokens'][token]