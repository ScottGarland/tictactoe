#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~#
#          Version 1.1          #
# TicTacToe.py by Scott Garland #
#  Can be played in a terminal  #
# Credit given to Jose Portilla #
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~#

import random

#Constructing initial game values for the guideline map
game_values = ['empty','1','2','3','4','5','6','7','8','9']

#Determines which player goes first
def who_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#Function that displays the current values on the board. Index values correspond to numpad on keyboard
def board(game_values):
    print("      #     #      ")
    print("   "+game_values[7]+"  #  "+game_values[8]+"  #  "+game_values[9]+"   ")
    print("      #     #      ")
    print(" ################# ")
    print("      #     #      ")
    print("   "+game_values[4]+"  #  "+game_values[5]+"  #  "+game_values[6]+"   ")
    print("      #     #      ")
    print(" ################# ")
    print("      #     #      ")
    print("   "+game_values[1]+"  #  "+game_values[2]+"  #  "+game_values[3]+"   ")
    print("      #     #      \n")

#Have players choose between 'X' and 'O' and print the result. Returns (player1,player2) tuple markers
def choose():
    begin = False
    while begin == False:
        player_input = input("Would you like to be X's or O's? Player 1, please input 'X' or 'O' to decide: ")
        if player_input.upper() == 'X':
            player = ('X','O')
            begin = True
        elif player_input.upper() == 'O':
            player = ('O','X')
            begin = True
        else:
            begin = False
    print("\nPlayer 1 is {}".format(player[0]))
    print("Player 2 is {}\n".format(player[1]))
    return player

#Function that sets the player's input marker on the board with the corresponding index position
def placement(game_values, player_input, index):
    game_values[index] = player_input
    
#Returns boolean and checks the board to see if there's a winner or a draw
def check_win(game_values, marker):
    return (game_values[1] == game_values[2] == game_values[3] == marker or #bottom row
    game_values[4] == game_values[5] == game_values[6] == marker or #middle row
    game_values[7] == game_values[8] == game_values[9] == marker or #top row
    game_values[1] == game_values[4] == game_values[7] == marker or #left column
    game_values[2] == game_values[5] == game_values[8] == marker or #middle column
    game_values[3] == game_values[6] == game_values[9] == marker or #right column
    game_values[7] == game_values[5] == game_values[3] == marker or #top left to bottom right diagonal
    game_values[9] == game_values[5] == game_values[1] == marker) #top right to bottom left diagonal

#Checks the spaces on the game board to see if they are playable/empty
def empty_check(game_values, index):
    return game_values[index] == ' '

#Check is board is full
def full_board(game_values):
    for i in range(1,10):
        if empty_check(game_values, i):
            return False
    return True

#Takes player input and converts it to a game_value index for the game board
def board_placement(game_values):
    placement = 0 #inital placement is off the printed game board
    inputs = [1,2,3,4,5,6,7,8,9]
    while placement not in inputs or not empty_check(game_values, placement):
        placement = int(input('Please choose your placement: 1-9 '))
    return placement
    
#Give players the option to replay
def replay():
    return input('Would you like to play again? Y/N ').upper().startswith('Y')

############################################# GAME LOGIC #############################################
print("\n~*~*~ Let's Play Tic-Tac-Toe! ~*~*~\nPlease use this number guideline to make your move.\n")
#Prints display board and guide numbers for user input on start up
board(game_values)
def game():
    game_values = [' ']*10
    player1,player2 = choose()
    turn = who_first()
    print(turn + " will make the first move!\n")
    win = False
    while win == False:
        if turn == 'Player 1':
            board(game_values)
            index = board_placement(game_values)
            placement(game_values,player1,index)
            if check_win(game_values,player1):
                board(game_values)
                print("Player 1 wins!!")
                if replay():
                    game()
                else:
                    quit()
            else:
                if full_board(game_values):
                    board(game_values)
                    print("Game ends in a draw!")
                    if replay():
                        game()
                    else:
                        quit()
                else: turn = 'Player 2'
        else:
            board(game_values)
            index = board_placement(game_values)
            placement(game_values,player2,index)
            if check_win(game_values,player2):
                board(game_values)
                print("Player 2 wins!!")
                if replay():
                    game()
                else:
                    quit()
            else:
                if full_board(game_values):
                    board(game_values)
                    print("Game ends in a draw!")
                    if replay():
                        game()
                    else:
                        quit()
                else: turn = 'Player 1'
game()