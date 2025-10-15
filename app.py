from flask import Flask, redirect, url_for, render_template, request

from fetch import races, classes
from classes.Character import Character, CharacterClass, CharacterRace

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        race_name = request.form.get("race")
        class_name = request.form.get("class_")
        player_name = request.form.get("player_name")
        character_name = request.form.get("character_name")

        if not race_name or not class_name:
            error_message = "Need both race and class before moving on."
            return render_template("index.html",
                                   races=races,
                                   classes=classes,
                                   character=None,
                                   error=error_message)

        print(f"User selected race={race_name}, class={class_name}")

        race = CharacterRace(race_name)
        char_class = CharacterClass(class_name)
        character = Character(
            player_name=player_name, 
            character_name=character_name,
            race=race,
            char_class=char_class)

        print(f"{character.player_name.capitalize()} is playing a "
              f"{character.race} {character.class_} named {character.character_name.capitalize()}.")

        return render_template("index.html",
                               races=races,
                               classes=classes,
                               character=character)

    return render_template("index.html", races=races, classes=classes, character=None)

if __name__ == "__main__":
    app.run()

