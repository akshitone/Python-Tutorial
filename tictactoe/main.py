board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_running = True
winner = None
current_player = "X"


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_rows():
    global game_running

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_running = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_columns():
    global game_running

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_running = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]


def check_diagonals():
    global game_running

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_running = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]


def check_win():
    global winner
    row_winnder = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winnder:
        winner = row_winnder
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_tie():
    global game_running
    if "-" not in board:
        game_running = False


def check_game_over():
    check_win()
    check_tie()


def display_board():
    i = 0
    while(i <= 6):
        print(board[i], "|", board[i+1], "|", board[i+2])
        i += 3


def handle_turn(current_player):
    print(current_player, "'s turn")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid choice. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("This spot is already taken. Please choose another slot.")

    board[position] = current_player
    display_board()


def play_game():

    display_board()

    while game_running:
        handle_turn(current_player)
        check_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner, "won!")
    else:
        print("Tie!")


play_game()
