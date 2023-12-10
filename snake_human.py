import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

font = pygame.font.SysFont('arial', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
GREEN1 = (153, 255, 51)
GREEN2 = (178, 255, 102)

BLOCK_SIZE = 64
SPEED = 10
MAX_STEPS = 100

class SnakeGame:
    
    def __init__(self, w=640, h=640):
        self.w = w
        self.h = h
        self.steps = 0
        self.total_steps = 0
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        
        # init game state
        self.direction = Direction.RIGHT
        
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x, self.head.y-BLOCK_SIZE),
                      Point(self.head.x, self.head.y-(2*BLOCK_SIZE))]
        
        self.score = 0
        self.food = None
        self._place_food()
        
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()
        
    def play_step(self):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
        
        # 2. move
        self._move(self.direction) # update the head
        self.snake.insert(0, self.head)
        
        # 3. check if game over
        game_over = False
        if self._is_collision() or self.steps == MAX_STEPS:
            game_over = True
            return game_over, self.score
            
        # 4. place new food or just move
        if self.head == self.food:
            self.steps = 0
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        # 6. return game over and score
        return game_over, self.score
    
    def _is_collision(self):
        # hits boundary
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        # hits itself
        if self.head in self.snake[1:]:
            return True
        
        return False
        
    def _update_ui(self):
        for y in range(0, self.h, BLOCK_SIZE):
            for x in range(0, self.w, BLOCK_SIZE):
                # Alternance des couleurs
                if (x + y) // BLOCK_SIZE % 2 == 0:
                    pygame.draw.rect(self.display, GREEN1, (x, y, BLOCK_SIZE, BLOCK_SIZE))
                else:
                    pygame.draw.rect(self.display, GREEN2, (x, y, BLOCK_SIZE, BLOCK_SIZE))
        
        pygame.draw.rect(self.display, BLUE1, pygame.Rect(self.snake[0].x, self.snake[0].y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, BLUE2, pygame.Rect(self.snake[0].x+12.8, self.snake[0].y+12.8, 38.4, 38.4))

        pygame.draw.circle(self.display, BLACK, (self.snake[0].x + BLOCK_SIZE // 3, self.snake[0].y + BLOCK_SIZE // 3), 5)
        pygame.draw.circle(self.display, BLACK, (self.snake[0].x + 2 * BLOCK_SIZE // 3, self.snake[0].y + BLOCK_SIZE // 3), 5)
    
        pygame.draw.arc(self.display, BLACK, pygame.Rect(self.snake[0].x + BLOCK_SIZE // 4, self.snake[0].y + 3 * BLOCK_SIZE // 5, BLOCK_SIZE // 2, BLOCK_SIZE // 4), 0, 3.14, 2)

        for pt in self.snake[1:]:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+12.8, pt.y+12.8, 38.4, 38.4))
            
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        text = font.render("Score: " + str(self.score), True, BLACK)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
        
    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
            
        self.head = Point(x, y)
            

if __name__ == '__main__':
    for i in range(10):
        game = SnakeGame()
        
        # game loop
        while True:
            game_over, score = game.play_step()
            game.steps += 1
            game.total_steps += 1
            if game_over == True:
                game.steps = 0
                break
            
        print('-------------------------------------')
        print('Final Score', score)
        print('Total Steps', game.total_steps)
        print('Fitness = ', (score*score) * (1/(game.total_steps))) # Score de fitness pour comparer les individus
        
            
        
    pygame.quit()