from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
from clearing_ds import df


df = df.head(20000)
print(df)
geocoder = RateLimiter(Nominatim(user_agent="sth").geocode, min_delay_seconds=1)
df['location'] = df['location'].apply(geocoder)
df['Latitude'] = df['location'].apply(lambda x: x.latitude if x else None)
df['Longitude'] = df['location'].apply(lambda x: x.longitude if x else None)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
print(df)
