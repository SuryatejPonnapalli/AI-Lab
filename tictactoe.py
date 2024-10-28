import math

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

X = 'X'
O = 'O'

def is_full(board):
    return all(cell != '' for row in board for cell in row)

def winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def minimax(board, depth, is_max, alpha, beta):
    if winner(board, X):
        return 1
    elif winner(board, O):
        return -1
    elif is_full(board):
        return 0

    if is_max:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = X
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = O
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board, player):
    best_val = -math.inf if player == X else math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = player
                move_val = minimax(board, 0, player == O, -math.inf, math.inf)
                board[i][j] = ''

                if player == X:
                    if move_val > best_val:
                        best_val = move_val
                        move = (i, j)
                else:
                    if move_val < best_val:
                        best_val = move_val
                        move = (i, j)

    return move

def display(board):
    for row in board:
        print(row)
    print()

def play():
    current = X
    while True:
        display(board)
        if current == X:
            move = best_move(board, X)
            if move:
                board[move[0]][move[1]] = X
        else:
            row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
            if board[row][col] == '':
                board[row][col] = O
            else:
                print("Invalid move, try again.")
                continue

        if winner(board, current):
            display(board)
            print(f"{current} wins!")
            break
        elif is_full(board):
            display(board)
            print("It's a draw!")
            break

        current = O if current == X else X

play()