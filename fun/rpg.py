#JS, 1st, rpg, FOR FUN
game_running = "yes"
player_position = [1,1]
def print_board(new_column, new_row):
    column = ""
    while new_column > 0:
        column = column + "X"
        new_column -= 1
    while new_row > 0:
        print(column)
        new_row -= 1
while game_running == "yes":
    new_column = int(input("How many per row?\n"))
    new_row = int(input("How many rows?\n"))
    print_board(new_column, new_row)
    game_running = input("Would you like to play again?\n")