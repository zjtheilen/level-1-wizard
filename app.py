from flask import Flask, request, session, redirect, url_for, render_template
from utils.fetch import races, classes, backgrounds
from utils.build_character import build_character
from classes.Character import Character, CharacterClass, CharacterRace, CharacterBackground

app = Flask(__name__)
app.secret_key = 'sk8board1979'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        race_name = request.form.get("race")
        class_name = request.form.get("char_class")
        player_name = request.form.get("player_name")
        character_name = request.form.get("character_name")
        background_name = request.form.get("background_name")

        # get assigned stats
        ability_scores = {
            "str": request.form.get("strength", 0),
            "dex": request.form.get("dexterity", 0),
            "con": request.form.get("constitution", 0),
            "int": request.form.get("intelligence", 0),
            "wis": request.form.get("wisdom", 0),
            "cha": request.form.get("charisma", 0),
        }

        if not all([race_name, class_name, player_name, character_name, background_name]):
            session["error"] = "Must complete all fields before continuing."
            return redirect(url_for("home"))

        character = build_character(player_name, character_name, race_name, class_name, background_name)

        # character.ability_scores.update(ability_scores)
        for stat, value in ability_scores.items():
            if stat in character.ability_scores:
                character.ability_scores[stat] += int(value)
            else:
                character.ability_scores[stat] += int(value)
        
        return render_template("index.html", races=races, classes=classes, backgrounds=backgrounds, character=character)
        
    return render_template("index.html", races=races, classes=classes, backgrounds=backgrounds, character=None)


if __name__ == "__main__":
    app.run()

