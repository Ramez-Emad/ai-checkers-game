from General_Var import init_game
from Draw_shapes import *
from MinimaxAglo import *
from Play_Functions import Possible_moves


def Game_Screen():
    for event in pygame.event.get():
        Winner = check_win(Gn.Board_pieces)
        mx, my = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # coordinate of Sound Icon
            if 25 <= mx <= 85 <= my <= 144:
                Gn.IS_sound_play = not Gn.IS_sound_play
            # -----------------------------

            # coordinate of Back Icon  -> go to menu
            if 25 <= mx <= 85 and 10 <= my <= 67:
                Gn.choose_screen = 0
            # ------------------------------

            # coordinate of Back Icon  -> go to menu
            if 25 <= mx <= 85 and 160 <= my <= 220:
                if len(Gn.Stack) > 2:
                    Gn.Stack.pop()
                    Gn.Board_pieces = Gn.Stack[-1]
                    Gn.player_turn = 2
                else:
                    Gn.Board_pieces=[
                            [1, 0, 1, 0, 1, 0, 1, 0],  # 0   empty cell
                            [0, 1, 0, 1, 0, 1, 0, 1],  # 1   black cell
                            [1, 0, 1, 0, 1, 0, 1, 0],  # 2   red cell
                            [0, 0, 0, 0, 0, 0, 0, 0],  # 3   possible cell
                            [0, 0, 0, 0, 0, 0, 0, 0],  # 4   Black (king) cell
                            [0, 2, 0, 2, 0, 2, 0, 2],  # 5   red (king) cell
                            [2, 0, 2, 0, 2, 0, 2, 0],
                            [0, 2, 0, 2, 0, 2, 0, 2]]
                    Gn.player_turn = 1

            # ------------------------------

        if Winner == 0:
            # ------ Computer Turn ------
            if Gn.player_turn == 2:

                # Minimax to determine best move
                print('---------------------------------------------------------')
                Max_eval, Best_move = minimax_2(Gn.Board_pieces, 4, -math.inf, math.inf, True,
                                                Gn.pre_is_killed, Gn.pre_killed_x, Gn.pre_killed_y, Gn.level)
                print("Max : ", Max_eval)
                # To avoid access none
                # When checker kill enemy checker it will have another chance to search for
                # a valid move But it may be no available move
                if Best_move:
                    Gn.Board_pieces = Best_move[0]  # index 0 = The Board after move
                    if Best_move[1]:  # index 1 = Pre_is_killed ( Flag )
                        Gn.Counter_black = Gn.Counter_black - 1
                    Gn.pre_is_killed = Best_move[1]
                    Gn.pre_killed_x = Best_move[2]  # index 2 = new x of red checker after killed
                    Gn.pre_killed_y = Best_move[3]  # index 3 = new y of red checker after killed
                else:
                    Gn.pre_is_killed = 0

                if Gn.pre_is_killed == 0:
                    Gn.player_turn = 1
                    Gn.Counter_for_timer = Gn.Counter_for_timer + 180
            # ------ End ------

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Convert from screen coordinate to index of board
                #  (145 , 46) = (0,0)
                temp_mx = mx
                mx = (my - 46) // 64
                my = (temp_mx - 145) // 64
                # -------------------------------

                # this condition to avoid out of range when access Board
                if 0 <= mx <= 7 and 0 <= my <= 7:

                    # 3 means its possible cell than I can move to
                    # and click on it = do action and play
                    if Gn.Board_pieces[mx][my] == 3:
                        # "IS_sound_play" is a variable control move sound
                        if Gn.IS_sound_play:
                            Gn.click.play()
                        # -----------------------------

                        # "pre_is_killed" is a flag to know is I have chance to kill another checker (piece)
                        if Gn.pre_is_killed:
                            # assign new coordinate of black checker after last kill crime to avoid any random click
                            Gn.pre_mx = Gn.pre_killed_x
                            Gn.pre_my = Gn.pre_killed_y
                        # --------------------------------------------

                        # pre_mx , pre_my -> Coordinate of original checker
                        # mx , my -> Coordinate of Goal cell

                        # This condition to know if I will Kill an enemy Checker or not
                        if abs(mx - Gn.pre_mx) != 1:

                            # To determine coordinate of enemy checker which will be killed
                            deleted_X = (mx + 1) if (mx < Gn.pre_mx) else (mx - 1)
                            deleted_Y = (my + 1) if (my < Gn.pre_my) else (my - 1)
                            # ---------------------

                            # Counter_ red is a variable contain number of red checkers
                            if Gn.Board_pieces[deleted_X][deleted_Y] != 3:
                                Gn.pre_is_killed = 1

                            # 0 in board means empty cell
                            # That equal deletes enemy ( Red ) checker
                            Gn.Board_pieces[deleted_X][deleted_Y] = 0

                            # save coordinate of killed red checker
                            Gn.pre_killed_x = mx
                            Gn.pre_killed_y = my

                        # when mx = 7 that mean Black checker reach to border ( Be a king )

                        if mx == 7:
                            Gn.Board_pieces[mx][my] = 4
                        else:
                            Gn.Board_pieces[mx][my] = Gn.Board_pieces[Gn.pre_mx][Gn.pre_my]

                        # Delete original checker because it will move to new coordinates
                        Gn.Board_pieces[Gn.pre_mx][Gn.pre_my] = 0
                        # -----------------------------------------------------

                        # to remove remain Possible Coordinates that checkers can move to
                        for xx in range(8):
                            for yy in range(8):
                                if Gn.Board_pieces[xx][yy] == 3:
                                    Gn.Board_pieces[xx][yy] = 0
                        # --------------------------------------

                        # if Black checker killed Red Checker we test if there are another
                        # chance to kill another Red checker
                        if Gn.pre_is_killed:
                            # Possible_moves return 1 if there are any possible move
                            Is_found = Possible_moves(Gn.Board_pieces, mx, my, False, 1)
                            Gn.pre_is_killed = Gn.pre_is_killed & Is_found
                        # -------------------------------------

                        if Gn.pre_is_killed == 0:
                            Gn.Stack.append(Gn.Board_pieces)
                            Gn.player_turn = 2
                            Gn.Counter_for_timer = Gn.Counter_for_timer + 180

                    elif Gn.pre_is_killed == 0:

                        # to remove old Possible Coordinates that checkers can move to
                        for xx in range(8):
                            for yy in range(8):
                                if Gn.Board_pieces[xx][yy] == 3:
                                    Gn.Board_pieces[xx][yy] = 0

                        # to ensure that is my turn
                        if Gn.Board_pieces[mx][my] == 1 or Gn.Board_pieces[mx][my] == 4:
                            # Flash possible moves by blue
                            Possible_moves(Gn.Board_pieces, mx, my, True, True)

                    # save last checker I clicked up
                    Gn.pre_mx = mx
                    Gn.pre_my = my
                else:
                    for xx in range(8):
                        for yy in range(8):
                            if Gn.Board_pieces[xx][yy] == 3:
                                Gn.Board_pieces[xx][yy] = 0

        back_ground()
        board()
        piece_location()
        cancel()
        sound(Gn.IS_sound_play)
        timer(Gn.Counter_for_timer)
        Result_of_Game(Winner)
        pygame.display.update()
