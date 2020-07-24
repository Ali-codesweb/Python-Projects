game_going = True
board = ["-","-", "-",
         "-","-", "-",
         "-","-","-"]
winner = None
current_player = "X"

def play_game():
    while game_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + " won")
    elif winner == None:
        print(" Its a tie")
    display_board()


def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def handle_turn(current_rplaye):
        print(current_player + "'s turn: ")
        valid = False
        position = input("Chose a position from one to nine")

        while not valid:

            while position not in ["1","2","3","4","5","6","7","8","9"]:
                position = input("Chose a position from one to nine7")

            position = int(position) -1

            if board[position] == "-":
                valid = True
            else:
                print("YOu cant go there")
        board[position] = current_rplaye
        display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def checkrows():
    global game_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3 :
        game_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def checkcols():
    global game_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None


def checkdiag():
    global game_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        game_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    else:
        return None

def check_if_win():
# check rows
    global winner
    row_winner = checkrows()
    col_wimmer = checkcols()
    diagonal_winner = checkdiag()
# check columns
# check diagonals
    if row_winner:
        winner = row_winner
        #row winner
    elif col_wimmer:
        winner = col_wimmer
        #col winner
    elif diagonal_winner:
        winner = diagonal_winner
        #diagonal win
    else:
        #no win
        winner = None

def check_if_tie():
    global game_going
    if "-" not in board:
        game_going = False

    return

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"



play_game()
#Game logic
    #board
    #display board
    #play game
    #is_win

    #is_tie
    #flip player
