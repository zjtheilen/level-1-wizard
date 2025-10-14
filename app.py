from classes.Character import Character, Character_Class
from fetch import races, classes

def get_input(category):
    print(f"Please select one of the following:")
    for each in category:
        print(f" -- {each}")
    x = input("-> ")
    print(f"You have selected {x}")
    return x

user_class = get_input(classes)
user_race = get_input(races)


zach = Character(player_name="Zach", character_name="Grog")
zach.race = user_race
zach.char_class = user_class

print(zach.player_name)
print(zach.race)
print(zach.char_class)
print(zach)

