

class Snake:
    def __init__(self, adn): # Initialise les paramètres du serpent
        self.fitness = 0
        self.adn = adn

    def choose_move(self, vision): # Permet de choisir le mouvement à effectuer
        move = self.adn.getOutput(vision)
        move = move.tolist()
        choice = 0

        for i in range(0,len(move[0])):
            if move[0][i] > move[0][choice]:
                choice = i
        return choice +1
    
    def mate(self,other, mutationRate): # Permet de croiser deux serpents
        newAdn = self.adn.mix(other.adn, mutationRate)
        return Snake(newAdn)