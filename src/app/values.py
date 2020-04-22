import sncf_utils as f
from logzero import logger
import pandas as pd

# Loading map token
mapbox_access_token = f.get_token('mapbox')

# Loading main data
df = f.load_pickle('dash_first_try.p')

# Loading gare information
gare_position = f.load_pickle('gare_gps.p')
df_gare = pd.DataFrame(
    {
        'gare': [key for key in gare_position.keys()],
        'latitude': [value['latitude'] for value in gare_position.values()],
        'longitude': [value['longitude'] for value in gare_position.values()],
        'adresse': [value['location_adress'] for value in gare_position.values()]
    }
).set_index('gare')

# Computing gare liste
gares = df.pipe(f.get_gares)


# Setting date for application purpose
min_date = 2014  # df['periode'].min()
max_date = 2019  # df['periode'].max()
min_max_date_value = [min_date, max_date]
marks_data = f.slicer(min_date, max_date)