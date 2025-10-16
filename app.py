from flask import Flask, render_template, request
import requests

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

        race_url = f"https://www.dnd5eapi.co/api/2014/races/{race_name.lower()}"
        race_response = requests.get(race_url)        
        if race_response.ok:
            race_data = race_response.json()
            size = race_data.get("size")
            speed = race_data.get("speed")
            ability_bonuses = race_data.get("ability_bonuses")
            languages = race_data.get("languages")
        else:
            size = "Unknown"
            speed = "Unknown"
            ability_bonuses = "Unknown"
            languages = "Unknown"
        race = CharacterRace(race_name)
        race.size = size
        race.speed = speed
        race.abilities = {}
        race.ability_bonuses = ability_bonuses
        for ability in race.ability_bonuses:
            name = ability['ability_score']['name']
            value = ability['bonus']
            race.abilities[name] = value
        race.languages = languages
        
        class_url = f"https://www.dnd5eapi.co/api/2014/classes/{class_name.lower()}"
        class_response = requests.get(class_url)
        if class_response.ok:
            class_data = class_response.json()
            hit_die = class_data.get("hit_die")
            proficiencies = class_data.get("proficiencies")
            saving_throws = class_data.get("saving_throws")
            starting_equipment = class_data.get("starting_equipment")
        else:
            hit_die = "Unknown"
            proficiencies = "Unknown"
            saving_throws = "Unknown"
            starting_equipment = "Unknown"
        char_class = CharacterClass(class_name)
        char_class.hit_die = hit_die
        char_class.proficiencies = proficiencies
        char_class.saving_throws = saving_throws
        char_class.starting_equipment = starting_equipment

        character = Character(
            player_name=player_name, 
            character_name=character_name,
            race=race,
            char_class=char_class)
        
        print(
            f"Character race/class: {character.race}/{character.char_class}.\n"
            f"{character.player_name} named his character {character.character_name}.\n"
            f"speed: {character.race.speed}, size: {character.race.size}\n"
            f"ability scores before rolling: {character.ability_scores}\n"
            f"proficiencies: {character.char_class.proficiencies}\n"
            f"saving throws: {character.char_class.saving_throws}\n"
        )

        return render_template("index.html", races=races, classes=classes, character=character)

    return render_template("index.html", races=races, classes=classes, character=None)

if __name__ == "__main__":
    app.run()

