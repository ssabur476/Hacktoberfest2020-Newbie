#Start of Code

#--------Global Variables (variables that are defined outside the function)-----------

# Game board
board = [ "-", "-", "-",
          "-", "-", "-",
          "-", "-", "-",]

# If game is still going
game_still_going = True

#Who won?
winner = None 

playerinput1 = 'X'

playerinput2 = 'O'

#Who is playing?
current_player = "X"


def display_board():
  print("1│2│3",'                ' ,board[0] + " │ " + board[1] + " │ " + board[2])
  print("4│5│6",'                ' ,board[3] + " │ " + board[4] + " │ " + board[5])
  print("7│8│9",'                ' ,board[6] + " │ " + board[7] + " │ " + board[8])
  

   
        
def play_game():

    # Display initial board
    display_board()
    
    checkwin()
   
    # Creating a loop so the game continues until a final outcome has been reached
    while game_still_going:



        handle_turn(current_player) #Handle current turn

        check_if_game_is_over() #checking if the game is over

        flip_player() #flip the player if the game is not over


def check_if_game_is_over():  #the crietiras for the game to end, is either if the game ends in a win or a game  
    checkwin()


def checkwin():
  
    
    def checkrow():
               #For X
            if board[0] == board[1] == board[2] and (board[0] ==  playerinput1):
                rownumber = board[0]
                win = True
                print(rownumber + ' has won')
            if board[3] == board[4] == board[5] and (board[3] == playerinput1):
                win = True
                rownumber = board[3]
                print(rownumber + ' has won')
            if board[6] == board[7] == board[8] and (board[7] == playerinput1):
                win = True
                rownumber = board[6]
                print(rownumber + ' has won')
                 #For O
            if board[0] == board[1] == board[2] and (board[0] ==  playerinput2):
                rownumber = board[0]
                win = True
                print(rownumber + ' has won')
            if board[3] == board[4] == board[5] and (board[3] == playerinput2):
                win = True
                rownumber = board[3]
                print(rownumber + ' has won')
            if board[6] == board[7] == board[8] and (board[7] == playerinput2):
                win = True
                rownumber = board[6]
                print(rownumber + ' has won')

    return checkrow()

    def checkcolumn(columnnumber):
        if board[0] == board[3] == board[6] and (board[0] == playerinput1):
            columnnumber = board[0]
            win = True
            print(columnnumber  + ' has won')
        if board[1] == board[4] == board[7] and (board[1] == playerinput1):
            win = True
            columnnumber = board[3]
            print(columnnumber + ' has won')
        if board[2] == board[5] == board[8] and (board[2] == playerinput1):
            win = True
            columnnumber = board[2]
            print(columnnumber + 'has won')
        if board[0] == board[3] == board[6] and (board[0] == playerinput2):
            columnnumber = board[0]
            win = True
            print(columnnumber  + ' has won')
        if board[1] == board[4] == board[7] and (board[1] == playerinput2):
            win = True
            columnnumber = board[3]
            print(columnnumber + ' has won')
        if board[2] == board[5] == board[8] and (board[2] == playerinput2):
            win = True
            columnnumber = board[2]
            print(columnnumber + ' has won')


    return checkcolumn()

    def checkdiagonal(diagonalnumber):
        if board[0] == board[4] == board[8] and (board[0] == playerinput1):
            diagonalnumber = board[0]
            win = True
            print(diagonalnumber + ' has won')
        if board[2] == board[4] == board[6] and (board[2] == playerinput1):
            diagonalnumber = board[2]
            win = True
            print(diagonalnumber + ' has won')
        if board[0] == board[4] == board[8] and (board[0] == playerinput2):
            diagonalnumber = board[0]
            win = True
            print(diagonalnumber + ' has won')
        if board[2] == board[4] == board[6] and (board[2] == playerinput2):
            diagonalnumber = board[2]
            win = True
            print(diagonalnumber + ' has won')

        return checkdiagonal()

    return checkwin()
# step6



def flip_player():  #This is to flip the player from "X" to "O"
    # global variable needed
    global current_player
    # if the current player is X, then the next player is O
    if current_player == "X":
      current_player = "O"
    # if the current player is O, then the next player is X
    elif current_player == "O":
        current_player = "X"


# Handle a turn for an arbitrary player
def handle_turn(player):

  # Get position from player
  print(current_player + "'s turn.")
  position_on_board = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position_on_board not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position_on_board = input("Please choose a number from 1-9 only: ")
 
    # Get correct index in our board list
    position_on_board = int(position_on_board) - 1

    # Then also make sure the spot is available on the board
    if board[position_on_board] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position_on_board] = current_player

  # Show the game board
  display_board()



play_game()
