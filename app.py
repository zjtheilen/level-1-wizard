from flask import Flask, render_template, request

from utils.fetch import races, classes
from classes.Character import Character, CharacterClass, CharacterRace

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        race_name = request.form.get("race")
        class_name = request.form.get("char_class")
        player_name = request.form.get("player_name")
        character_name = request.form.get("character_name")

        if not race_name or not class_name or not player_name or not character_name:
            error_message = "Must complete all fields before moving on."
            return render_template("index.html",
                                   races=races,
                                   classes=classes,
                                   character=None,
                                   error=error_message)

        race = CharacterRace(race_name)
        char_class = CharacterClass(class_name)

        character = Character(
            player_name=player_name, 
            character_name=character_name,
            race=race,
            char_class=char_class)

        return render_template("index.html",
                               races=races,
                               classes=classes,
                               character=character)

    return render_template("index.html", races=races, classes=classes, character=None)

if __name__ == "__main__":
    app.run()

