from classes.Character import Character, Character_Class
from fetch import races, classes


print("Please select a class:")
class_map = {}
i = 0
for char_class in classes:
    print(f" -- {char_class}")
    i += 1
    class_map[char_class] = i
x = input("-> ")
print(f"You have selected {x}.")
print(class_map[x])
print()

print("Please select a race:")
race_map = {}
i = 0
for race in races:
    print(f" -- {race}")
    i += 1
    race_map[race] = i
y = input("-> ")
print(f"You have selected {y}.")
print(race_map[y])
print()

zach = Character(player_name="Zach", character_name="Bobbly-Ben")
zach = Character_Class(
    player_name=zach.player_name, 
    character_name=zach.character_name,
    class_name=class_map[x]
)

print(f"{zach.player_name} is playing a {y.lower()} {x.lower()}.")
