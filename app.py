from flask import Flask, request, session, redirect, url_for, render_template
from utils.fetch import races, classes, backgrounds, skills
from utils.build_character import build_character
from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)

# Initialize Flask-Assets
assets = Environment(app)

# Define SCSS bundle
scss = Bundle(
    'scss/styles.scss',           # input
    filters='libsass',            # compile SCSS -> CSS
    output='css/styles.css',      # output
    depends='scss/**/*.scss'      # optional: watch all SCSS files
)

assets.register('scss_all', scss)
scss.build()  # build on startup (optional)

@app.route("/reset", methods=["POST"])
def reset_character():
    return redirect(url_for("home"))

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
        character.apply_base_scores(ability_scores)
        character.apply_base_skill_modifiers()

        # character.ability_scores.update(ability_scores)
        for stat, value in ability_scores.items():
            if value:
                character.ability_scores[stat] += int(value)
        
        return render_template("index.html", races=races, classes=classes, backgrounds=backgrounds, character=character, skills=sorted(skills))
        
    return render_template("index.html", races=races, classes=classes, backgrounds=backgrounds, character=None, skills=sorted(skills))


if __name__ == "__main__":
    app.run()

