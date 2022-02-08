import argparse
import folium
from folium import plugins
import pandas as pd
import numpy as np
from os import path

parser = argparse.ArgumentParser(description="Find movies that where filmed"
                                             " closest/furthest to your location")
parser.add_argument("year", help="The year when the movies where filmed", type=int)
parser.add_argument("latitude", help="The latitude of the point of your location", type=float)
parser.add_argument("longitude", help="The longitude of the point of your location", type=float)
parser.add_argument("path_to_ds", help="The path to your dataset", type=str)
args = parser.parse_args()


def checking_path(ds_path):
    if not path.isfile(ds_path):
        print('Please, enter valid path to your dataset (cvs file)')
        quit()


def haversine(lon1, lat1, lon2, lat2, year):
    if year == args.year:
        lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        dist = 2 * 6367 * np.arcsin(np.sqrt(np.sin(dlat / 2.0) ** 2 + np.cos(lat1)
                                            * np.cos(lat2) * np.sin(dlon / 2.0) ** 2))
        return dist
    else:
        return float("inf")


# creating datasets
checking_path(args.path_to_ds)
films_df = pd.read_csv(args.path_to_ds)  # using cleared dataset from clearing_ds.py
films_df['Distance'] = films_df.apply(lambda row: haversine(args.longitude,
                                                            args.latitude, row['Longitude'],
                                                            row['Latitude'], row['year']), axis=1)
films_df.sort_values(by=['Distance'], inplace=True)
closest_films = films_df.head(10)
films_df.drop(films_df.index[films_df['Distance'] == float('inf')], inplace=True)
furthest_films = films_df.tail(10)
banned_films = films_df[films_df['location'].str.contains("Россия")]
domestic_films = films_df[films_df['location'].str.contains("Україна")]

# creating map
my_map = folium.Map(location=[args.latitude, args.longitude], zoom_start=10)
mini_map = plugins.MiniMap(toggle_display=True)
my_map.add_child(mini_map)
plugins.ScrollZoomToggler().add_to(my_map)
plugins.Fullscreen(position='topright').add_to(my_map)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(my_map)
fg_closest = folium.FeatureGroup(name='Closest Films')
fg_furthest = folium.FeatureGroup(name='Furthest Films')
fg_ban = folium.FeatureGroup(name="Low-Quality Films")
fg_domestic = folium.FeatureGroup(name="Слава Україні!")
closest_films.apply(lambda row: folium.Marker(
    location=[row['Latitude'], row['Longitude']],
    popup=row['Title'] + " " + str(row['year']),
    icon=folium.Icon(icon='film', prefix='fa')).add_to(fg_closest), axis=1)
furthest_films.apply(lambda row: folium.Marker(
    location=[row['Latitude'], row['Longitude']],
    popup=row['Title'] + " " + str(row['year']),
    icon=folium.Icon(icon='film', prefix='fa',
                     color='purple')).add_to(fg_furthest), axis=1)
banned_films.apply(lambda row: folium.Marker(
    location=[row['Latitude'], row['Longitude']],
    popup=row['Title'] + " " + str(row['year']),
    icon=folium.Icon(icon='fa-trash', prefix='fa',
                     color='red'), tooltip='should not watch it anyway').add_to(fg_ban), axis=1)
domestic_films.apply(lambda row: folium.Marker(
    location=[row['Latitude'], row['Longitude']],
    popup=row['Title'] + " " + str(row['year']),
    icon=folium.Icon(icon='fa-thumbs-up', prefix='fa',
                     color='lightblue')).add_to(fg_domestic), axis=1)
fg_furthest.add_to(my_map)
fg_closest.add_to(my_map)
fg_ban.add_to(my_map)
fg_domestic.add_to(my_map)
folium.LayerControl().add_to(my_map)
my_map.save("maps/my_map1.html")
