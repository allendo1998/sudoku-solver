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


def exist_in_row(number,row):
    if number in board[row]:
        return True
    return False

def exist_in_col(number,y):
    for col in range (0, 9):
        if number == board[col][y]:
            return True
    return False

def exist_in_quaderant(number, x, y, board):
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        for row in range (0,3):
            for col in range (0,3):
                if number == board[row][col]:
                    return True
    elif x >= 3 and x <= 5 and y >= 0 and y <= 2:
        for row in range (0,3):
            for col in range(3,6):
                if number == board[row][col]:
                    return True
    elif x >= 6 and x <= 8 and y >= 0 and y <= 2:
        for row in range (0,3):
            for col in range(6,9):
                if number == board[row][col]:
                    return True
    elif x >= 0 and x <= 2 and y >= 3 and y <= 5:
        for row in range (3,6):
            for col in range(0,3):
                if number == board[row][col]:
                    return True
    elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
        for row in range (3,6):
            for col in range(3,6):
                if number == board[row][col]:
                    return True
    elif x >= 6 and x <= 8 and y >= 3 and y <= 5:
        for row in range (3,6):
            for col in range(6,9):
                if number == board[row][col]:
                    return True
    elif x >= 0 and x <= 2 and y >= 6 and y <= 8:
        for row in range (6,9):
            for col in range(0,3):
                if number == board[row][col]:
                    return True
    elif x >= 3 and x <= 5 and y >= 6 and y <= 8:
        for row in range (6,9):
            for col in range(3,6):
                if number == board[row][col]:
                    return True
    elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
        for row in range (6,9):
            for col in range(6,9):
                if number == board[row][col]:
                    return True
    return False
    

print_sudoku(board)