class CharacterClass:
    def __init__(self, name):
        self.name = name
        # later, you can add spell lists, hit dice, proficiencies, etc.

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"CharacterClass({self.name})"


class CharacterRace:
    def __init__(self, name):
        self.name = name
        # later, you can add resistances, languages, etc.

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"CharacterRace({self.name})"


class Character:
    def __init__(self, player_name: str, character_name: str):
        self.player_name: str = player_name
        self.character_name: str = character_name
        self.race: CharacterRace | None = None
        self.class_: CharacterClass | None = None  

    def __str__(self):
        parts = [self.character_name]
        if self.class_:
            parts.append(f"the {self.class_}")
        if self.race:
            parts.append(f"({self.race})")
        return " ".join(parts)

    def __repr__(self):
        return f"Character({self.character_name}, {self.class_})"
