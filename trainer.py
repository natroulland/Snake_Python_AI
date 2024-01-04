import snake_random
from adn import ADN
from snake import Snake

class SnakeTrainer:
    def __init__(self):
        self.snakes = [Snake(ADN()) for i in range(100)]
        self.bestFitness = 0
        self.bestScore = 0
        self.bestSnake = self.snakes[0]
        self.bestGenFitness = 0
        self.generation = 0
        self.totalGenScore = 0
        self.bestGenScore = 0
    
    def playing(self):
        for snake in self.snakes:
            game = snake_random.SnakeGame()
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
            fitness = (score*score) * (1/(game.total_steps))
            if fitness > self.bestFitness:
                self.bestFitness = fitness
                self.bestSnake = snake
            if score > self.bestScore:
                self.bestScore = score
            self.totalGenScore += score
        print("Generation : ", self.generation)
        print("Best fitness : ", self.bestFitness)
        print("Best score : ", self.bestScore)
        print("Average score : ", self.totalGenScore/100)
        print("Total Score : ", self.totalGenScore)

    
if __name__ == "__main__":
    trainer = SnakeTrainer()
    trainer.playing()
