from rooms import PrincessRoom

import sys

class Game(object):
    def __init__(self,rooms):
        self.rooms = rooms

    def play(self):
        for room in self.rooms:
            if(room.play()):
                continue
            else:
                print("Game Over!")
                sys.exit(1)
        print("You win!")
       
if __name__=="__main__":
    G = Game([PrincessRoom()])
    G.play()
 
