from classes.Character import Character, CharacterClass, CharacterRace, CharacterBackground
from utils.fetch import get_data

ALLOWED_RACE_FIELDS = {
    "age", "size", "speed", "traits", "subraces", "alignment", "languages", 
    "language_desc", "ability_bonuses", "size_description", "starting_proficiencies" 
}

ALLOWED_CLASS_FIELDS = {
    "spells", "hit_die", "subclasses", "spellcasting", "proficiencies", "saving_throws",
    "starting_equipment", "proficiency_choices", "starting_equipment_options"
}

ALLOWED_BACKGROUND_FIELDS = {
    'flaws', 'bonds', 'ideals', "feature", 'language_options', 'starting_proficiencies', 
    'starting_equipment', "personality_traits", 'starting_equipment_options'
}

# take all objects from below and create a character object
def build_character(player_name, character_name, race_name, class_name, background_name):

    race_data = get_data("races", race_name)
    class_data = get_data("classes", class_name)
    background_data = get_data("backgrounds", background_name)
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
        for key, value in race_data.items():
            if key in ALLOWED_RACE_FIELDS:
                setattr(race, key, value)
    return race

# establish char_class with char_class object
def build_char_class_object(class_name, class_data):
    char_class = CharacterClass(class_name)
    if class_data:
         for key, value in class_data.items():
            if key in ALLOWED_CLASS_FIELDS:
                setattr(char_class, key, value)
    return char_class

# establish background with background object
def build_background_object(background_name, background_data):
    char_background = CharacterBackground(background_name)
    if background_data:
        for key, value in background_data.items():
            if key in ALLOWED_BACKGROUND_FIELDS:
                setattr(char_background, key, value)
    return char_background        