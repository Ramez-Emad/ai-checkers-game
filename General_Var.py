import pygame
from queue import LifoQueue

pygame.init()
"""
[1, 0, 1, 0, 1, 0, 1, 0],  # 0   empty cell
    [0, 1, 0, 1, 0, 1, 0, 1],  # 1   black cell
    [1, 0, 1, 0, 1, 0, 1, 0],  # 2   red cell
    [0, 0, 0, 0, 0, 0, 0, 0],  # 3   possible cell
    [0, 0, 0, 0, 0, 0, 0, 0],  # 4   Black (king) cell
    [0, 2, 0, 2, 0, 2, 0, 2],  # 5   red (king) cell
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2]"""

Board_pieces =[
        [1, 0, 1, 0, 1, 0, 1, 0],  # 0   empty cell
        [0, 1, 0, 1, 0, 1, 0, 1],  # 1   black cell
        [1, 0, 1, 0, 1, 0, 1, 0],  # 2   red cell
        [0, 0, 0, 0, 0, 0, 0, 0],  # 3   possible cell
        [0, 0, 0, 0, 0, 0, 0, 0],  # 4   Black (king) cell
        [0, 2, 0, 2, 0, 2, 0, 2],  # 5   red (king) cell
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2]
    ]


Counter_black = 0
Counter_red = 12


player_turn = 2
IS_sound_play = 0  # click
choose_screen = 0

option_clicked = 0
exit_clicked = 0
play_clicked = 0
Song_Played = 1
Song_need_to_change = 0
Sound_Level = 5
level = 1

pre_mx = 0    # original checker before move
pre_my = 0

pre_is_killed = 0    # flag determine if i kill an checker
pre_killed_x = 0
pre_killed_y = 0
Stack = []
Counter_for_timer = 0
Stack.append(Board_pieces)

click = pygame.mixer.Sound("Music/click.wav")


def init_game():
    global Board_pieces
    global player_turn
    global IS_sound_play
    global Counter_for_timer
    global pre_is_killed
    global Stack
    Board_pieces = [
        [1, 0, 1, 0, 1, 0, 1, 0],  # 0   empty cell
        [0, 1, 0, 1, 0, 1, 0, 1],  # 1   black cell
        [1, 0, 1, 0, 1, 0, 1, 0],  # 2   red cell
        [0, 0, 0, 0, 0, 0, 0, 0],  # 3   possible cell
        [0, 0, 0, 0, 0, 0, 0, 0],  # 4   Black (king) cell
        [0, 2, 0, 2, 0, 2, 0, 2],  # 5   red (king) cell
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2]
    ]
    player_turn = 1
    IS_sound_play = 1
    Counter_for_timer = 0
    pre_is_killed = 0
    Stack = []
    Stack.append(Board_pieces)
