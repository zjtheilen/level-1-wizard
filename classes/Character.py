class Character:
    def __init__(self, player_name, character_name):
        self.player_name = player_name
        self.character_name = character_name
        self.race = ""
        self.char_class = ""
    
    # when logging the object, return a useful name
    def __str__(self):
        return f"{self.character_name}"

    def __repr__(self):
        return f"{self.character_name}"


class Character_Class(Character):
    def __init__(self, player_name, character_name, class_name):
        super().__init__(player_name, character_name)
        self.class_name = class_name

    def __str__(self):
        return f"{self.class_name}"
    
    def __repr__(self):
        return(f"{self.class_name}")