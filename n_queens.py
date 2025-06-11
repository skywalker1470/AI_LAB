def is_safe(row , col , board):
    for prev_row in range(row):
        prev_col = board[prev_row]
        if(prev_col == col or abs(row-prev_row) == abs(col - prev_col)):
            return False
    return True
def solve_n_queens(board , row , N):
    
    if(N==row):
        for r in range(len(board)):
            line = ["."] * N
            line[board[r]] = 'Q'
            print(' '.join(line))
        return True
    for col in range(N):
        if(is_safe(row , col , board)):
            board[row] = col
            if(solve_n_queens(board , row + 1 , N )):
                return True
    return False
            
N = 10
board = [-1]* N 
if not solve_n_queens(board , 0 , N):
    print("No solution exists!")