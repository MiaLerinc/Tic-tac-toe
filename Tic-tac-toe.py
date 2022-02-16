def display_board(board):
    print('\n'*100)
    print(board[7] + 'l' + board[8] + 'l' + board[9])
    print(board[4] + 'l' + board[5] + 'l' + board[6])
    print(board[1] + 'l' + board[2] + 'l' + board[3])

def player_input():
    choice='wrong'
    while choice not in ['X','O']:
        choice=input('Player 1 chose X or O: ')
    player1=choice
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)

def input_on_board(game_board,player1_sign,player2_sign):
    p=0
    for i in range (9):
        while p not in range(1,10) or game_board[p]!='   ':
            if (i%2==0):
                p=int(input('PLAYER 1: Pick a position (1-9): '))
            else:
                p=int(input('PLAYER 2: Pick a position (1-9): '))
        if i%2==0:
                game_board[p]=player1_sign
        else:
                game_board[p]=player2_sign
        display_board(game_board)
        d=win_function(game_board,player1_sign,player2_sign)
        if d=='win':
            break
        
def win_function(game_board,player1_sign,player2_sign):
    for i in range(1,9,3):
        if game_board[i]==game_board[i+1]==game_board[i+2]==player1_sign:
            print('Player 1 has won the game!')
            return 'win'
        if game_board[i]==game_board[i+1]==game_board[i+2]==player2_sign:
            print('Player 2 has won the game!')
            return 'win'
        else:
            pass
    for i in range(1,4,1):
        if game_board[i]==game_board[i+3]==game_board[i+6]==player1_sign:
            print('Player 1 has won the game!')
            return 'win'
        if game_board[i]==game_board[i+3]==game_board[i+6]==player2_sign:
            print('Player 2 has won the game!')
            return 'win'
        else:
            pass
    if game_board[1]==game_board[5]==game_board[9]==player1_sign:
        print('Player 1 has won the game!')
        return 'win'
    if game_board[1]==game_board[5]==game_board[9]==player2_sign:
        print('Player 2 has won the game!')
        return 'win'
    if game_board[3]==game_board[5]==game_board[7]==player1_sign:
        print('Player 1 has won the game!')
        return 'win'
    if game_board[3]==game_board[5]==game_board[7]==player2_sign:
        print('Player 2 has won the game!')
        return 'win'
    else:
        pass

def gameon_choice():
    choice='wrong'
    while choice not in ['YES','NO']:
        choice=input('Do yu want to play again? (YES or NO) ')
        if choice not in ['YES','NO']:
            print("Sorry, I don't understand, please choose YES or NO")
        if choice == 'YES':
            return True
        else:
            return False


game_on=True


while game_on==True:
    game_board=['r']+['   ']*9
    display_board(game_board)
    player1_sign,player2_sign=player_input()
    game_board=input_on_board(game_board,player1_sign,player2_sign)
    game_on=gameon_choice()


            
