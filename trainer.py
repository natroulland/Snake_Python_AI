import snake_random
from adn import ADN
from snake import Snake
import random as rd
from os import listdir
import pickle
from pathlib import Path
import add_values
import save_training

class SnakeTrainer:
    def __init__(self, snakes = None):
        self.bestFitness = 0
        self.bestScore = 0
        self.bestGenFitness = 0
        self.generation = 1
        self.totalGenScore = 0
        self.bestGenScore = 0
        self.nbrSnakes = 500
        self.survivalProportion = 0.12
        self.mutationRate = 0.05
        self.snakes = snakes
        if self.snakes == None:
            self.snakes = []
            for i in range(self.nbrSnakes):
                self.snakes.append(Snake(ADN()))
        self.bestSnake = self.snakes[0]

    
    def training(self):
        bestScore = -1
        bestFitness = -1
        itEnd = 0

        # Create new generations until the stop condition is satisfied
        while itEnd < 250:
            print(
                f"Generation {self.generation}, best: {bestScore}, bestfit: {bestFitness}"
            )
            self.playing()
            currentScore = self.bestGenScore
            currentFitness = self.bestGenFitness
            self.change_generation()

            # Check if the game score or fitness for this generation improved
            if currentScore <= bestScore and currentFitness <= bestFitness:
                itEnd += 1
            else:
                # Improvement + reset counter
                bestScore = max(bestScore, currentScore)
                bestFitness = max(bestFitness, currentFitness)
                itEnd = 0

    def change_generation(self):
        newSnakes = sorted(self.snakes, key=lambda x: x.fitness, reverse=True)
        newSnakes = newSnakes[:int(self.nbrSnakes*self.survivalProportion)]
        snakesToAdd = []

        while len(newSnakes)+len(snakesToAdd) < self.nbrSnakes:
            parents = self.select_parents(newSnakes)
            child = parents[0].mate(parents[1], mutationRate = self.mutationRate)
            snakesToAdd.append(child)

        newSnakes += snakesToAdd

        self.snakes = newSnakes

        self.bestGenFitness = 0
        self.bestGenScore = 0
        self.totalGenScore = 0
        self.generation += 1

    def select_parents(self, matingSnakes):
        parents = []
        popSize = len(matingSnakes)
        totalFitness = popSize / 2 * (popSize + 1)

        for t in range(2):
            r = rd.randint(0, totalFitness - 1)
            i = 0
            used = None

            while i < len(matingSnakes):
                if r < popSize - i:
                    parents.append(matingSnakes[i])
                    totalFitness -= popSize
                    popSize -= 1
                    used = i
                    break

                r -= popSize - i
                i += 1

                if i == used:
                    i += 1
        return parents


    def playing(self):
        for snake in self.snakes:
            game = snake_random.SnakeGame(training = True, generation = self.generation)
            # game loop
            while True:
                vision = game.vision()
                j = snake.choose_move(vision)
                game_over, score = game.play_step(j)
                game.steps += 1
                game.total_steps += 1
                if game_over == True:
                    game.steps = 0
                    break
            fitness = game.steps+(2**score+score**2.1*500)-((score**1.2)*((0.25*game.steps)**1.3))
            snake.fitness = fitness


            self.bestGenFitness = max([fitness, self.bestGenFitness])
            self.bestFitness = max([fitness, self.bestFitness])
            self.bestGenScore = max([score, self.bestGenScore])
            self.totalGenScore += score

            if fitness == self.bestGenFitness:
                self.bestSnake = snake

        
        print("Best fitness Generation: ", self.bestGenFitness)
        print("Best score Generation : ", self.bestGenScore)
        print("Average score : ", self.totalGenScore/self.nbrSnakes)
        print("Total Score : ", self.totalGenScore)
        # Lire les nouvelles valeurs depuis l'utilisateur
        nouvelles_valeurs = [self.generation, self.bestGenScore]

        add_values.inscrire_et_modifier("valeurs_graphes.txt", nouvelles_valeurs)

         # Save the weights and biases of the snakes for the new game scores
        files = listdir(Path("best_snakes"))

        # If this is a new game score
        if str(self.bestGenScore) + ".snake" not in files:
            with open(
                Path("best_snakes") / Path(str(self.bestGenScore) + ".snake"), "wb"
            ) as f:
                pickle.dump(
                    (self.bestSnake.adn.weights), f
                )

if __name__ == "__main__":
    trainer = SnakeTrainer()
    trainer.training()
 