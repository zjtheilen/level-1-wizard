from classes.Character import Character, CharacterClass, CharacterRace, CharacterBackground
from utils.fetch import get_class_data, get_race_data, get_background_data

def build_character(player_name, character_name, race_name, class_name, background_name):
    race_data = get_race_data(race_name)
    class_data = get_class_data(class_name)
    background_data = get_background_data(background_name)

    race = CharacterRace(race_name)
    if race_data:
        race.size = race_data.get("size", "Unknown")
        race.speed  = race_data.get("speed", "Unknown")
        race.ability_bonuses  = race_data.get("ability_bonuses", [])
        race.languages  = race_data.get("languages", [])
        race.abilities = {
            ab["ability_score"]["name"]: ab["bonus"]
            for ab in race.ability_bonuses
        }
    
    char_class = CharacterClass(class_name)
    if class_data:
        char_class.hit_die = class_data.get("hit_die", "Unknown")
        char_class.proficiencies = class_data.get("proficiencies", [])
        char_class.saving_throws = class_data.get("saving_throws", [])
        char_class.starting_equipment = class_data.get("starting_equipment", [])
    
    char_background = CharacterBackground(background_name)

    return Character(
        player_name=player_name,
        character_name=character_name,
        race=race,
        char_class=char_class,
        background=char_background
    )    