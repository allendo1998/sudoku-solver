import os
import time

start = 0

board = [
    [0, 0, 0, 2, 0, 0, 0, 1, 3],
    [0, 0, 2, 0, 5, 9, 6, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 7, 0],
    [7, 0, 0, 0, 8, 0, 1, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 8, 0, 4, 5],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 3, 0, 0, 2, 0, 0, 0],
]

solution_list = []

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

def fill_empty(board):   
    for row in range(0,9):
        for col in range(0,9):
            if board[row][col] == 0:
                solution_list.append((row,col))

def backtrack(index, board):
    current_number = board[solution_list[index][0]][solution_list[index][1]]
    board[solution_list[index][0]][solution_list[index][1]] = 0

    if current_number == 9:
        return backtrack(index - 1, board)

    for number in range(current_number + 1, 10):
        if exist_in_row(number, solution_list[index][0]) == False and exist_in_col(number, solution_list[index][1]) == False and exist_in_quaderant(number, solution_list[index][1], solution_list[index][0], board) == False:
            board[solution_list[index][0]][solution_list[index][1]] = number
            return index + 1 
    
        if number == 9:
            return backtrack(index - 1, board)

def solve_sudoku(board):
    index = 0
    start = time.time()
    while True:
        for number in range(1,10):
            if exist_in_row(number, solution_list[index][0]) == False and exist_in_col(number, solution_list[index][1]) == False and exist_in_quaderant(number, solution_list[index][1], solution_list[index][0], board) == False:
                board[solution_list[index][0]][solution_list[index][1]] = number
                os.system('clear')
                print_sudoku(board)
                end = time.time()
                print("[Time Elapsed : %3.2f]" % (end - start))
                index += 1 
                break
            if number == 9:
                index = backtrack(index - 1, board)

        if index == len(solution_list):
            break

fill_empty(board)
solve_sudoku(board)