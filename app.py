# imports
import requests

from classes.Character import Character, Character_Class


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

zach = Character(player_name="Zach", character_name="Bobbly-Ben")
zach = Character_Class(
    player_name=zach.player_name, 
    character_name=zach.character_name,
    class_name=class_map[x]
)

print(f"{zach.player_name} is playing a {y.lower()} {x.lower()}.")