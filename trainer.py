import snake_random
from adn import ADN
from snake import Snake

class SnakeTrainer:
    def __init__(self):
        self.snakes = [Snake(ADN()) for i in range(100)]
    
    def playing(self):
        game = snake_random.SnakeGame()
        # game loop
        while True:
            vision = game.vision()
            j = self.feur.choose_move(vision)
            game_over, score = game.play_step(j)
            game.steps += 1
            game.total_steps += 1
            if game_over == True:
                game.steps = 0
                break
            
        print('-------------------------------------')
        print('Final Score', score)
        print('Total Steps', game.total_steps)
        fitness = (score*score) * (1/(game.total_steps))
        print('Fitness = ', fitness) # Score de fitness pour comparer les individus
    
if __name__ == "__main__":
    trainer = SnakeTrainer()
    trainer.playing()