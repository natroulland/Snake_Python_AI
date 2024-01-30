

class Snake:
    def __init__(self, adn):
        self.fitness = 0
        self.adn = adn

    def choose_move(self, vision):
        move = self.adn.getOutput(vision)
        move = move.tolist()
        choice = 0

        for i in range(0,len(move[0])):
            if move[0][i] > move[0][choice]:
                choice = i
        return choice +1
    
    def mate(self,other, mutationRate):
        newAdn = self.adn.mix(other.adn, mutationRate)
        return Snake(newAdn)