"""
Member List
- Batchansaa Batzorig
- Dmitri Golota
- Sally Poon
- Subin Moon
- Martin Gatchev

Mar 13, 2021
"""


import pygame
import sys
import random
from pygame_functions import *
import time

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Namu")

WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
clock = pygame.time.Clock()
#pygame.mixer.music.load("./assets/sounds/NAMU-1.mp3")
#pygame.mixer.music.play(loops=-1)

# Game Classes

class Namu(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = True
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f1.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f2.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f3.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f4.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f5.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f6.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f7.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f8.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f9.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f10.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f11.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f12.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


    def update(self):
        if self.is_animating:
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]


class button():

    # colours for button and text
    button_col = (39, 60, 117)
    hover_col = ()
    click_col = ()
    text_col = (255, 255, 255)
    width = 100
    height = 70



# class test

# Namu class test

moving_sprite = pygame.sprite.Group()
player = Namu(100, 100)
moving_sprite.add(player)

 # Namu class test



# Game Variables
game_font = pygame.font.Font('./assets/Fipps_font.otf', 14)
score = 0
high_score = 0

# Floor_Sand
sand_surface = pygame.image.load('./assets/new_sand.png').convert()
sand_surface = pygame.transform.scale(sand_surface, (512, 56))
sand_x_position = 0

# Background_Image
bg_1 = pygame.image.load('./assets/bg-1.png').convert()
bg_1 = pygame.transform.scale(bg_1, (512, 512))
bg_x_position = 0

# Obstacles
obstacle_1 = pygame.image.load('./assets/iceberg.png')
obstacle_1 = pygame.transform.scale(obstacle_1, (100, 160))


# Game Functions
def generate_random_question():
    questions_to_be_asked = {
        "How many different species of fish exist in the Ocean?":
            [["15_000", "32_000", "40_000", "23_000"],
             1,
             "32 000! This is greater than the total of all other \
            vertebrate species (amphibians, reptiles, birds, and mammals) combined."],
        "The Ocean contributes to: ":
            [["Producing Oxygen and storing Carbon Dioxide",
              "Regulating weather and climate",
              "Nutrient-rich food chains",
              "All the above"],
             3,
             "All the above. The Ocean is thus essential to life on Earth from producing \
            50-80% of the Oxygen we breath, regulating the seasons, and sustaining food \
            chains on and off land."],
        "How much of the Ocean have humans been able to map, explore, and observe?":
            [["20%", "35%", "55%", "we've mapped all of it!"],
             0,
             "Roughly 20%. The Ocean covers 70% of our planet's surface, 80% of it still \
            remains unobserved, undiscovered, and unmapped."],
        "How many species live in the Ocean?":
            [["78 300", "360 000", "620 000", "I'm not really sure"],
             3,
             "Trick question! Scientists have no way of tracking how many species there \
            are in the ocean since the majority of it has yet to be observed. They \
            estimate that there are roughly 91% of species remain undiscovered in \
            the ecosystem; there can be millions of species!"
            ]
    }
    question_for_this_turn = random.choice(questions_to_be_asked.keys())
    return question_for_this_turn, questions_to_be_asked[question_for_this_turn]


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(score), True, (39, 60, 117))
        score_rect = score_surface.get_rect(center=(250, 17))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (39, 60, 117))
        score_rect = score_surface.get_rect(center=(250, 17))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (39, 60, 117))
        high_score_rect = high_score_surface.get_rect(center=(250, 400))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


def move_sand(floor_position):
    floor_position -= 10
    screen.blit(sand_surface, (floor_position, 445))
    screen.blit(sand_surface, (floor_position + 500, 445))
    if floor_position <= - 500:
        return 0
    else:
        return floor_position


def move_bg(bg_position):
    bg_position -= 2
    screen.blit(bg_1, (bg_position, 0))
    screen.blit(bg_1, (bg_position + 500, 0))
    if bg_position <= - 500:
        return 0
    else:
        return bg_position


# Main Loop
game_active = True
game_running = True

while game_running:
    pygame.time.delay(100)

    for event in pygame.event.get():      # catch all the events that are happening right now
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_running = False

        if event.type == pygame.QUIT: # Quitting the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # Move Namu with space bar
            if event.type == pygame.K_SPACE:
                pass


    # Background image
    bg_x_position = move_bg(bg_x_position)
    sand_x_position = move_sand(sand_x_position)
    screen.blit(obstacle_1, (0, 0))


    if game_active:
        # image of player

        moving_sprite.draw(screen)
        moving_sprite.update()


        # Game Functions
        score_display('main_game')

    # game over
    else:
        score_display('game_over')
        time.sleep(5)
    pygame.display.update()
    clock.tick(120)

pygame.quit()