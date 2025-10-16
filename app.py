from flask import Flask, render_template, request
from utils.fetch import races, classes, backgrounds
from utils.build_character import build_character

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        race_name = request.form.get("race")
        class_name = request.form.get("char_class")
        player_name = request.form.get("player_name")
        character_name = request.form.get("character_name")
        background_name = request.form.get("background_name")

        if not all([race_name, class_name, player_name, character_name, background_name]):
            return render_template("index.html",
                                   races=races,
                                   classes=classes,
                                   backgrounds=backgrounds,
                                   character=None,
                                   error="Must complete all fields before moving on.")

        character = build_character(player_name, character_name, race_name, class_name, background_name)
        return render_template("index.html", races=races, classes=classes, backgrounds=backgrounds, character=character)
        
    return render_template("index.html", races=races, classes=classes, backgrounds=backgrounds, character=None)

if __name__ == "__main__":
    app.run()

