# imports
import requests

# Fetch and prepare races
races_response = requests.get("https://www.dnd5eapi.co/api/2014/races")
races_object = races_response.json()
races = set()
for race in races_object['results']:
    races.add(race['name'])

# Fetch and prepare classes
classes_response = requests.get("https://www.dnd5eapi.co/api/2014/classes")
classes_object = classes_response.json()
classes = set()
for charClass in classes_object['results']:
    classes.add(charClass['name'])