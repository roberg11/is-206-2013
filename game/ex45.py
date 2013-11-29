from ex45scenes import *

# Setup main game class
class Game(object):
    
    def __init__(self):
        self.map = Map('start')
        self.player = Player()
        self.engine = Engine(self.map)
        self.engine.play(self)

# Player class that creates a name object
class Player(object):
    
    def __init__(self):
        self.name = "noName"

# Map class with list of scenes in ex45scenes file
class Map(object):
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    scenes = {
        'start': Start(),
        'house': House(),
        'church': Church(),
        'toolshed': Toolshed(),
        'graveyard': Graveyard(),
        'crypt': Crypt(),
        'end': End(),
    }

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
# Item class with list of items available
# Note: Not yet functional
class Items(object):

    def __init__(self, inventory):
        self.inventory = inventory

    itemList = {
        "chain": 1,
        "gem": 2,
        "tooth": 3,
        "eye": 4,
    }

    necklace = False

    # Class not done

# Characters class with list of characters ingame
# Note: Not yet functional
class Characters(object):

    def __init__(self, charName):
        self.charName = charName

    charList = {
        "gravekeeper": 1,
        "vampire": 2,
        "zombie": 3,
        "bats": 4,
        "witch": 5,
        "murray": 6,
    }

    
# Engine class
class Engine(object):

    #
    def __init__(self, scene_map):
        self.scene_map = scene_map

    # Calls opening_scene() definition in class Map and assigns object to variable
    def play(self, game):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n--------"
            next_scene_name = current_scene.enter(game)
            current_scene = self.scene_map.next_scene(next_scene_name)

    
# Initializes the game
game = Game()
