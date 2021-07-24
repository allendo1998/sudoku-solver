board = [
    [9, 0, 0, 6, 8, 7, 0, 4, 0],
    [0, 2, 0, 0, 0, 3, 0, 6, 0],
    [6, 0, 0, 2, 5, 0, 1, 0, 7],
    [1, 3, 0, 0, 0, 0, 0, 0, 5],
    [5, 0, 0, 0, 0, 2, 7, 3, 0],
    [7, 6, 4, 0, 3, 8, 0, 0, 9],
    [0, 0, 0, 3, 0, 0, 0, 2, 6],
    [0, 5, 6, 0, 0, 1, 4, 7, 3],
    [0, 4, 0, 7, 2, 0, 0, 0, 1],
]

def print_sudoku(board):
    print("-"*37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "   +"*8 + "   |")


def exist_in_col(number,x):
    if number in board[x]:
        return True
    return False

def exist_in_row(number,y):
    for col in range (0, 9):
        if number == board[col][y]:
            return True
    return False

# def exist_in_quaderant(number, x, y):


print_sudoku(board)