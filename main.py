from Menu import *
from Game import *
from Option import *

pygame.mixer.music.load("Music/Back1.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer_music.set_volume(0.5)

while True:
    '''time to process action was taken is 5ms'''
    if Gn.Song_need_to_change:
        Gn.Song_need_to_change = 0
        if Gn.Song_Played == 1:
            pygame.mixer.music.load("Music/Back1.mp3")
            pygame.mixer.music.play(-1, 0.0)

        else:
            pygame.mixer.music.load("Music/Back2.mp3")
            pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(Gn.Sound_Level/10)
    '''store events that that was taken by keyboard and mouse here the action is quit the game when click exit'''
    if Gn.choose_screen == 0:
        Menu_Screen()
    elif Gn.choose_screen == 1:
        Game_Screen()
    elif Gn.choose_screen == 2:
        Option_Screen()