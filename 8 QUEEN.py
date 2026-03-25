N = 8
board = [-1]*N

def safe(r,c):
    for i in range(r):
        if board[i]==c or abs(board[i]-c)==abs(i-r):
            return False
    return True

def solve(r):
    if r==N:
        print(board)
        return
    for c in range(N):
        if safe(r,c):
            board[r]=c
            solve(r+1)

solve(0)
