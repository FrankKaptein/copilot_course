
import random

clues = [
    "There is a faint smell of smoke lingering in the air, as if a fire once raged here.",
    "There is a broken mirror on the wall, its shards scattered across the floor.",
    "There is a dusty old book on the table, its pages filled with cryptic symbols.",
    "There is a bloodstain on the carpet, partially hidden under a piece of furniture.",
    "There is a portrait hanging crookedly on the wall, the eyes seeming to follow you.",
    "There is a cold draft coming from a hidden passage behind the bookshelf.",
    "There is a set of footprints leading to a locked door, then disappearing.",
    "There is a whispering sound that seems to come from the shadows.",
    "There is a rusted key lying on the floor, its purpose long forgotten.",
    "There is a sense of unease in the room, as if someone or something is watching."
]

sense_exp = [
    "You see flickering shadows dancing on the walls, cast by an unseen light source.",
    "You hear the distant echo of footsteps, growing louder with each passing moment.",
    "You smell the faint aroma of lavender, mixed with the musty scent of old stone.",
    "You feel a chill run down your spine as a cold breeze brushes past you.",
    "You sense an overwhelming presence, as if the very walls are watching you.",
    "You see cobwebs glistening in the corners, untouched for years.",
    "You hear the soft rustling of fabric, as if someone is moving just out of sight.",
    "You smell the acrid scent of burning candles, mingling with the damp air.",
    "You feel the rough texture of the stone walls, worn smooth in places by countless hands.",
    "You sense a hidden passage nearby, its entrance concealed by clever craftsmanship.",
    "You see a faint glow emanating from beneath a heavy wooden door.",
    "You hear the faint whisper of voices, their words just beyond comprehension."
]

inventory = {
    "Shield Spell": False,
    "Invisibility Scroll": False
}

class RandomItemSelector:
    def __init__(self, items):
        self.items = items
        self.used_items = []

    def add_item(self, item):
        self.items.append(item)

    def pull_random_item(self):
        if len(self.used_items) == len(self.items):
            self.reset()
        available_items = [item for item in self.items if item not in self.used_items]
        if not available_items:
            return None
        selected_item = random.choice(available_items)
        self.used_items.append(selected_item)
        return selected_item

    def reset(self):
        self.used_items = []

class SenseClueGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SenseClueGenerator, cls).__new__(cls)
            cls._instance.clue_selector = RandomItemSelector(clues)
            cls._instance.sense_selector = RandomItemSelector(sense_exp)
        return cls._instance

    def get_senseclue(self):
        clue = self.clue_selector.pull_random_item()
        sense = self.sense_selector.pull_random_item()
        return f"{clue} {sense}"

from enum import Enum

class EncounterOutcome(Enum):
    CONTINUE = 1
    END = 2

from abc import ABC, abstractmethod

class Encounter(ABC):
    @abstractmethod
    def run_encounter(self) -> EncounterOutcome:
        pass


class DefaultEncounter(Encounter):
    def __init__(self):
        self.sense_clue_generator = SenseClueGenerator()

    def run_encounter(self) -> EncounterOutcome:
        sense_clue = self.sense_clue_generator.get_senseclue()
        print(sense_clue)
        return EncounterOutcome.CONTINUE


class TreasureEncounter(Encounter):
    def run_encounter(self) -> EncounterOutcome:
        print("You have found the treasure! Congratulations!")
        return EncounterOutcome.END


red_wizard_game_rules = {
    "Fireball": ["Ice Shard", "Lightning Bolt"],
    "Ice Shard": ["Wind Gust", "Earthquake"],
    "Wind Gust": ["Lightning Bolt", "Fireball"],
    "Lightning Bolt": ["Earthquake", "Ice Shard"],
    "Earthquake": ["Fireball", "Wind Gust"]
}


class RedWizardEncounter(Encounter):
    def __init__(self):
        self.wizard_vanquished = False

    def run_encounter(self) -> EncounterOutcome:
        if self.wizard_vanquished:
            print("You have entered the Wizard's Tower, but the Red Wizard has already been vanquished. You may proceed without a battle.")
            return EncounterOutcome.CONTINUE

        if inventory["Invisibility Scroll"]:
            use_scroll = input("You have an Invisibility Scroll. Would you like to use it to skip the battle? (Y/n): ").strip().lower()
            if use_scroll == '' or use_scroll == 'y':
                print("You use the Invisibility Scroll and sneak past the Red Wizard undetected.")
                inventory["Invisibility Scroll"] = False
                return EncounterOutcome.CONTINUE

        print("You have encountered the Red Wizard! To proceed, you must defeat him in a spell battle.")
        
        choices = list(red_wizard_game_rules.keys())
        
        while True:
            user_choice = input("Choose your spell (Fireball, Ice Shard, Wind Gust, Lightning Bolt, Earthquake): ").strip().title()
            if user_choice not in choices:
                print("Invalid choice. Please choose again.")
                continue
            
            wizard_choice = random.choice(choices)
            print(f"The Red Wizard casts: {wizard_choice}")
            
            if user_choice == wizard_choice:
                print("The spells clash in mid-air, creating a dazzling explosion of light and sound! It's a draw! Cast again.")
                continue
            elif wizard_choice in red_wizard_game_rules[user_choice]:
                print("With a surge of power, your spell overwhelms the Red Wizard's defenses!")
                print("The air crackles with energy as the Red Wizard is engulfed in a blinding light.")
                print("When the light fades, the Red Wizard is no more. You have vanquished him from this castle!")
                self.wizard_vanquished = True
                return EncounterOutcome.CONTINUE
            else:
                if inventory["Shield Spell"]:
                    print("The Red Wizard's spell strikes you with devastating force, but your shield spell activates just in time!")
                    print("A shimmering barrier of light surrounds you, absorbing the impact of the spell.")
                    print("The shield spell dissipates, leaving you unharmed. You get another chance to defeat the Red Wizard.")
                    inventory["Shield Spell"] = False
                    continue
                else:
                    print("The Red Wizard's spell strikes you with devastating force.")
                    print("You feel your strength ebbing away as darkness closes in.")
                    print("You have been vanquished by the Red Wizard. Game Over.")
                    return EncounterOutcome.END


# Define the new game rules for the spell battle
blue_wizard_game_rules = {
    "Magic Wand": ["Magic Scroll"],
    "Magic Scroll": ["Magic Stone"],
    "Magic Stone": ["Magic Wand"]
}


class BlueWizardEncounter(Encounter):
    def __init__(self):
        self.wizard_vanquished = False

    def run_encounter(self) -> EncounterOutcome:
        if self.wizard_vanquished:
            print("You have entered the Blue Wizard's Lair, but the Blue Wizard has already been vanquished. You may proceed without a battle.")
            return EncounterOutcome.CONTINUE

        if inventory["Invisibility Scroll"]:
            use_scroll = input("You have an Invisibility Scroll. Would you like to use it to skip the battle? (Y/n): ").strip().lower()
            if use_scroll == '' or use_scroll == 'y':
                print("You use the Invisibility Scroll and sneak past the Blue Wizard undetected.")
                inventory["Invisibility Scroll"] = False
                return EncounterOutcome.CONTINUE

        print("You have encountered the Blue Wizard! To proceed, you must defeat him in a spell battle.")
        
        choices = list(blue_wizard_game_rules.keys())
        
        while True:
            user_choice = input("Choose your spell (Magic Wand, Magic Scroll, Magic Stone): ").strip().title()
            if user_choice not in choices:
                print("Invalid choice. Please choose again.")
                continue
            
            wizard_choice = random.choice(choices)
            print(f"The Blue Wizard casts: {wizard_choice}")
            
            if user_choice == wizard_choice:
                print("It's a draw! Cast your spell again.")
                continue
            elif wizard_choice in blue_wizard_game_rules[user_choice]:
                print("Congratulations! You have vanquished the Blue Wizard from this castle!")
                self.wizard_vanquished = True
                return EncounterOutcome.CONTINUE
            else:
                if inventory["Shield Spell"]:
                    print("The Blue Wizard's spell strikes you with devastating force, but your shield spell activates just in time!")
                    print("A shimmering barrier of light surrounds you, absorbing the impact of the spell.")
                    print("The shield spell dissipates, leaving you unharmed. You get another chance to defeat the Blue Wizard.")
                    inventory["Shield Spell"] = False
                    continue
                else:
                    print("You have been vanquished by the Blue Wizard. Game Over.")
                    return EncounterOutcome.END


class ShieldSpellEncounter(Encounter):
    def __init__(self):
        self.spell_obtained = False

    def run_encounter(self) -> EncounterOutcome:
        if self.spell_obtained:
            print("You have entered the Enchanted Chamber, but the Shield Spell has already been taken. You find nothing of interest.")
            return EncounterOutcome.CONTINUE

        print("You have entered the Enchanted Chamber. The air is thick with magic, and a glowing scroll lies on a pedestal in the center of the room.")
        print("As you approach, the scroll unfurls, revealing the incantation for a powerful Shield Spell.")
        print("You have obtained the Shield Spell! This spell can protect you from one fatal attack.")
        inventory["Shield Spell"] = True
        self.spell_obtained = True
        return EncounterOutcome.CONTINUE


class InvisibilityScrollEncounter(Encounter):
    def __init__(self):
        self.scroll_obtained = False

    def run_encounter(self) -> EncounterOutcome:
        if self.scroll_obtained:
            print("You have entered the Hidden Alcove, but the Invisibility Scroll has already been taken. You find nothing of interest.")
            return EncounterOutcome.CONTINUE

        print("You have entered the Hidden Alcove. The air shimmers with a strange energy, and a translucent scroll floats in mid-air.")
        print("As you reach out, the scroll solidifies, revealing the incantation for an Invisibility Scroll.")
        print("You have obtained the Invisibility Scroll! This spell can make you invisible and allow you to skip one wizard battle.")
        inventory["Invisibility Scroll"] = True
        self.scroll_obtained = True
        return EncounterOutcome.CONTINUE


class Room:
    def __init__(self, name: str, encounter: Encounter):
        self.name = name
        self.encounter = encounter

    def visit_room(self) -> EncounterOutcome:
        return self.encounter.run_encounter()

# Create instances of DefaultEncounter, TreasureEncounter, RedWizardEncounter, BlueWizardEncounter, ShieldSpellEncounter, and InvisibilityScrollEncounter
default_encounter = DefaultEncounter()
treasure_encounter = TreasureEncounter()
red_wizard_encounter = RedWizardEncounter()
blue_wizard_encounter = BlueWizardEncounter()
shield_spell_encounter = ShieldSpellEncounter()
invisibility_scroll_encounter = InvisibilityScrollEncounter()

# Create a list of Room objects
rooms = [
    Room("Great Hall", default_encounter),
    Room("Dungeon", default_encounter),
    Room("Library", default_encounter),
    Room("Throne Room", default_encounter),
    Room("Armory", default_encounter),
    Room("Secret Chamber", default_encounter),
    Room("Wizard's Tower", red_wizard_encounter),  # Added RedWizardEncounter
    Room("Blue Wizard's Lair", blue_wizard_encounter),  # Added BlueWizardEncounter
    Room("Treasure Room", treasure_encounter),  # Added TreasureEncounter
    Room("Enchanted Chamber", shield_spell_encounter),  # Added ShieldSpellEncounter
    Room("Hidden Alcove", invisibility_scroll_encounter)  # Added InvisibilityScrollEncounter
]


class Castle:
    def __init__(self, rooms):
        self.room_selector = RandomItemSelector(rooms)

    def select_door(self) -> int:
        while True:
            try:
                num_doors = random.randint(2, 4)
                print(f"There are {num_doors} doors.")
                selected_door = int(input(f"Select a door number (1 to {num_doors}): "))
                if 1 <= selected_door <= num_doors:
                    return selected_door
                else:
                    print(f"Invalid choice. Please select a number between 1 and {num_doors}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def next_room(self) -> EncounterOutcome:
        self.select_door()
        room = self.room_selector.pull_random_item()
        print(f"You have entered the {room.name}.")
        return room.visit_room()

    def reset(self):
        self.room_selector.reset()


class Game:
    def __init__(self, rooms):
        self.castle = Castle(rooms)

    def play_game(self):
        print("Welcome to the Castle Adventure Game!")
        print("Your objective is to navigate through the castle and find the treasure.")
        print("Good luck!\n")

        while True:
            outcome = self.castle.next_room()
            if outcome == EncounterOutcome.END:
                self.castle.reset()
                print("Game Over")
                play_again = input("Would you like to explore a different castle? (Y/n): ").strip().lower()
                if play_again == '':
                    play_again = 'y'
                if play_again != 'y':
                    print("Thank you for playing the Castle Adventure Game!")
                    break
            elif outcome == EncounterOutcome.CONTINUE:
                continue_game = input("Do you want to continue exploring the castle? (Y/n): ").strip().lower()
                if continue_game == '':
                    continue_game = 'y'
                if continue_game != 'y':
                    print("Thank you for playing the Castle Adventure Game!")
                    break

# Run the game
game = Game(rooms)
game.play_game()
