import copy
import math

from Play_Functions import check_win


def calculate_heuristics_1(board):
    mine = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 2 or board[i][j] == 5:
                mine += 1
    return mine


def calculate_heuristics_2(board):
    mine = 0
    king_mine = 0
    opp = 0
    king_opp = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 2:
                if 0 < i < 7 and 0 < j < 7:
                    if (board[i + 1][j + 1] == 0 and ( board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == 4)) or \
                            (board[i + 1][j - 1] == 0 and (board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == 4)):
                        opp += 1
                mine += 2
            elif board[i][j] == 5:
                if 0 < i < 7 and 0 < j < 7:
                    if (board[i + 1][j + 1] == 0 and (board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == 4)) or \
                            (board[i + 1][j - 1] == 0 and (board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == 4)):
                        opp += 1
                king_mine += 2.5
            elif board[i][j] == 4:
                king_opp += 4
            elif board[i][j] == 1:
                opp += 4
    return -opp + mine - (king_opp * 0.5 - king_mine * 0.5)


def minimax_2(Board, depth, alpha, beta, max_player, pre_is_killed, pre_x, pre_y, level):
    if check_win(Board) == 1:
        return -math.inf, Board

    elif check_win(Board) == 2:
        return math.inf, Board

    elif depth == 0:
        if level == 1:
            return calculate_heuristics_1(Board), Board
        else:
            return calculate_heuristics_2(Board), Board

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in Possible_moves_Minimax(Board, 2, not pre_is_killed, pre_x, pre_y):
            Can = 0
            if move[1]:
                Can = Possible_moves_Minimax(move[0], 2, 0, move[2], move[3])
                if Can:
                    Can = 1
            evaluation = minimax_2(move[0], depth - 1, alpha, beta, Can, Can, move[2], move[3], level)
            maxEval = max(maxEval, evaluation[0])
            if maxEval <= evaluation[0]:
                best_move = move
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in Possible_moves_Minimax(Board, 1, 1, pre_x, pre_y):
            minEval = float('inf')
            Can = 0
            if move[1]:
                Can = Possible_moves_Minimax(move[0], 1, 0, move[2], move[3])
                if Can:
                    Can = 1
            evaluation = minimax_2(move[0], depth - 1, alpha, beta, not Can, Can, move[2], move[3], level)
            minEval = min(minEval, evaluation[0])
            if minEval == evaluation[0]:
                best_move = move
            beta = min(beta, evaluation[0])
            if beta <= alpha:
                break
        return minEval, best_move


def Possible_hint_Minimax(Board, x, y, opx, opy, is_first, moves):
    Xx = x
    Yy = y
    current_state = copy.deepcopy(Board)
    current_state[x][y] = 0
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
                current_state[Xx][Yy] = Board[x][y]
                moves.append((copy.deepcopy(current_state), 0, 0, 0))
                current_state[Xx][Yy] = 0
        elif (Board[Xx][Yy] == Board[x][y]) or (Board[Xx][Yy] == Board[x][y] - 3):
            break
        else:
            current_state[Xx][Yy] = 0
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
                current_state[Xx][Yy] = Board[x][y]
                moves.append((copy.deepcopy(current_state), 1, Xx, Yy))
                current_state[Xx][Yy] = 0
                if opx == '-':
                    Xx = Xx + 1
                else:
                    Xx = Xx - 1
                if opy == '-':
                    Yy = Yy + 1
                else:
                    Yy = Yy - 1
                current_state[Xx][Yy] = Board[Xx][Yy]
            break


def Possible_moves_Minimax(Board, player, Is_first, pre_x, pre_y):
    moves = []
    current_state = copy.deepcopy(Board)
    if Is_first:
        for x in range(8):
            for y in range(8):
                if Board[x][y] == 1 and player == 1:
                    current_state[x][y] = 0
                    if x + 1 < 8 and y + 1 < 8 and Board[x + 1][y + 1] == 0:
                        current_state[x + 1][y + 1] = 1
                        if x + 1 == 7:
                            current_state[x + 1][y + 1] = 4
                        moves.append((copy.deepcopy(current_state), 0, 0, 0))
                        current_state[x + 1][y + 1] = 0
                    if x + 1 < 8 and y - 1 >= 0 and Board[x + 1][y - 1] == 0:
                        current_state[x + 1][y - 1] = 1
                        if x + 1 == 7:
                            current_state[x + 1][y - 1] = 4
                        moves.append((copy.deepcopy(current_state), 0, 0, 0))
                        current_state[x + 1][y - 1] = 0
                    if x + 2 < 8 and y + 2 < 8 and (
                            (Board[x + 1][y + 1] == 2 or Board[x + 1][y + 1] == 5) and Board[x + 2][y + 2] == 0):
                        current_state[x + 2][y + 2] = 1
                        if x + 2 == 7:
                            current_state[x + 2][y + 2] = 4
                        current_state[x + 1][y + 1] = 0
                        moves.append((copy.deepcopy(current_state), 1, x + 2, y + 2))
                        current_state[x + 2][y + 2] = 0
                        current_state[x + 1][y + 1] = Board[x + 1][y + 1]
                    if x + 2 < 8 and y - 2 >= 0 and (
                            (Board[x + 1][y - 1] == 2 or Board[x + 1][y - 1] == 5) and Board[x + 2][y - 2] == 0):
                        current_state[x + 2][y - 2] = 1
                        if x + 2 == 7:
                            current_state[x + 2][y - 2] = 4
                        current_state[x + 1][y - 1] = 0
                        moves.append((copy.deepcopy(current_state), 1, x + 2, y - 2))
                        current_state[x + 2][y - 2] = 0
                        current_state[x + 1][y - 1] = Board[x + 1][y - 1]
                if Board[x][y] == 2 and player == 2:
                    current_state[x][y] = 0
                    if x - 1 >= 0 and y + 1 < 8 and Board[x - 1][y + 1] == 0:
                        current_state[x - 1][y + 1] = 2
                        if x - 1 == 0:
                            current_state[x - 1][y + 1] = 5
                        moves.append((copy.deepcopy(current_state), 0, 0, 0))
                        current_state[x - 1][y + 1] = 0
                    if x - 1 >= 0 and y - 1 >= 0 and Board[x - 1][y - 1] == 0:
                        current_state[x - 1][y - 1] = 2
                        if x - 1 == 0:
                            current_state[x - 1][y - 1] = 5
                        moves.append((copy.deepcopy(current_state), 0, 0, 0))
                        current_state[x - 1][y - 1] = 0

                    if x - 2 >= 0 and y + 2 < 8 and (
                            (Board[x - 1][y + 1] == 1 or Board[x - 1][y + 1] == 4) and Board[x - 2][y + 2] == 0):
                        current_state[x - 2][y + 2] = 2
                        if x - 2 == 0:
                            current_state[x - 2][y + 2] = 5
                        current_state[x - 1][y + 1] = 0
                        moves.append((copy.deepcopy(current_state), 1, x - 2, y + 2))

                        current_state[x - 2][y + 2] = 0
                        current_state[x - 1][y + 1] = Board[x - 1][y + 1]
                    if x - 2 >= 0 and y - 2 >= 0 and (
                            (Board[x - 1][y - 1] == 1 or Board[x - 1][y - 1] == 4) and Board[x - 2][y - 2] == 0):
                        current_state[x - 2][y - 2] = 2
                        if x - 2 == 0:
                            current_state[x - 2][y - 2] = 5
                        current_state[x - 1][y - 1] = 0
                        moves.append((copy.deepcopy(current_state), 1, x - 2, y - 2))
                        current_state[x - 2][y - 2] = 0
                        current_state[x - 1][y - 1] = Board[x - 1][y - 1]

                if (Board[x][y] == 4 and player == 1) or (Board[x][y] == 5 and player == 2):
                    Possible_hint_Minimax(Board, x, y, '-', '-', Is_first, moves)
                    Possible_hint_Minimax(Board, x, y, '-', '+', Is_first, moves)
                    Possible_hint_Minimax(Board, x, y, '+', '-', Is_first, moves)
                    Possible_hint_Minimax(Board, x, y, '+', '+', Is_first, moves)
                current_state[x][y] = Board[x][y]
    else:
        current_state[pre_x][pre_y] = 0
        if (Board[pre_x][pre_y] == 4 and player == 1) or (Board[pre_x][pre_y] == 5 and player == 2):
            Possible_hint_Minimax(Board, pre_x, pre_y, '-', '-', Is_first, moves)
            Possible_hint_Minimax(Board, pre_x, pre_y, '-', '+', Is_first, moves)
            Possible_hint_Minimax(Board, pre_x, pre_y, '+', '-', Is_first, moves)
            Possible_hint_Minimax(Board, pre_x, pre_y, '+', '+', Is_first, moves)

        if Board[pre_x][pre_y] == 1 and player == 1:

            if pre_x + 2 < 8 and pre_y + 2 < 8 and (
                    (Board[pre_x + 1][pre_y + 1] == 2 or Board[pre_x + 1][pre_y + 1] == 5) and
                    Board[pre_x + 2][pre_y + 2] == 0):
                current_state[pre_x + 2][pre_y + 2] = 1
                if pre_x + 2 == 7:
                    current_state[pre_x + 2][pre_y + 2] = 4
                current_state[pre_x + 1][pre_y + 1] = 0
                moves.append((copy.deepcopy(current_state), 1, pre_x + 2, pre_y + 2))
                current_state[pre_x + 2][pre_y + 2] = 0
                current_state[pre_x + 1][pre_y + 1] = Board[pre_x + 1][pre_y + 1]
            if pre_x + 2 < 8 and pre_y - 2 >= 0 and (
                    (Board[pre_x + 1][pre_y - 1] == 2 or Board[pre_x + 1][pre_y - 1] == 5) and
                    Board[pre_x + 2][pre_y - 2] == 0):
                current_state[pre_x + 2][pre_y - 2] = 1
                if pre_x + 2 == 7:
                    current_state[pre_x + 2][pre_y - 2] = 4
                current_state[pre_x + 1][pre_y - 1] = 0
                moves.append((copy.deepcopy(current_state), 1, pre_x + 2, pre_y - 2))
                current_state[pre_x + 2][pre_y - 2] = 0
                current_state[pre_x + 1][pre_y - 1] = Board[pre_x + 1][pre_y - 1]

        if Board[pre_x][pre_y] == 2 and player == 2:

            if pre_x - 2 >= 0 and pre_y + 2 < 8 and (
                    Board[pre_x - 1][pre_y + 1] == 1 or Board[pre_x - 1][pre_y + 1] == 4) \
                    and Board[pre_x - 2][pre_y + 2] == 0:

                current_state[pre_x - 2][pre_y + 2] = 2
                if pre_x - 2 == 0:
                    current_state[pre_x - 2][pre_y + 2] = 5

                current_state[pre_x - 1][pre_y + 1] = 0
                moves.append((copy.deepcopy(current_state), 1, pre_x - 2, pre_y + 2))

                current_state[pre_x - 2][pre_y + 2] = 0
                current_state[pre_x - 1][pre_y + 1] = Board[pre_x + 1][pre_y + 1]

            if pre_x - 2 >= 0 and pre_y - 2 >= 0 and \
                    ((Board[pre_x - 1][pre_y - 1] == 1 or Board[pre_x - 1][pre_y - 1] == 4)
                     and Board[pre_x - 2][pre_y - 2] == 0):
                current_state[pre_x - 2][pre_y - 2] = 2
                if pre_x - 2 == 0:
                    current_state[pre_x - 2][pre_y - 2] = 5
                current_state[pre_x - 1][pre_y - 1] = 0
                moves.append((copy.deepcopy(current_state), 1, pre_x - 2, pre_y - 2))

                current_state[pre_x - 2][pre_y - 2] = 0
                current_state[pre_x - 1][pre_y - 1] = Board[pre_x - 1][pre_y - 1]
    return moves
