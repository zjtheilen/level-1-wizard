from flask import Flask, redirect, url_for, render_template
from fetch import races, classes
# from pages.homepage import homepage

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", races=races, classes=classes)

if __name__ == "__main__":
    app.run()














# from classes.Character import Character, CharacterClass, CharacterRace
# from fetch import races, classes

# def get_input(category):
#     print(f"Please select one of the following:")
#     for each in category:
#         print(f" -- {each}")
#     x = input("-> ")
#     print(f"You have selected {x}")
#     return x

# user_class_name = get_input(classes)
# user_race_name = get_input(races)

# user_class = CharacterClass(user_class_name)
# user_race = CharacterRace(user_race_name)


# # TESTING 
# zach = Character(player_name="Zach", character_name="Grog")
# zach.race = user_race
# zach.char_class = user_class

# print(zach.player_name)
# print(zach.race)
# print(zach.char_class)
# print(zach)

