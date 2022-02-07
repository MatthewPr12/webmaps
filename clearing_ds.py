import pandas as pd
import re
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv("locations.list", sep="\"|\t+", error_bad_lines=False, encoding_errors="ignore",
                 skiprows=14, engine='python', names=["shit", "Title", "year", "location"], nrows=500000)
del df["shit"]


def year_format(bad_year):
    year = re.sub('[^0-9]', '', bad_year)
    year = re.sub('{[^>]+}', '', year)
    year = re.sub('[()]', '', year)
    return int(year) if len(year) == 4 else 2004


df['year'] = df['year'].map(lambda x: year_format(x))
new_df = df.head(20000)
geocoder = RateLimiter(Nominatim(user_agent="sth").geocode, min_delay_seconds=1)
new_df['location'] = new_df['location'].apply(geocoder)
new_df['Latitude'] = new_df['location'].apply(lambda x: x.latitude if x else None)
new_df['Longitude'] = new_df['location'].apply(lambda x: x.longitude if x else None)

new_df.to_csv('new_df.csv')  # cleared dataset, although some films do not have location
df_films = pd.read_csv("new_df.csv", delimiter=',')
print(df_films.head())
df_films.dropna(subset=['Latitude'], inplace=True)
print(df_films.head())

del df_films['Unnamed: 0']
df_films.to_csv('cleared_films.csv')  # all-cleared dataset with coordinates
