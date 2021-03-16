import pygame
import sys
import random
from pygame.math import Vector2


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.eat_fruit()
        self.game_fail()

    def draw_elements(self):
        # Draw the snake and fruit
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def eat_fruit(self):
        if self.fruit.x_y_cord == self.snake.body[0]:
            self.fruit.new_fruit()
            self.snake.add_segment()

    def game_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_color = (150, 200, 60)

        for row in range(cell_number):
            if row % 2 == 0:
                for column in range(cell_number):
                    if column % 2 == 0:
                        grass_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(display_screen, grass_color, grass_rect)
            else:
                for column in range(cell_number):
                    if column % 2 != 0:
                        grass_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(display_screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 4)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(display_screen_dimensions - 45)
        score_y = int(display_screen_dimensions - 45)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(center=(score_x - 30, score_y))

        display_screen.blit(score_surface, score_rect)
        display_screen.blit(apple, apple_rect)


class SNAKE:

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10), Vector2(2, 10)]
        # A bunch of rectangles that represent the snake
        self.direction = Vector2(1, 0)

        self.head_up = pygame.image.load('Snake_game_images/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Snake_game_images/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Snake_game_images/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Snake_game_images/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Snake_game_images/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Snake_game_images/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Snake_game_images/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Snake_game_images/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Snake_game_images/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Snake_game_images/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Snake_game_images/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Snake_game_images/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Snake_game_images/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Snake_game_images/body_bl.png').convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size) - 5
            y_pos = int(block.y * cell_size) - 5
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                display_screen.blit(self.head, block_rect)

            elif index == len(self.body) - 1:
                display_screen.blit(self.tail, block_rect)

            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    display_screen.blit(self.body_vertical, block_rect)
                if previous_block.y == next_block.y:
                    display_screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or next_block.x == -1 and previous_block.y == -1:
                        display_screen.blit(self.body_tl, block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or next_block.x == -1 and previous_block.y == 1:
                        display_screen.blit(self.body_bl, block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or next_block.x == 1 and previous_block.y == -1:
                        display_screen.blit(self.body_tr, block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or next_block.x == 1 and previous_block.y == 1:
                        display_screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        body_copy = self.body[:-1]  # entire snake except the last segment
        body_copy.insert(0, body_copy[0] + self.direction)  # adds the head segment to the rest of snake
        self.body = body_copy

    def add_segment(self):
        new_segment = self.body[-1]
        self.body.append(new_segment)


class FRUIT:
    def __init__(self):
        self.new_fruit()

    def draw_fruit(self):
        # create a rect
        # draw the rect
        fruit_rect = pygame.Rect(self.x_pos, self.y_pos, cell_size, cell_size)  # x-cord, y-cord, width and height
        display_screen.blit(apple, fruit_rect)

    def new_fruit(self):
        # create an x and y position
        # Draw a square at that position
        self.x_cord = random.randint(0, cell_number - 1)
        self.y_cord = random.randint(0, cell_number - 1)
        self.x_y_cord = Vector2(self.x_cord, self.y_cord)
        self.x_pos = int(self.x_y_cord.x * cell_size) - 5
        self.y_pos = int(self.x_y_cord.y * cell_size) - 5


# GAME DEFINITIONS
# Initiate pygame
pygame.init()

# Limits how fast game can run
clock = pygame.time.Clock()
framerate = 100

# Make window screen
cell_size = 30
cell_number = 20
display_screen_dimensions = cell_size * cell_number
display_screen = pygame.display.set_mode((display_screen_dimensions, display_screen_dimensions))

# Custom event that is triggered by the timer
SCREEN_UPDATE = pygame.USEREVENT
# Timer
pygame.time.set_timer(SCREEN_UPDATE, 150)  # this even will be triggered every 150 milli-seconds

# Make main
main_game = MAIN()

# Import apple
apple = pygame.image.load('Snake_game_images/apple.png').convert_alpha()

# Game font:
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

# Game Event loop. Infinite
while True:
    # check every event done in the loop
    for event in pygame.event.get():

        # If a player hits the "x" on the top right, they close the window.
        # That event is seen as pygame.QUIT and so we want to close the application
        if event.type == pygame.QUIT:
            pygame.quit()  # opposite of pygame.init
            sys.exit()  # completely closes the screen

        # Every 150 milsec it adds SCREEN_UPDATE to list of events
        # If SCREEN_UPDATE appears in events, it moves the snake
        if event.type == SCREEN_UPDATE:
            main_game.update()

        # If user presses a key
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)

    # Change color of screen
    display_screen.fill((175, 230, 70))

    # Draw snake and fruit
    main_game.draw_elements()

    # Update the what we have drawn on the screen
    pygame.display.update()

    # Limits of game framerate
    clock.tick(framerate)
