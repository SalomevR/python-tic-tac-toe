import random

def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')


def player_marker():
    player1 = 'Player 1'
    marker = ['X', 'O']

    player_choice = input(player1 + ", please select your marker (X or O)").upper()

    while player_choice not in marker:
        print("Ooops! Wrong choice, pick 'X' or 'O'")
        player_choice = input(player1 + ", please select your marker (X or O)").upper()

    player1_marker = player_choice

    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    return player1_marker, player2_marker

def choose_first():

    first_play = random.randint(0,1)

    if first_play == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):

    return board[position] == ' '


def player_move(board):
    position = int(input('Choose your next position. (1 - 9)'))

    while position not in range(1, 10) or not space_check(board, position):
        print('Invalid position or space taken. Try again')
        position = int(input('Choose your next position. (1 - 9)'))

    return position

def win_check(board, mark):

    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark))

def tie_check(board):

    return ' ' not in board

def place_marker(board,marker,position):
    board[position] = marker


def replay():
    answer = input('Do you want to play again? Y or N.').upper()
    return answer == 'Y'


print('Welcome to Tic Tac Toe!')
board = ['#'] + [' '] * 9
display_board(board)

while True:

    board = ['#'] + [' '] * 9
    play_game = input('Are you ready to play? Y or N.').upper()

    if play_game == 'Y':
        game_on = True
    else:
        break

    player1_marker, player2_marker = player_marker()
    turn = choose_first()
    print(turn + ' will go first')

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            print('Player 1 turn')
            position = player_move(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Player 1 wins!! Congrats!')
                game_on = False
            elif tie_check(board):
                display_board(board)
                print("It's a tie!")
                game_on = False
            else:
                turn = 'Player 2'

        else:
            display_board(board)
            print('Player 2 turn')
            position = player_move(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Player 2 wins!! Congrats!')
                game_on = False
            elif tie_check(board):
                display_board(board)
                print("It's a tie!")
                game_on = False
            else:
                turn = 'Player 1'

    if not replay():
        break
