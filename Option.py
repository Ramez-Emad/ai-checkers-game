from Draw_shapes import *
from General_Var import *


def Option_Screen():

    for event in pygame.event.get():

        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 340 <= mx <= 380 and 218 <= my <= 253:
                if Gn.Song_Played == 2:
                    Gn.Song_need_to_change = 1
                Gn.Song_Played = 1
            if 458 <= mx <= 495 and 218 <= my <= 253:
                if Gn.Song_Played == 1:
                    Gn.Song_need_to_change = 1
                    Gn.Song_Played = 2
            if 378 <= mx <= 455 and 454 <= my <= 498:
                Gn.choose_screen = 0
            if 348 <= mx <= 396 and 368 <= my <= 414:
                if Gn.Sound_Level < 10:
                    Gn.Sound_Level += 1
            if 455 <= mx <= 492 and 381 <= my <= 399:
                if Gn.Sound_Level > 0:
                    Gn.Sound_Level -= 1
        if event.type == pygame.QUIT:
            quit()

        setting_show()
        pygame.display.update()
