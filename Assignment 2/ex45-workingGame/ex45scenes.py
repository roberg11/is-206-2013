class Scene(object):

    # Empty dictionaries of hints and dialogs
    hints = {}
    dialogs = {}
    
    def enter(self, game):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
        
    # Action handling
    def actions(self, actions):
        actionText = {
          'goto': 'Go to', 
          'talkto': 'Talk to',
          'examine': 'Examine',
        }
        actionKeys = {}
        # Loop that always runs (always is True)
        while(True):
            # Prints the current room name
            print "-------------------------------"
            print self.__class__.__name__
            print "-------------------------------"
            actionIndex = 0
            # Iterate over player actions and compares user input with possible actions in actionKeys dict
            for action in actions:
                actionIndex+=1
                actionKeys[action] = actionIndex
                print "[%s]: %s" % (actionIndex, actionText[action])

            playerAction = raw_input("> ")

            # Read action input and calls the definition equal to input in actionText[action] dictionary

            # Calls the goto function if user input does not equal any elements to actionText[action]
            if('goto' in actions):
                if(playerAction == str(actionKeys['goto'])):
                    goto = self.goto(self.__class__.__name__.lower())
                    if(goto != False):
                        return goto
                    
            if('talkto' in actions):
                if(playerAction == str(actionKeys['talkto'])):
                    self.talkto()
                    
            if('examine' in actions):
                if(playerAction == str(actionKeys['examine'])):
                    self.examine()
                    
    # Go to handling
    def goto(self, currentSceneName):
        index_of_scene = 0
        list_of_scene = []
        print "Go to:"
        # Iterate over scenes
        for scene in self.game.map.scenes:
            if(scene in ['end','start']): 
                continue
            # Print all scene options that the player is not in
            if(scene != currentSceneName):
                list_of_scene.append(scene)
                index_of_scene+=1
                print "[%s]: %s" % (index_of_scene,scene.capitalize())
            
        playerAction = raw_input("> ")

        # If player does not enter a digit return False
        if(playerAction.isdigit() != True):
            return False

        # If player input number is more than lenght of list_of_scenes return False
        if(len(list_of_scene) < int(playerAction)):
            return False
        
        return list_of_scene[int(playerAction)-1]
    
    # Dialog handling
    def talkto(self):
        dialogNum = 0
        list_of_dialog = []

        # Appends all dialogs available in each scene to list_of_dialog and prints them
        for dialog in self.dialogs.keys():
            list_of_dialog.append("%s: %s" % (dialog.capitalize(), self.dialogs[dialog]))
            dialogNum += 1
            print "[%s]: %s"  % (dialogNum, dialog.capitalize())
        
        playerAction = raw_input("> ")

        # If player does not enter a digit return False
        if(playerAction.isdigit() != True):
            return False

        # If player input number is more than lenght of list_of_dialog return False
        if(len(list_of_dialog) < int(playerAction)):
            return False
        
        print list_of_dialog[int(playerAction)-1]
        
    # Examine handling
    def examine(self):
        hint_number = 0
        list_of_hints = []

        # Appends all hints available in each scene to list_of_hints and prints them
        for hint in self.hints.keys():
            list_of_hints.append(self.hints[hint])
            hint_number += 1
            print "[%s]: %s"  % (hint_number, hint.capitalize())
        
        playerAction = raw_input("> ")

        # If player does not enter a digit return False
        if(playerAction.isdigit() != True):
            return False

        # If player input number is more than lenght of list_of_hints return False
        if(len(list_of_hints) < int(playerAction)):
            return False
        
        print list_of_hints[int(playerAction)-1]

class Start(Scene):
    def enter(self, game):
        self.game = game
        print "Enter your name: "
        
        # Calls the definition inside Player class and assigns player name to self.name
        game.player.name = raw_input("> ")
        print "You have arrived at a dark and loomy place %s" % game.player.name
        print "Type in some numbers to see where you can go."
        
        return self.actions(['goto'])
        

class House(Scene):

    hints = {
             'zombie': 'His left arm seems to be ripped off!'
    }
    
    dialogs = {
              'stay': 'Wonderful, this way please',
              'leave': 'Please come again'
    }

    def enter(self, game):
        self.game = game
        print "Zombie: \"Welcome %s, I will be your host for the evening." % game.player.name # calls player name
        print "%s: \"What is this place?\""
        print "Zombie: \"This is the Late Brain Inn. Do you want a room?\""
        print "*****************************"
        print "What do you want to do next?"
        
        actions = ['goto']

        # If dialogs dictionary has elements, calls actions parameter in talkto definition of class Scene
        if(len(self.dialogs)>0):
            actions.append('talkto')

        # If hints dictionary has elements, calls actions parameter in examine definition of class Scene
        if(len(self.hints)>0):
            actions.append('examine')
        
        return self.actions(actions)

class Church(Scene):

    hints = {
        'vampire': 'The creature is very pale with just one pointy tooth, the other one seems to be lost.'
    }

    dialog = {
        'vampire': 'Leave this place!!'
    }
    
    def enter(self, game):
        self.game = game
        print "A sudden flash followed by white smoke appears as you enter the church and a vampire shows up from the smoke"
        print "Vampire: Welcome to this holy place %s" % game.player.name
        print "%s: Can I enter the churc?"
        print "Vampire: No!"
        print "%s: Why did you say welcome then?"
        print "Vampire: I thought you were someone else."
        print "*****************************"
        print "What do you want to do next?"
        
        actions = ['goto']
        if(len(self.dialogs)>0):
            actions.append('talkto')
            
        if(len(self.hints)>0):
            actions.append('examine')
        
        return self.actions(actions)
        
class Toolshed(Scene):

    hints = {
        'bats': 'The bats are completely still.'
    }

    dialogs = {
        'bats': 'No response'
    }

    def enter(self, game):
        self.game = game
        print "Inside the toolshed you see alot of junk and some bats hanging from the ceeling."
        print "The bats seems to be sleeping... for now."
        print "*****************************"
        print "What do you want to do next?"
        
        actions = ['goto']
        if(len(self.dialogs)>0):
            actions.append('talkto')
            
        if(len(self.hints)>0):
            actions.append('examine')
        
        return self.actions(actions)
        
class Graveyard(Scene):

    hints = {
        'gravekeeper': 'The gravekeeper looks tired, and you notice he has a long thin chain around his neck'
    }

    dialogs = {
        'gravekeeper': 'Why are you staring at me? Haven\'t you seen a hunchback before?',
        'chain': 'Gravekeeper: Fine, I\'ll give you the chain'
    }
    
    def enter(self, game):
        self.game = game
        print "You enter the graveyard and see a man with a hunchback approaching"
        print "Gravekeeper: Welcome to the graveyard young %s" % game.player.name
        print "*****************************"
        print "What do you want to do next?"
        
        actions = ['goto']
        if(len(self.dialogs)>0):
            actions.append('talkto')
            
        if(len(self.hints)>0):
            actions.append('examine')
        
        return self.actions(actions)
        
class Crypt(Scene):
    
    hints = {
         'trash_can': 'You see a red gem lying in the bottom.',
         'skeleton': 'Looks like a normal skeleton apart from a few missing teeths.',
    }

    dialogs = {
        'murray' : 'The red light scares me, but I\'m still evil!'
    }
    
    def enter(self, game):
        self.game = game
        print "You enter the crypt and see a skeleton without its head."
        print "Suddenly a dark voice echoes in by the entrance."
        print "Murray: \"Greetings %s, I am the evil demonic skull, Murray.\"" % game.player.name
        print "%s: \"Why is your head placed in a trashcan?\"." % game.player.name
        print "Murray: \"It's those damned voodoo kids.\""
        print "%s: \"Do you want me to attach your head to your body?\"." % game.player.name
        print "Murray: \"That's not my body but yes, please do\"."
        print "*****************************"
        print "What do you want to do next?"
        
        actions = ['goto']
        if(len(self.dialogs)>0):
            actions.append('talkto')
            
        if(len(self.hints)>0):
            actions.append('examine')
        
        return self.actions(actions)
                
class End(Scene):

    # Not yet implemented
    def enter(self, game):
        self.game = game
        print "You exit the fog with the necklace"
        print "Congratulations, you've finished the game.!"

class Dead(Scene):

    # Not yet implemented
    def death(self, game):
        self.game = game
        print "You died."
 
