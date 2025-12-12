import General_Var as Gn


def Possible_hint(Board, x, y, opx, opy, is_first, Flash_on):
    # first
    Xx = x
    Yy = y
    is_found = 0
    while True:
        if opx == '-':
            Xx = Xx - 1
        else:
            Xx = Xx + 1
        if opy == '-':
            Yy = Yy - 1
        else:
            Yy = Yy + 1
        if Xx < 0 or Yy < 0 or Xx > 7 or Yy > 7:
            break
        if Board[Xx][Yy] == 0:
            if is_first:
                if Flash_on:
                    Board[Xx][Yy] = 3
                is_found = 1
        elif (Board[Xx][Yy] == Board[x][y]) or (Board[Xx][Yy] == Board[x][y] - 3):
            break
        else:
            if opx == '-':
                Xx = Xx - 1
            else:
                Xx = Xx + 1
            if opy == '-':
                Yy = Yy - 1
            else:
                Yy = Yy + 1
            if Xx < 0 or Yy < 0 or Xx > 7 or Yy > 7:
                break
            if Board[Xx][Yy] == 0:
                if Flash_on:
                    Board[Xx][Yy] = 3
                is_found = 1
            break
    return is_found


def Possible_moves(Board, x, y, is_first, Flash_on):
    is_found = 0
    if Board[x][y] == 1:
        if is_first:
            if x + 1 < 8 and y + 1 < 8 and Board[x + 1][y + 1] == 0:
                if Flash_on:
                    Board[x + 1][y + 1] = 3
                is_found = 1
            if x + 1 < 8 and y - 1 >= 0 and Board[x + 1][y - 1] == 0:
                if Flash_on:
                    Board[x + 1][y - 1] = 3
                is_found = 1
        if x + 2 < 8 and y + 2 < 8 and ((Board[x + 1][y + 1] == 2 or Board[x + 1][y + 1] == 5)
                                        and Board[x + 2][y + 2] == 0):
            if Flash_on:
                Board[x + 2][y + 2] = 3
            is_found = 1
        if x + 2 < 8 and y - 2 >= 0 and ((Board[x + 1][y - 1] == 2 or Board[x + 1][y - 1] == 5)
                                         and Board[x + 2][y - 2] == 0):
            if Flash_on:
                Board[x + 2][y - 2] = 3
            is_found = 1

    if Board[x][y] == 2:
        if is_first:
            if x - 1 >= 0 and y + 1 < 8 and Board[x - 1][y + 1] == 0:
                if Flash_on:
                    Board[x - 1][y + 1] = 3
                is_found = 1
            if x - 1 >= 0 and y - 1 >= 0 and Board[x - 1][y - 1] == 0:
                if Flash_on:
                    Board[x - 1][y - 1] = 3
                is_found = 1
        if x - 2 >= 0 and y + 2 < 8 and ((Board[x - 1][y + 1] == 1 or Board[x - 1][y + 1] == 4)
                                         and Board[x - 2][y + 2] == 0):
            if Flash_on:
                Board[x - 2][y + 2] = 3
            is_found = 1
        if x - 2 >= 0 and y - 2 >= 0 and ((Board[x - 1][y - 1] == 1 or Board[x - 1][y - 1] == 4)
                                          and Board[x - 2][y - 2] == 0):
            if Flash_on:
                Board[x - 2][y - 2] = 3
            is_found = 1

    if Board[x][y] == 4 or Board[x][y] == 5:
        is_found = is_found | Possible_hint(Board, x, y, '-', '-', is_first, Flash_on)
        is_found = is_found | Possible_hint(Board, x, y, '-', '+', is_first, Flash_on)
        is_found = is_found | Possible_hint(Board, x, y, '+', '-', is_first, Flash_on)
        is_found = is_found | Possible_hint(Board, x, y, '+', '+', is_first, Flash_on)

    return is_found


def check_win(Board):
    is_found_B = 0
    is_found_R = 0
    for Xx in range(8):
        for Yy in range(8):
            if Board[Xx][Yy] == 1 or Board[Xx][Yy] == 4:
                is_found_B = 1
            elif Board[Xx][Yy] == 2 or Board[Xx][Yy] == 5:
                is_found_R = 1
    is_found = 0
    for Xx in range(8):
        for Yy in range(8):
            if Board[Xx][Yy] == 3:
                is_found = 1
            if Board[Xx][Yy] == Gn.player_turn or Board[Xx][Yy] == Gn.player_turn + 3:
                is_found = is_found | Possible_moves(Board, Xx, Yy, 1, 0)
    if is_found == 0:
        return 3 - Gn.player_turn
    if is_found_B == 0:
        return 2
    if is_found_R == 0:
        return 1
    return 0
