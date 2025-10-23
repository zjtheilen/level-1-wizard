from classes.Character import Character, CharacterClass, CharacterRace, CharacterBackground
from utils.fetch import get_class_data, get_race_data, get_background_data

# take all objects from below and create a character object
def build_character(player_name, character_name, race_name, class_name, background_name):
    race_data = get_race_data(race_name)
    class_data = get_class_data(class_name)
    background_data = get_background_data(background_name)

    return Character(
        player_name=player_name,
        character_name=character_name,
        race=build_race_object(race_name, race_data),
        char_class=build_char_class_object(class_name, class_data),
        background=build_background_object(background_name, background_data)
    )    

# establish race with race object
def build_race_object(race_name, race_data):
    race = CharacterRace(race_name)
    if race_data:
        race.age = race_data.get("age")
        race.size = race_data.get("size")
        race.speed  = race_data.get("speed")
        race.traits = race_data.get("traits")
        race.subraces = race_data.get("subraces")
        race.alignment = race_data.get("alignment")
        race.languages  = race_data.get("languages")
        race.language_desc = race_data.get("language_desc")
        race.ability_bonuses  = race_data.get("ability_bonuses")
        race.size_description = race_data.get("size_description")
        race.starting_proficiencies = race_data.get("starting_proficiencies")
    return race

# establish char_class with char_class object
def build_char_class_object(class_name, class_data):
    char_class = CharacterClass(class_name)
    if class_data:
        char_class.spells = class_data.get("spells")
        char_class.hit_die = class_data.get("hit_die")
        char_class.subclasses = class_data.get("subclasses")
        char_class.spellcasting = class_data.get("spellcasting")
        char_class.proficiencies = class_data.get("proficiencies")
        char_class.saving_throws = class_data.get("saving_throws")
        char_class.starting_equipment = class_data.get("starting_equipment")
        char_class.proficiency_choices = class_data.get("proficiency_choices")
        char_class.starting_equipment_options = class_data.get("starting_equipment_options")
    return char_class

# establish background with background object
def build_background_object(background_name, background_data):
    char_background = CharacterBackground(background_name)
    if background_data:
        char_background.flaws = background_data.get('flaws')
        char_background.bonds = background_data.get('bonds')
        char_background.ideals = background_data.get('ideals')
        char_background.feature = background_data.get("feature")
        char_background.language_options = background_data.get('language_options')
        char_background.proficiencies = background_data.get('starting_proficiencies')
        char_background.starting_equipment = background_data.get('starting_equipment')
        char_background.personality_traits = background_data.get("personality_traits")
        char_background.starting_equipment_options = background_data.get('starting_equipment_options')        
    return char_background        