board = [' ']*9

def show():
    print(board[0:3],"\n",board[3:6],"\n",board[6:9])

def win(p):
    wins = [(0,1,2),(3,4,5),(6,7,8)]
    return any(board[i]==board[j]==board[k]==p for i,j,k in wins)

for i in range(9):
    show()
    move = int(input("Enter pos 0-8: "))
    board[move] = 'X' if i%2==0 else 'O'
    if win(board[move]):
        show()
        print("Winner:", board[move])
        break
