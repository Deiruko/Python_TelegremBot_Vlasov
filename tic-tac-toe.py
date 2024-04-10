def draw_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        print("---------")


def ask_move(player, board):
    x, y = input(f"{player}, введите координаты X и Y  (e.g. 0 0): ").strip().split()
    x, y = int(x), int(y)
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        return (x,y)
    else:
        print("Клетка занята. Введите другие координаты.")
        return ask_move(player, board)


def make_move(player, board, x, y):
    if board[x][y] != " ":
        print("Клетка занята")
        return False
    board[x][y] = player
    return True


def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    make_move(player, board, x, y)


def check_win(player, board):
    for i in range(3):
        if board[i] == [player, player, player]:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    while True:
        board = [[" " for i in range(3)] for j in range(3)]
        player = "x"
        while True:
            draw_board(board)
            ask_and_make_move(player, board)
            if check_win(player, board):
                print(f"{player} Победил!")
            tie_game = False
            for row in board:
                for cell in row:
                    if cell == " ":
                        tie_game = True
            if not tie_game:
                break
            player = "O" if player == "X" else "X"
        restart = input("Начать заново? (y/n")
        if restart.lower()!= "y":
            break

tic_tac_toe()