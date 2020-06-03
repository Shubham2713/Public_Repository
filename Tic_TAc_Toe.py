import random
from IPython.display import clear_output

#display the board everytime

def print_board(board):
    
        clear_output()
        print(board[7]+"|"+board[8]+"|"+board[9])
        print("_____")
        print(board[4]+"|"+board[5]+"|"+board[6])
        print("_____")
        print(board[1]+"|"+board[2]+"|"+board[3])

#to take which player has which moves sign

def player_input():
    marker=" "
    while marker!="X" and marker!="O":
        marker=input("Player 1: Enter the choice (X or O)").upper() 
        if marker not in ["X","O"]:
            continue
        if marker=="X":
            return ("X","O")
        else:
            return ("O","X")

#to place marker in board

def place_marker(board,marker,position):
    board[position]=marker

# to check whwther a player won

def win_check(board,mark):
        return ((board[1]==mark and board[2]==mark and board[3]==mark) or
        (board[4]==mark and board[5]==mark and board[6]==mark) or
        (board[7]==mark and board[8]==mark and board[9]==mark) or
        (board[1]==mark and board[4]==mark and board[7]==mark) or
        (board[2]==mark and board[5]==mark and board[8]==mark) or
        (board[3]==mark and board[6]==mark and board[9]==mark) or
        (board[7]==mark and board[5]==mark and board[3]==mark) or
        (board[9]==mark and board[5]==mark and board[1]==mark))


#chooses the player who go first

def choose_first():
    flip=random.randint(1,2)
    if(flip==1):
        return "Player 1"
    else:
        return "Player 2"

#check whether a position is empty

def space_check(board,position):
    return board[position]==" "

#check whether a board is full

def full_check(board):
    c=9
    for i in range(1,10):
        if space_check(board,i)==False:
            c=c-1
    if(c==0):
        
        return True
    else:
        
        return False
            

#takes input of position

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Enter a position: (1-9)"))
        
    return position

#to replay a game

def replay():
    res=""
    while res not in ["Y","N"]:
         res=input("Play again ? Enter[Y/N] ").upper()

    return res=="Y"

### MAIN Part

print ("WELCOME to Tic Tac Toe X/O!!!")


while True:
    
    board=[" "]*10
    player1_marker, player2_marker=player_input()
    turn=choose_first()
    print(turn +" will go first")
    
    play_game=input("Ready for a game ?? [Y/N]").upper()
    
    if play_game=="Y":
        game_on=True
    else:
        game_on=False
        
    while game_on:
        
        if turn=="Player 1":
            
            print_board(board)
            
            position=player_choice(board)
            
            place_marker(board,player1_marker,position)
            
            if win_check(board,player1_marker):
                print_board(board)
                print("Player 1 Won!!!")
                game_on=False
            else:
                if full_check(board):
                    print_board(board)
                    print("A Tie !!!")
                    game_on=False
                else:
                    turn="Player 2"
                    
                
                
            
            
            
            
        else:
            print_board(board)
            
            position=player_choice(board)
            
            place_marker(board,player2_marker,position)
            
            if win_check(board,player2_marker):
                print_board(board)
                print("Player 2 Won!!!")
                game_on=False
            else:
                if full_check(board):
                    print_board(board)
                    print("A Tie !!!")
                    game_on=False
                else:
                    turn="Player 1"
          
    
    if not replay():
        break
