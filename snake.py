import random

class Snake:
    def __init__(self, adn):
        self.fitness = 0
        self.adn = adn

    def choose_move(self, vision):
        move = self.adn.getOutput(vision)
        move = move.tolist()
        print(move)
        choice = 0

        for i in range(1,len(move[0])):
            print(i)
            if move[0][i] > move[0][choice]:
                choice = i
        print(choice)
        return choice