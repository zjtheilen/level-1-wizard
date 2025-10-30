from utils.fetch import skills

class CharacterClass:
    def __init__(self, name):
        self.name = name
        # later, add spell lists, hit dice, proficiencies, etc.

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"CharacterClass({self.name})"


class CharacterRace:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"CharacterRace({self.name})"


class CharacterBackground:
    def __init__(self, name):
        self.name = name
        # later, add bonuses, etc.

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"CharacterBackground({self.name})"


class Character:
    def __init__(self, player_name: str, character_name: str, 
                 race: CharacterRace, 
                 char_class: CharacterClass,
                 background: CharacterBackground):
        self.player_name: str = player_name
        self.character_name: str = character_name
        self.race: CharacterRace = race
        self.char_class: CharacterClass = char_class
        self.background: CharacterBackground = background
        self.speed = self.race.speed
        self.size = self.race.size
        self.languages = self.race.languages
        self.ability_scores = {
            'str': 0,
            'dex': 0,
            'con': 0,
            'int': 0,
            'wis': 0,
            'cha': 0
        }

        for each in self.race.ability_bonuses:
            self.ability_scores[each['ability_score']['index']] += each['bonus']

        # Initialize skills dynamically as None (or False)
        for skill in skills:
            # convert spaces / hyphens to underscores
            attr_name = skill.lower().replace(" ", "_").replace("-", "_")
            setattr(self, attr_name, 0)

    def __str__(self):
        parts = [self.character_name]
        if self.char_class:
            parts.append(f"the {self.char_class}")
        if self.race:
            parts.append(f"({self.race})")
        return " ".join(parts)

    def __repr__(self):
        return f"Character({self.character_name}, {self.char_class})"
    
    @property
    def str(self): return self.ability_scores['str']

    @property
    def dex(self): return self.ability_scores['dex']

    @property
    def con(self): return self.ability_scores['con']

    @property
    def int(self): return self.ability_scores['int']

    @property
    def wis(self): return self.ability_scores['wis']

    @property
    def cha(self): return self.ability_scores['cha']

    def apply_base_scores(self, base_scores: dict):
        for stat, val in base_scores.items():
            self.ability_scores[stat] = self.ability_scores.get(stat, 0) + val


    @property
    def str_mod(self): return self.ability_modifiers['str']

    @property
    def dex_mod(self): return self.ability_modifiers['dex']

    @property
    def con_mod(self): return self.ability_modifiers['con']

    @property
    def int_mod(self): return self.ability_modifiers['int']

    @property
    def wis_mod(self): return self.ability_modifiers['wis']

    @property
    def cha_mod(self): return self.ability_modifiers['cha']

    @property
    def ability_modifiers(self):
        return {
            stat: (score - 10) // 2
            for stat, score in self.ability_scores.items()
        }

