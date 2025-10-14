# imports
import requests

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


class Character_Class(Character):
    def __init__(self, player_name, character_name, class_name):
        super().init(player_name, character_name)
        self.class_name = class_name

    def __str__(self):
        return f"{self.class_name}"
    
    def __repr__(self):
        return(f"{self.class_name}")


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


# Test data

print("Please select a class:")
class_map = {}
i = 0
for char_class in classes:
    print(f"    {char_class}")
    i += 1
    class_map[char_class] = i
x = input()
print(f"You have selected {x}.")
print(class_map[x])
print()

print("Please select a race:")
race_map = {}
i = 0
for race in races:
    print(f"    {race}")
    i += 1
    race_map[race] = i
y = input()
print(f"You have selected {y}.")
print(race_map[y])
print()

# ben = Character(player_name="Zach", character_name="Bobbly-Ben")
# print(ben)