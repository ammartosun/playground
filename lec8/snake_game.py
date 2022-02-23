import math
import pygame
import random

# system constants
FRAME_SPEED = 5
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FOOD_COLOR = [255,255,255]
FOOD_SIZE = 5
SNAKE_SIZE = 25
SNAKE_COLOR = [0, 255, 0]
SEGMENT_SIZE = 15
BACKGROUND_COLOR = [0,0,0]


def exit_screen():
    exitFlag = False
    while not exitFlag:
        event = pygame.event.poll()
        if event.type==pygame.QUIT:
            exitFlag = True


# Food
class Food:
    '''Attribute: color, size, location'''
    def __init__(self):
        self.x = random.randint(SNAKE_SIZE+1, SCREEN_WIDTH-SNAKE_SIZE)
        self.y = random.randint(SNAKE_SIZE+1, SCREEN_HEIGHT-SNAKE_SIZE)
        self.size = FOOD_SIZE
        self.color = FOOD_COLOR
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

# Snake
class Snake:
    '''represents the snake/player in the game
    Attributes: location, color, direction, size, length, segments
    '''
    def __init__(self):
        self.x = SCREEN_WIDTH//2
        self.y = SCREEN_HEIGHT//2
        self.xdir = 1
        self.ydir = 0
        self.size = SNAKE_SIZE
        self.color = SNAKE_COLOR
        self.length = 3
        self.segments = []

    def draw(self, screen):
        for s in self.segments:
            s.draw(screen)
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
    
    def step(self):
        self.segments.append(Segment(self.x, self.y))
        if len(self.segments) > self.length:
            self.segments.pop(0)
        
        self.x += self.xdir * self.size
        self.y += self.ydir * self.size

    def up(self):
        self.xdir = 0
        self.ydir = -1
    def down(self):
        self.xdir = 0
        self.ydir = 1
    def left(self):
        self.xdir = -1
        self.ydir = 0
    def right(self):
        self.xdir = 1
        self.ydir = 0
    
    def eat(self):
        self.length += 1
    
    def die(self):
        self.color = [238,59,59]


class Segment:
    '''reperesnts one segment of the snake's body
    Att: location, size'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = SEGMENT_SIZE
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = [r,g,b]
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)


def distance(p1, p2):
    xdiff = p1.x - p2.x
    ydiff = p1.y - p2.y
    return math.sqrt(xdiff*xdiff + ydiff*ydiff)


# Game display
def main():
    # screen
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    # timer
    clock = pygame.time.Clock()

    # initialize the food and snake
    snake = Snake()
    food = Food()

    running = True
    # game loop
    while running:
        events = pygame.event.get()
        # poll/get event
        for event in events:        
            if event.type == pygame.QUIT:
                running = False
            # handle keyboard events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.up()
                elif event.key == pygame.K_DOWN:
                    snake.down()
                elif event.key == pygame.K_LEFT:
                    snake.left()
                elif event.key == pygame.K_RIGHT:
                    snake.right()

        # snake move
        snake.step()
    
        # detect collision: food 
        if distance(snake, food) < snake.size + food.size:
            snake.eat()
            food = Food()

        # detect collision: segment
        for s in snake.segments:
            if distance(snake, s) < snake.size:
                snake.die()
                running = False

        # draw everything
        # draw background
        screen.fill(BACKGROUND_COLOR)

        # draw food
        food.draw(screen)
        # draw snake
        snake.draw(screen)

        # flip display
        pygame.display.flip()
        # tick timer
        clock.tick(FRAME_SPEED)
    
    exit_screen()


main()
