import enum
from html import entities
from multiprocessing.sharedctypes import Value
import tkinter as tk
import os
import time

# --- Global Variables ---

solution_list = []

entries = []

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# --- Functions ---

def grid_layout(root, grid_dim):
    
    for row in range(grid_dim):
        for col in range(grid_dim):
        
            entry = tk.Entry(root, width=2, highlightthickness=5, highlightbackground='#000000', justify="center")

            pad_y = (0, 0)
            pad_x = (0, 0)
            
            if (row+1) % 3 == 0 and (row+1) < grid_dim: 
                pad_y = (0, 10)
                
            if (col+1) % 3 == 0 and (col+1) < grid_dim: 
                pad_x = (0, 10)

            entry.grid(row=row, column=col, ipadx=10, ipady=10, padx=pad_x, pady=pad_y)
            entries.append(entry)

def clear_board():
    index = 0
    for row in range(9):
        for col in range(9):
            board[row][col] = 0
            entries[index].delete(0, "end")
            index += 1
    solution_list.clear()
    


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


def insert_board_to_grid():
    index = 0
    for row in range(9):
        for col in range(9):
            entries[index].delete(0, "end")
            if(board[row][col] != 0):
                entries[index].insert(-1,board[row][col])
            index += 1

def entries_to_board():
    row = 0
    col = 0
    for index,x in enumerate(entries):
        if(len(x.get()) != 0):    
            board[row][col] = int(x.get())
        else:
            board[row][col] = 0
        col += 1

        if((index + 1) % 9 == 0):
            row += 1
            col = 0
   


# --- Solve Functions ---
def fill_empty(board):   
    for row in range(0,9):
        for col in range(0,9):
            if board[row][col] == 0:
                solution_list.append((row,col))


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

def solve():
    entries_to_board()
    fill_empty(board)
    index = 0
    
    while True:
        for number in range(1,10):
            if exist_in_row(number, solution_list[index][0]) == False and exist_in_col(number, solution_list[index][1]) == False and exist_in_quaderant(number, solution_list[index][1], solution_list[index][0], board) == False:
                board[solution_list[index][0]][solution_list[index][1]] = number
                insert_board_to_grid()
                print_sudoku(board)
                index += 1 
                break
            if number == 9:
                index = backtrack(index - 1, board)

        if index == len(solution_list):
            break
  
# --- Main ---
root = tk.Tk()
root.title('Sudoku Solver')
grid_layout(root, 9)
insert_board_to_grid()

# Solve Board
S = tk.Button(root, text = "Solve", comman = solve)
S.grid(row = 0, column = 16)

# Clear Board
C = tk.Button(root, text = "Clear", comman = clear_board)
C.grid(row = 3, column = 16)

root.mainloop()