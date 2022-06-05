import time
import sys
import pygame
import random
from pygame.math import Vector2

if __name__ == "__main__":
    class Snake:
        def __init__(self) -> None:
            self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
            self.direction = Vector2(1, 0)
            self.new_block = False
            self.sound = pygame.mixer.Sound("sounds/coin1.mp3")

        def draw_snake(self):
            for block in self.body:
                x_position = block.x * cell_size
                y_position = block.y * cell_size
                block_rect = pygame.Rect(
                    x_position, y_position, cell_size, cell_size)
                pygame.draw.rect(screen, ("white"), block_rect)

        def move_snake(self):
            if self.new_block == True:

                body_copy = self.body[:]
            # slicing
                body_copy.insert(0, body_copy[0] + self.direction)
            # copy the self.body list but remove last item
            # for head add one block to front
                self.body = body_copy[:]
            # returns list to body copy
            # only want to execute this method at certain intervals
                self.new_block = False
            else:

                body_copy = self.body[:-1]
            # slicing
                body_copy.insert(0, body_copy[0] + self.direction)
            # copy the self.body list but remove last item
            # for head add one block to front
                self.body = body_copy[:]
            # returns list to body copy
            # only want to execute this method at certain intervals

        def add_block(self):
            self.new_block = True

        def play_sound(self):
            self.sound.play()

    class Fruit:
        def __init__(self):
            self.randomize()

        def draw_fruit(self):
            # create a rectangle and then draw
            fruit_rectangle = pygame.Rect(
                self.postion.x * cell_size, self.postion.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, ("red"), fruit_rectangle)

        def randomize(self):
            self.x = random.randint(0, cell_number - 1)
            self.y = random.randint(0, cell_number - 1)
            self.postion = Vector2(self.x, self.y)

    class Main:
        def __init__(self) -> None:
            self.snake = Snake()
            self.fruit = Fruit()

        def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

        def draw_elements(self):
            self.fruit.draw_fruit()
            self.snake.draw_snake()

        def check_collision(self):
            if self.fruit.postion == self.snake.body[0]:
                self.fruit.randomize()
                # want to reposition the fruit
                # add another block to the snake
                self.snake.add_block()
                self.snake.play_sound()

        def check_fail(self):
            # check if snake hits itself
            if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
                # checks vector left and right
                self.game_over()
            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()

        def game_over(self):
            pygame.quit()
            sys.exit()

    pygame.init()
    cell_size = 25
    cell_number = 25
    screen = pygame.display.set_mode(
        (cell_number * cell_size, cell_number * cell_size))
    clock = pygame.time.Clock(
        # helps set a speed for the while loop
        # helps set a maximum frame rate for consistent game running
    )
    screen_update = pygame.USEREVENT
    pygame.time.set_timer(screen_update, 100)
    # triggers event x milliseconds

    main_game = Main()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(
                    # looks for an input to quit the game
                )
                sys.exit(
                    # allows dev to exit from the game
                )
            if event.type == screen_update:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                        # if direction is anything but 1, move downwards
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)

        screen.fill(pygame.Color("black"
                                 # colour of the display of the background surface
                                 ))
        main_game.draw_elements()
        pygame.display.update(
            # draws all our elements
            # update can be any user inputs
        )
        clock.tick(60
                   # game will stay at 60 frames a second
                   )
