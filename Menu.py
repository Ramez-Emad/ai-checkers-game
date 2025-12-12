from Draw_shapes import *
from General_Var import *


def Menu_Screen():

    for event in pygame.event.get():
        if Gn.play_clicked:
            Gn.choose_screen = 1
            init_game()
        elif Gn.option_clicked:
            Gn.choose_screen = 2
        Gn.option_clicked = 0
        Gn.exit_clicked = 0
        Gn.play_clicked = 0
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 228 <=mx <= 573 and 65 <= my <= 165:
                Gn.play_clicked = 1
                Gn.level = 1
            elif 216 <= mx <= 580 and 195 <= my <= 295:
                Gn.play_clicked = 1
                Gn.level = 2
            elif 216 <= mx <= 580 and 325 <= my <= 425:
                Gn.option_clicked = 1
            elif 216 <= mx <= 580 and 455 <= my <= 555:
                quit()
        if event.type == pygame.QUIT:
            quit()

        menu_show()
        pygame.display.update()
