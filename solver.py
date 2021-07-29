import os
import time

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
    # print("current number",current_number)
    # print("current position", solution_list[index])
    # print_sudoku(board)   
    # index_sol = index

    if current_number == 9:
        # print("no solution we need to back track")
        return backtrack(index - 1, board)

    for number in range(current_number + 1, 10):
        # print(solution_list[index],",",number)
        if exist_in_row(number, solution_list[index][0]) == False and exist_in_col(number, solution_list[index][1]) == False and exist_in_quaderant(number, solution_list[index][1], solution_list[index][0], board) == False:
            board[solution_list[index][0]][solution_list[index][1]] = number
            # print("found solution return to next index",solution_list[index + 1])
            # print_sudoku(board)  
            return index + 1 
            # index_sol = index + 1
            break
        
        if number == 9:
            # print("no solution we need to back track")
            return backtrack(index - 1, board)
    # print("next index",solution_list[index + 1])
    # return index_sol



def solve_sudoku(board):
    debug = 0
    index = 0

    while True:
        # print("actual index", solution_list[index])
        for number in range(1,10):
            # print(solution_list[index],",",number)
            if exist_in_row(number, solution_list[index][0]) == False and exist_in_col(number, solution_list[index][1]) == False and exist_in_quaderant(number, solution_list[index][1], solution_list[index][0], board) == False:
                board[solution_list[index][0]][solution_list[index][1]] = number
                os.system('clear')
                print_sudoku(board)   
                index += 1 
                break
            if number == 9:
                # print("no solution we need to back track")
                index = backtrack(index - 1, board)
                # print(index)

            
            # time.sleep(0.1) # to slow down the printing so we can see it moving

        # print('input:')
        # x = input()

        # if x == 'd':
        #     debug += 1
        # elif x == 'a':
        #     debug -= 1

        # to break the while loop for debugging
        # debug += 1
        # if debug == 11:
        #     break
        if index == len(solution_list):
            break



fill_empty(board)

solve_sudoku(board)