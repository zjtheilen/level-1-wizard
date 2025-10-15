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
        # later, add resistances, languages, etc.

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"CharacterRace({self.name})"


class Character:
    def __init__(self, player_name: str, character_name: str, 
                 race: CharacterRace, char_class: CharacterClass):
        self.player_name: str = player_name
        self.character_name: str = character_name
        self.race: CharacterRace = race
        self.char_class: CharacterClass = char_class

    def __str__(self):
        parts = [self.character_name]
        if self.char_class:
            parts.append(f"the {self.char_class}")
        if self.race:
            parts.append(f"({self.race})")
        return " ".join(parts)

    def __repr__(self):
        return f"Character({self.character_name}, {self.char_class})"
