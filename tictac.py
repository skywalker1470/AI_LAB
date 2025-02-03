def check_my_board(num1,num2,board,player):
    #checking row
    sign = 'i'
    if(player=='A'):
        sign = 'X'
    else:
        sign = 'O'
    row_f  = False
    for i in range(3) :
        if(board[num1][(num2+i)%3] != sign):
            break
        if(i==2):
            row_f = True
    #checking column
    column = False
    for i in range(3):
        if(board[(num1+i)%3][num2] != sign):
            break
        if(i==2):
            column = True
    #checking diagnols \
        diagnol1 = False
    if(num1==num2):
        for i in range(3):
            if(board[(num1+i)%3][(num2+i)%3] != sign ):
                break
            if(i==2):
                diagnol1 = True
    #checking diagnol / 
    diagnol2 = False           
    if(num1+num2 == 2):
        for i in range(3):
            column_no = num2-i
            if(column_no<0):
                column_no = 2
            if(board[(num1+i)%3][column_no] != sign):
                break
            if(i==2):
                diagnol2 = True
            
    ans = row_f or column or diagnol1 or diagnol2 
    return ans
    
            
print("TicTacToe \n")
board = (['-','-','-'],['-','-','-'],['-','-','-'])
player = 'A'
count = 0
game_status = False 
while not game_status :
    print(f"Player {player}'s turn :")
    num1 = int(input("Enter row : "))
    num2 = int(input("Enter Column : "))
    if(player == 'A') : 
        board[num1][num2] = 'X'
    else : 
        board[num1][num2] = 'O'
    game_status = check_my_board(num1 , num2 , board , player)
    count += 1
    if(game_status):
        print(f"Player {player} Won !!")
        break
    if(count == 9):
        print("None of you dipshits won !!")
        break
    #swapping players
    if(player == 'A') : 
        player = 'B'
    else : 
        player = 'A'