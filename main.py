import argparse
import folium
import pandas as pd
import re
import numpy as np
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


parser = argparse.ArgumentParser(description="Find ten movies that where filmed closest to your location")
parser.add_argument("year", help="The year when the movies where filmed", type=int)
parser.add_argument("latitude", help="The latitude of the point of your location", type=float)
parser.add_argument("longitude", help="The longitude of the point of your location", type=float)
parser.add_argument("path_to_ds", help="The path to your dataset", type=str)
args = parser.parse_args()

def haversine(lon1, lat1, lon2, lat2, year):
    if year == args.year:
        lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        rad_angle = 2 * np.arcsin(np.sqrt(np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2))
        return 6367 * rad_angle
    else:
        return float("inf")


films_df = pd.read_csv(args.path_to_ds)  # using cleared dataset from clearing_ds.py
films_df['Distance'] = films_df.apply(lambda row: haversine(args.longitude,
                                                            args.latitude, row['Longitude'],
                                                            row['Latitude'], row['year']), axis=1)
print(films_df.head(100))
df_closest = films_df.sort_values(by=['Distance'])
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
print(df_closest.head(10))



# my_map = folium.Map()
# my_map.save("/Users/matthewprytula/pythonProject/term2/lab1/webmaps/my_map.html")
