# JS, 1st, Tic Tac Toe Pseudo Code
import random
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
reference = " 0 | 1 | 2 \n---|---|---\n 3 | 4 | 5 \n---|---|---\n 6 | 7 | 8 "
def win(turn, board):
    out = "None"
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == turn:
            out = f"{turn}'s won!"
    return out
print(f" {board[0]} | {board[1]} | {board[2]} \n---|---|---\n {board[3]} | {board[4]} | {board[5]} \n---|---|---\n {board[6]} | {board[7]} | {board[8]}\n")
while True:
    #------PLAYER TURN------
    inp = int(input(f"{reference}\n Where would you like to place your X?\n "))
    while board[inp] != "-" or inp > 8 or inp < 0:
        inp = int(input("That was not a valid input, where would you like to place your X?\n "))
    board[inp] = "X"
    print(f" {board[0]} | {board[1]} | {board[2]} \n---|---|---\n {board[3]} | {board[4]} | {board[5]} \n---|---|---\n {board[6]} | {board[7]} | {board[8]}\n")
    #------CHECK BOARD------
    #  ---WIN?---
    message = win("X", board)
    if message != "None":
        break
    #  ---TIE?---
    spaces = 0
    for place in board:
        if place == "-":
            spaces += 1
    if spaces == 0:
        message = "You Tied."
        break
    #------COMPUTER TURN------
    inp = random.randint(0,8)
    while board[inp] != "-":
        inp = random.randint(0,8)
    board[inp] = "O"
    print(f" {board[0]} | {board[1]} | {board[2]} \n---|---|---\n {board[3]} | {board[4]} | {board[5]} \n---|---|---\n {board[6]} | {board[7]} | {board[8]}\n")
    #------CHECK BOARD------
    #  ---WIN?---
    message = win("O", board)
    if message != "None":
        break
print(message)