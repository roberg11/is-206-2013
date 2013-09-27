class GameStep(object):
    def __init__(self,question=None,correct_choice=None,live=None,death=None):
        self.question = question
        self.correct_choice = correct_choice
        self.live = live
        self.death = death


class PrincessRoom(object):
    def __init__(self):
        self.steps = []
        self.steps.append(GameStep("Red pill or blue pill?",
                                   "Red",
                                   "you stay in Wonderland and I show you how deep the rabbit-hole goes",
                                   "the story ends, you wake up in your bed and believe whatever you want to believe"))
        self.steps.append(GameStep("Up or down?"
                                   "Up",
                                   "Up is way cooler than down",
                                   "Dude, you've fallen and you can't get up"))
        self.steps.append(GameStep("Left or right?",
                                   "Left",
                                   "Lefty loosey, You return from Princess' Lair!",
                                   "Righty tighty, you stay in the Room....FOREVER"))
 
    def play(self):
        for step in self.steps:
            print(step.question)
            choice = raw_input("> ")
            if choice.lower() == step.correct_choice.lower(): #use lower so all string comparisons are lowercase
                print(step.live)
                continue
            else:
                print(step.death)
                return False
        return True
