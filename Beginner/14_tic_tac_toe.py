import random 

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    

def check_win():
    pass

def check_draw():
    pass


if __name__ == "__main__":
    display_board(board)