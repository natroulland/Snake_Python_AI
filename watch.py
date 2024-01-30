from adn import ADN
from snake import Snake
import random as rd
from os import listdir
import pickle
from pathlib import Path
import snake_random

class Watch : 
    def __init__(self):
        print("Quel est le score du serpent que vous voulez charger ?")
        x = input()
        x += ".snake"
        with open(Path("best_snakes/"+x), "rb") as f:
                weights = pickle.load(f)
        self.snake = Snake(ADN(weights))

    def playing(self):
        for i in range(10):
            game = snake_random.SnakeGame(training = False, generation = 0)
            # game loop
            while True:
                vision = game.vision()
                j = self.snake.choose_move(vision)
                game_over, score = game.play_step(j)
                game.steps += 1
                game.total_steps += 1
                if game_over == True:
                    game.steps = 0
                    break

if __name__ == "__main__":
    watch = Watch()
    watch.playing()