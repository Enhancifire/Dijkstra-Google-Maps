import requests, json
import googlemaps

with open("data.json", "r") as f:
    data = json.load(f)

    APIKEY = data['apiKey']


gmaps = googlemaps.Client(key=APIKEY)

dist = gmaps.distance_matrix('Delhi', 'Mumbai')

print(dist)
