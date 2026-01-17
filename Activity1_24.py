#Implementation of two player Tic Tac Toe game

'''We will make the board using dictionary in which keys will be the location(i.e: top-left,mid-right,etc.)
   and initially it's values will be empty space and then after every move 
   we will change the value according to the player's choice of move. '''

theBoard={'7': ' ' ,'8': ' ' , '9': ' ',
         '4': ' ' ,'5': ' ','6': ' ' ,
         '1': ' ' ,'2': ' ' ,'3': ' '}

board_keys=[]

for key in theBoard:
    board_keys.append(key)

'''We will have to print the updated board after every move in the game and
   thus we will make a function in whick we'll define the printBoard function
   so that we can easily print the board everytime by calling this function.'''

def printBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])
    print('-+-+-')

#Now we'll write the main function which has all the gameplay functionaloty.
def game():

    turn='x'
    count=0
    