import pygame
import General_Var as Gn
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Checker Game")


def sound(Is_Played):
    if Is_Played:
        Board = pygame.image.load("Photos/sound.png")
    else:
        Board = pygame.image.load("Photos/mute.png")
    DEFAULT_IMAGE_SIZE = (60, 60)
    Board = pygame.transform.scale(Board, DEFAULT_IMAGE_SIZE)
    screen.blit(Board, (25, 85))

    Board = pygame.image.load("Photos/reset.png")
    DEFAULT_IMAGE_SIZE = (60, 60)
    Board = pygame.transform.scale(Board, DEFAULT_IMAGE_SIZE)
    screen.blit(Board, (25, 160))


def timer(angle):
    Board = pygame.image.load("Photos/timer.png")
    Board = pygame.transform.rotate(Board, angle)
    screen.blit(Board, (725, 25))


def cancel():
    Board = pygame.image.load("Photos/cancel.png")
    DEFAULT_IMAGE_SIZE = (60, 60)
    Board = pygame.transform.scale(Board, DEFAULT_IMAGE_SIZE)
    screen.blit(Board, (25, 10))


def back_ground():  # background
    Board = pygame.image.load("Photos/boardback.png")
    DEFAULT_IMAGE_SIZE = (800, 600)
    Board = pygame.transform.scale(Board, DEFAULT_IMAGE_SIZE)
    screen.blit(Board, (0, 0))


def board():
    Board = pygame.image.load("Photos/board.png")
    DEFAULT_IMAGE_SIZE = (600, 600)
    Board = pygame.transform.scale(Board, DEFAULT_IMAGE_SIZE)
    screen.blit(Board, (100, 0))


def piece_location():
    for x in range(8):
        for y in range(8):
            if Gn.Board_pieces[x][y] == 1:
                piece = pygame.image.load("Photos/black.png")
                DEFAULT_IMAGE_SIZE = (60, 60)
                piece = pygame.transform.scale(piece, DEFAULT_IMAGE_SIZE)
                screen.blit(piece, (145 + (y * 64), 46 + (x * 64)))
            if Gn.Board_pieces[x][y] == 2:
                piece = pygame.image.load("Photos/red.png")
                DEFAULT_IMAGE_SIZE = (60, 60)
                piece = pygame.transform.scale(piece, DEFAULT_IMAGE_SIZE)
                screen.blit(piece, (145 + (y * 64), 46 + (x * 64)))
            if Gn.Board_pieces[x][y] == 3:
                piece = pygame.image.load("Photos/blue.png")
                DEFAULT_IMAGE_SIZE = (60, 60)
                piece = pygame.transform.scale(piece, DEFAULT_IMAGE_SIZE)
                screen.blit(piece, (145 + (y * 64), 46 + (x * 64)))
            if Gn.Board_pieces[x][y] == 4:
                piece = pygame.image.load("Photos/black_king.png")
                DEFAULT_IMAGE_SIZE = (60, 60)
                piece = pygame.transform.scale(piece, DEFAULT_IMAGE_SIZE)
                screen.blit(piece, (145 + (y * 64), 46 + (x * 64)))
            if Gn.Board_pieces[x][y] == 5:
                piece = pygame.image.load("Photos/red_king.png")
                DEFAULT_IMAGE_SIZE = (60, 60)
                piece = pygame.transform.scale(piece, DEFAULT_IMAGE_SIZE)
                screen.blit(piece, (145 + (y * 64), 46 + (x * 64)))


def Result_of_Game(winner):
    if winner == 0:
        return
    if winner == 1:
        Board = pygame.image.load("Photos/win.png")
        DEFAULT_IMAGE_SIZE = (600, 600)
        Board = pygame.transform.scale(Board, DEFAULT_IMAGE_SIZE)
        screen.blit(Board, (100, 0))
    else:
        Board = pygame.image.load("Photos/lose.png")
        DEFAULT_IMAGE_SIZE = (600, 600)
        Board = pygame.transform.scale(Board, DEFAULT_IMAGE_SIZE)
        screen.blit(Board, (100, 0))


def menu_show():
    background = pygame.image.load("Photos/menuback.png")
    DEFAULT_IMAGE_SIZE = (800, 600)
    background = pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)
    screen.blit(background, (0, 0))

    play = pygame.image.load("Photos/level1.png")
    DEFAULT_IMAGE_SIZE = (750 - 50 * (Gn.level == 1 and Gn.play_clicked), 550 - 50*(Gn.level == 1 and Gn.play_clicked))
    play = pygame.transform.scale(play, DEFAULT_IMAGE_SIZE)
    screen.blit(play, (25 + 25 * (Gn.level == 1 and Gn.play_clicked), -160 + 25 * (Gn.level == 1 and Gn.play_clicked)))

    play = pygame.image.load("Photos/level2.png")
    DEFAULT_IMAGE_SIZE = (750 - 50 * (Gn.level == 2 and
                                      Gn.play_clicked), 550 - 50 * (Gn.level == 2 and Gn.play_clicked))
    play = pygame.transform.scale(play, DEFAULT_IMAGE_SIZE)
    screen.blit(play, (25 + 25 * (Gn.level == 2 and Gn.play_clicked), -30 + 25 * (Gn.level == 2 and Gn.play_clicked)))

    option = pygame.image.load("Photos/opb.png")
    DEFAULT_IMAGE_SIZE = (750 - 50 * Gn.option_clicked, 550 - 50 * Gn.option_clicked)
    option = pygame.transform.scale(option, DEFAULT_IMAGE_SIZE)
    screen.blit(option, (25 + 25 * Gn.option_clicked, 100 + 25 * Gn.option_clicked))

    Exit = pygame.image.load("Photos/exb.png")
    DEFAULT_IMAGE_SIZE = (750 - 50 * Gn.exit_clicked, 550 - 50 * Gn.exit_clicked)
    Exit = pygame.transform.scale(Exit, DEFAULT_IMAGE_SIZE)
    screen.blit(Exit, (25 + 25 * Gn.exit_clicked, 230 + 25 * Gn.exit_clicked))


def setting_show():

    background = pygame.image.load("Photos/setting.png")
    DEFAULT_IMAGE_SIZE = (800, 600)
    if Gn.Song_Played == 1:
        pygame.draw.circle(background, (0, 255, 0),
                           [1510, 980], 75, 0)
    else:
        pygame.draw.circle(background, (0, 255, 0),
                           [1990, 980], 75, 0)

    pygame.draw.rect(background, (0, 0, 255),
                     [1510, 1530, 80, 200], 0)

    pygame.draw.rect(background, (0, 0, 255),
                     [1450, 1585, 200, 80], 0)

    pygame.draw.rect(background, (0, 0, 255),
                     [1850, 1585, 200, 80], 0)

    start = 1240
    for i in range(Gn.Sound_Level):
        pygame.draw.rect(background, (255, 255, 255),
                         [start, 1409, 90, 20], 0)
        start += 100

    background = pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)

    screen.blit(background, (0, 0))
