#Webmaps
##### using python package **folium**
## Clearing Data
Given the *.list* file(imdb dataset) which consists of more than **1 million** lines with film names, the year that they were relesed and the set location(sometimes with some additional info), I neaded to get the clear data out of it, so that it would be easier to work with it. Obviously, the file was messy, but I did not need all the films(and there's the reson for that which will be depicted later). Therefore, I used **pandas** package in order to get the needed info and turn it into clear csv-file [cleared_films.csv](https://github.com/MatthewPr12/webmaps/blob/main/datasets/cleared_films.csv).
All in all, I got clear DataFrame of more than 10000 films and info about them.

</ br>

## Coordinates
Having the places(countries, cities, streets etc.) where all the films were shot, I needed to get their accurate geographical coordinates location(to be able to set some Markers later). In order to do so, I used **geopy** python package. The thing is that with only one request per second is allowed there. So I launched [geocoder.py](https://github.com/MatthewPr12/webmaps/blob/main/geocoder.py) overnight and managed to get coordinates for all the locations.
 </ br>

 ## Creating Maps
The task itself(create the map and mark different types of film on it) is implemented using **folium** python package. [main.py](https://github.com/MatthewPr12/webmaps/blob/main/main.py) can be launched using comand line.

'''python3 main.py 1993 49.7714509 23.6730132 /Users/< user >/path_to_dataset/cleared_films.csv'''
<pre><code>python3 main.py 1993 49.7714509 23.6730132 /Users/< user >/path_to_dataset/cleared_films.csv</code></pre>

It takes three arguments:
1. year (integer)
2. latitude (float)
3. longitude (float)
4. path to the dataset (csv-file)

The program will find up to ten films that were shot closest to the given *location(latitude, longitude)* in the given *year*.
It will create an *.html* file named [my_map1.html](https://github.com/MatthewPr12/webmaps/tree/main/maps) that you can open using your favorite browser
[![safari-icon](https://user-images.githubusercontent.com/91616807/153007732-88700934-3954-4767-8acd-8cba5f97ca93.png)]
[![google-chrome-icon-blue-black-33](https://user-images.githubusercontent.com/91616807/153007781-37bc553c-8826-45f7-aa10-366884e7f6ca.png)]
[![Firefox-icon](https://user-images.githubusercontent.com/91616807/153007799-90cf659c-2eaa-472d-b1ba-5f4315f9700e.png)]
[![Internet-Explorer-icon](https://user-images.githubusercontent.com/91616807/153007817-2301fa80-bc5f-4a8b-9d98-08052369da9c.png]

After you opened the page you can do next things:
* zoom in or out + enter or exit full-screen mode (topright) [<img width="26" alt="Screenshot 2022-02-08 at 16 39 12" src="https://user-images.githubusercontent.com/91616807/153009786-d726f812-0791-42e8-a265-fd70b9353713.png">]
* display or remove layers of Markers + change dark and light modes of the map (topright) [<img width="35" alt="Screenshot 2022-02-08 at 16 38 07" src="https://user-images.githubusercontent.com/91616807/153010227-f38c1ca4-3ef0-4b84-9483-49114ad9135f.png">]
* change scrolling method (bottomleft) [<img width="31" alt="Screenshot 2022-02-08 at 16 39 31" src="https://user-images.githubusercontent.com/91616807/153010508-6553158b-24e5-4754-adce-3cb051b61338.png">]