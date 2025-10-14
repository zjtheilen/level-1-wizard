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


# Class for character objects
# initializes with player_name, character_name, and empty fields for race / class
class Character:
    def __init__(self, player_name, character_name):
        self.player_name = player_name
        self.character_name = character_name
        self.race = ""
        self.char_class = ""
    
    # when logging the object, return a useful name
    def __str__(self):
        return f"{self.character_name}"

    def __repr__(self):
        return f"{self.character_name}"


# Test data
ben = Character(player_name="Zach", character_name="Bobbly-Ben")
print(ben)