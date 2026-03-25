# Tic Tac Toe (Moderate)

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def show():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def win(p):
    if (board[0]==board[1]==board[2]==p or
        board[3]==board[4]==board[5]==p or
        board[6]==board[7]==board[8]==p or
        board[0]==board[3]==board[6]==p or
        board[1]==board[4]==board[7]==p or
        board[2]==board[5]==board[8]==p or
        board[0]==board[4]==board[8]==p or
        board[2]==board[4]==board[6]==p):
        return True
    return False


player = "X"

for i in range(9):

    show()

    pos = int(input("Enter position 0-8: "))

    if board[pos] == " ":
        board[pos] = player
    else:
        print("Wrong move")
        continue

    if win(player):
        show()
        print(player, "Wins")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
