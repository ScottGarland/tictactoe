#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~#
#          Version 1.0          #
# TicTacToe.py by Scott Garland #
#  Can be played in a terminal  #
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~#

#######################
# Declaring variables #
#######################

board = ["      #     #      ",
         "   7  #  8  #  9   ",
         "      #     #      ",
         " ################# ",
         "      #     #      ",
         "   4  #  5  #  6   ",
         "      #     #      ",
         " ################# ",
         "      #     #      ",
         "   1  #  2  #  3   ",
         "      #     #      "]

str0 = "      #     #      "
str1 = "      #     #      "
str2 = "      #     #      "
str3 = " ################# "
str4 = "      #     #      "
str5 = "      #     #      "
str6 = "      #     #      "
str7 = " ################# "
str8 = "      #     #      "
str9 = "      #     #      "
strT = "      #     #      "

updated_board = [str0, str1, str2, str3, str4, str5, str6, str7, str8, str9, strT]

player1 = 'X'
player2 = 'O'
game_values = [None, None, None,
               None, None, None,
               None, None, None]
######################################################
# Function that prints game's instructions and rules #
######################################################

def instructions():
    instruct = False
    while instruct == False:
        question = input("Would you like to read the instructions and guide? Y/N\n")
        if question.upper() == 'YES' or question.upper() == 'Y':
            print("\nTaking turns, Player 1 and Player 2 will place their X or O on the board. Get 3 placements in line either horizontally, vertically, or diagonally to win.")
            print("The numbers on the board correspond to the player's placement options.")
            print("Use the numpad on the keyboard as a guideline.\n")
            for line in board:
                print(line)
            instruct = True
        elif question.upper() == 'NO' or question.upper() == 'N':
            instruct = True
        else:
            instruct = False

####################################################################
# Function for Player 1 and Player 2 to choose between X's and O's #
####################################################################

def start():
    print("\n~*~Begin Game~*~\n")
    begin = False
    while begin == False:
        global player1
        global player2
        player1 = input("Would you like to be X's or O's? Player 1, please input 'X' or 'O' to decide: \n")
        if player1.upper() == 'X':
            player1 = 'X'
            player2 = 'O'
            begin = True
        elif player1.upper() == 'O':
            player1 = 'O'
            player2 = 'X'
            begin = True
        else:
            begin = False
    print("\nPlayer 1 is {}".format(player1))
    print("Player 2 is {}\n".format(player2))

    for line in updated_board:
        print(line)

########################################################
# Function that updates the current board for Player 1 #
########################################################

def update_player1():
    global updated_board
    global str9
    global str5
    global str1
    global game_values

    play = False

    while play == False:
        placement = input("\nPlayer 1, please input your number placement.\n")

        if placement == '1':
            list9 = list(str9)
            if list9[3] == player1 or list9[3] == player2:
                play = False
            else:
                list9[3] = player1
                game_values[6] = player1
                str9 = ''.join(list9)
                updated_board.pop(9)
                updated_board.insert(9,str9)
                play = True

        elif placement == '2':
            list9 = list(str9)
            if list9[9] == player1 or list9[9] == player2:
                play = False
            else:
                list9[9] = player1
                game_values[7] = player1
                str9 = ''.join(list9)
                updated_board.pop(9)
                updated_board.insert(9,str9)
                play = True

        elif placement == '3':
            list9 = list(str9)
            if list9[15] == player1 or list9[15] == player2:
                play = False
            else:
                list9[15] = player1
                game_values[8] = player1
                str9 = ''.join(list9)
                updated_board.pop(9)
                updated_board.insert(9,str9)
                play = True

        elif placement == '4':
            list5 = list(str5)
            if list5[3] == player1 or list5[3] == player2:
                play = False
            else:
                list5[3] = player1
                game_values[3] = player1
                str5 = ''.join(list5)
                updated_board.pop(5)
                updated_board.insert(5,str5)
                play = True

        elif placement == '5':
            list5 = list(str5)
            if list5[9] == player1 or list5[9] == player2:
                play = False
            else:
                list5[9] = player1
                game_values[4] = player1
                str5 = ''.join(list5)
                updated_board.pop(5)
                updated_board.insert(5,str5)
                play = True
        
        elif placement == '6':
            list5 = list(str5)
            if list5[15] == player1 or list5[15] == player2:
                play = False
            else:
                list5[15] = player1
                game_values[5] = player1
                str5 = ''.join(list5)
                updated_board.pop(5)
                updated_board.insert(5,str5)
                play = True

        elif placement == '7':
            list1 = list(str1)
            if list1[3] == player1 or list1[3] == player2:
                play = False
            else:
                list1[3] = player1
                game_values[0] = player1
                str1 = ''.join(list1)
                updated_board.pop(1)
                updated_board.insert(1,str1)
                play = True

        elif placement == '8':
            list1 = list(str1)
            if list1[9] == player1 or list1[9] == player2:
                play = False
            else:
                list1[9] = player1
                game_values[1] = player1
                str1 = ''.join(list1)
                updated_board.pop(1)
                updated_board.insert(1,str1)
                play = True

        elif placement == '9':
            list1 = list(str1)
            if list1[15] == player1 or list1[15] == player2:
                play = False
            else:
                list1[15] = player1
                game_values[2] = player1
                str1 = ''.join(list1)
                updated_board.pop(1)
                updated_board.insert(1,str1)
                play = True
        
        else:
            play = False

    for line in updated_board:
        print(line)

########################################################
# Function that updates the current board for Player 2 #
########################################################

def update_player2():
    global updated_board
    global str9
    global str5
    global str1
    global game_values

    play = False

    while play == False:
        placement = input("\nPlayer 2, please input your number placement.\n")

        if placement == '1':
            list9 = list(str9)
            if list9[3] == player1 or list9[3] == player2:
                play = False
            else:
                list9[3] = player2
                game_values[6] = player2
                str9 = ''.join(list9)
                updated_board.pop(9)
                updated_board.insert(9,str9)
                play = True

        elif placement == '2':
            list9 = list(str9)
            if list9[9] == player1 or list9[9] == player2:
                play = False
            else:
                list9[9] = player2
                game_values[7] = player2
                str9 = ''.join(list9)
                updated_board.pop(9)
                updated_board.insert(9,str9)
                play = True

        elif placement == '3':
            list9 = list(str9)
            if list9[15] == player1 or list9[15] == player2:
                play = False
            else:
                list9[15] = player2
                game_values[8] = player2
                str9 = ''.join(list9)
                updated_board.pop(9)
                updated_board.insert(9,str9)
                play = True

        elif placement == '4':
            list5 = list(str5)
            if list5[3] == player1 or list5[3] == player2:
                play = False
            else:
                list5[3] = player2
                game_values[3] = player2
                str5 = ''.join(list5)
                updated_board.pop(5)
                updated_board.insert(5,str5)
                play = True

        elif placement == '5':
            list5 = list(str5)
            if list5[9] == player1 or list5[9] == player2:
                play = False
            else:
                list5[9] = player2
                game_values[4] = player2
                str5 = ''.join(list5)
                updated_board.pop(5)
                updated_board.insert(5,str5)
                play = True
        
        elif placement == '6':
            list5 = list(str5)
            if list5[15] == player1 or list5[15] == player2:
                play = False
            else:
                list5[15] = player2
                game_values[5] = player2
                str5 = ''.join(list5)
                updated_board.pop(5)
                updated_board.insert(5,str5)
                play = True

        elif placement == '7':
            list1 = list(str1)
            if list1[3] == player1 or list1[3] == player2:
                play = False
            else:
                list1[3] = player2
                game_values[0] = player2
                str1 = ''.join(list1)
                updated_board.pop(1)
                updated_board.insert(1,str1)
                play = True

        elif placement == '8':
            list1 = list(str1)
            if list1[9] == player1 or list1[9] == player2:
                play = False
            else:
                list1[9] = player2
                game_values[1] = player2
                str1 = ''.join(list1)
                updated_board.pop(1)
                updated_board.insert(1,str1)
                play = True

        elif placement == '9':
            list1 = list(str1)
            if list1[15] == player1 or list1[15] == player2:
                play = False
            else:
                list1[15] = player2
                game_values[2] = player2
                str1 = ''.join(list1)
                updated_board.pop(1)
                updated_board.insert(1,str1)
                play = True
        
        else:
            play = False

    for line in updated_board:
        print(line)

#############################################
# Function that checks if there is a winner #
#############################################

def check_win():
    return game_values[0] == game_values[1] == game_values[2] == player1 or game_values[0] == game_values[1] == game_values[2] == player2 or \
    game_values[3] == game_values[4] == game_values[5] == player1 or game_values[3] == game_values[4] == game_values[5] == player2 or \
    game_values[6] == game_values[7] == game_values[8] == player1 or game_values[6] == game_values[7] == game_values[8] == player2 or \
    game_values[0] == game_values[3] == game_values[6] == player1 or game_values[0] == game_values[3] == game_values[6] == player2 or \
    game_values[1] == game_values[4] == game_values[7] == player1 or game_values[1] == game_values[4] == game_values[7] == player2 or \
    game_values[2] == game_values[5] == game_values[8] == player1 or game_values[2] == game_values[5] == game_values[8] == player2 or \
    game_values[0] == game_values[4] == game_values[8] == player1 or game_values[0] == game_values[4] == game_values[8] == player2 or \
    game_values[2] == game_values[4] == game_values[6] == player1 or game_values[2] == game_values[4] == game_values[6] == player2

##########################################################
# Function that asks if players would like to play again #
##########################################################

def replay():
    global str9
    global str5
    global str1
    global updated_board
    global game_values
    replay = input("Would you like to play again? Y/N\n")
    if replay.upper() == 'YES' or replay.upper() == 'Y':
        str1 = "      #     #      "
        str5 = "      #     #      "
        str9 = "      #     #      "
        updated_board = [str0, str1, str2, str3, str4, str5, str6, str7, str8, str9, strT]
        game_values = [None, None, None,
                       None, None, None,
                       None, None, None]
        start()
        game()
    else:
        quit()

###############################################################
# Function that executes the update functions until game over #
###############################################################

def game():
    current_move = 1
    win = False
    while current_move <= 9:
        update_player1()
        win = check_win()
        if win == True:
            print("We have a winner!\n")
            replay()
        elif current_move == 9 and win == False:
            print("Match ends in a draw!\n")
            replay()
        else:
            current_move += 1
            update_player2()
            win = check_win()
            if win == True:
                print("We have a winner!\n")
                replay()
            else:
                current_move += 1

# Ask if the players would like to see the instructions #
instructions()

# Start the game #
start()

# Execute the game with the update_player functions #
game()