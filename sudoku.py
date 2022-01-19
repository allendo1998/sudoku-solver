from html import entities
from multiprocessing.sharedctypes import Value
import tkinter as tk


# --- Global Variables ---

solution_list = []

entries = []

board = [
    [0, 0, 0, 0, 0, 0, 4, 7, 3],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 8, 0, 1, 9, 0, 6],
    [9, 0, 0, 0, 2, 7, 5, 6, 8],
    [6, 8, 0, 0, 0, 0, 0, 0, 2],
    [0, 5, 0, 0, 8, 0, 0, 0, 7],
    [4, 0, 9, 0, 3, 0, 0, 0, 0],
    [0, 6, 0, 5, 0, 8, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 2, 0, 0],
]




# --- Functions ---

def grid_layout(root, grid_dim):
    
    for row in range(grid_dim):
        for col in range(grid_dim):
        
            entry = tk.Entry(root, width=2, highlightthickness=5, highlightbackground='#000000', justify="center")
            if(board[row][col] != 0):
                entry.insert(-1,board[row][col])
            pad_y = (0, 0)
            pad_x = (0, 0)
            
            if (row+1) % 3 == 0 and (row+1) < grid_dim: 
                pad_y = (0, 10)
                
            if (col+1) % 3 == 0 and (col+1) < grid_dim: 
                pad_x = (0, 10)

            entry.grid(row=row, column=col, ipadx=10, ipady=10, padx=pad_x, pady=pad_y)
            entries.append(entry)

def get_entries():
    return entries

def clear_board():
    for row in range(9):
        for col in range(9):
            board[row][col] = 0
    grid_layout(root,9)


# Put entries onto a board to solve
def board_to_entries(list):
    row = 0
    col = 0
    for value in list:
        board[row][col] = value
        col = col + 1

        if((list.index(value) + 1) % 9 == 0):
            row = row + 1
            col = 0
    return board



# --- Solving Functions ---

def fill_empty(board):   
    for row in range(0,9):
        for col in range(0,9):
            if(len(board[row][col].get()) == 0):
                solution_list.append((row,col))


def exist_in_row(number,row):
    for col in range (0,9):
        if len(board[row][col].get()) != 0 and number == int(board[row][col].get()):
            return True
    return False

def exist_in_col(number,y):
    for col in range (0, 9):
        if len(board[col][y].get()) != 0 and number == int(board[col][y].get()):
            return True
    return False

def exist_in_quaderant(number, x, y, board):
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        for row in range (0,3):
            for col in range (0,3):
                if(len(board[row][col].get()) != 0):
                    if number == int(board[row][col].get()):
                        return True
    elif x >= 3 and x <= 5 and y >= 0 and y <= 2:
        for row in range (0,3):
            for col in range(3,6):
                if(len(board[row][col].get()) != 0):
                    if number == int(board[row][col].get()):
                        return True
    elif x >= 6 and x <= 8 and y >= 0 and y <= 2:
        for row in range (0,3):
            for col in range(6,9):
                if(len(board[row][col].get()) != 0):
                    if number == int(board[row][col].get()):
                        return True
    elif x >= 0 and x <= 2 and y >= 3 and y <= 5:
        for row in range (3,6):
            for col in range(0,3):
                if(len(board[row][col].get()) != 0):
                    if number == int(board[row][col].get()):
                        return True
    elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
        for row in range (3,6):
            for col in range(3,6):
                if(len(board[row][col].get()) != 0):
                    if number == int(board[row][col].get()):
                        return True
    elif x >= 6 and x <= 8 and y >= 3 and y <= 5:
        for row in range (3,6):
            for col in range(6,9):
                if(len(board[row][col].get()) != 0):
                    if number == int(board[row][col].get()):
                        return True
    elif x >= 0 and x <= 2 and y >= 6 and y <= 8:
        for row in range (6,9):
            for col in range(0,3):
                if(len(board[row][col].get()) != 0):
                    if number == int(board[row][col].get()):
                        return True
    elif x >= 3 and x <= 5 and y >= 6 and y <= 8:
        for row in range (6,9):
            for col in range(3,6):
                if(len(board[row][col].get()) != 0):
                    if number == int(board[row][col].get()):
                        return True
    elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
        for row in range (6,9):
            for col in range(6,9):
                if(len(board[row][col].get()) != 0):
                    if number == int(board[row][col].get()):
                        return True
    return False

def backtrack(index, board):
    current_number = int(board[solution_list[index][0]][solution_list[index][1]].get())
    board[solution_list[index][0]][solution_list[index][1]].delete(0, "end")

    if current_number == 9:
        return backtrack(index - 1, board)

    for number in range(current_number + 1, 10):
        if exist_in_row(number, solution_list[index][0]) == False and exist_in_col(number, solution_list[index][1]) == False and exist_in_quaderant(number, solution_list[index][1], solution_list[index][0], board) == False:
            board[solution_list[index][0]][solution_list[index][1]].delete(0, "end")
            board[solution_list[index][0]][solution_list[index][1]].insert(-1, number)
            return index + 1 
    
        if number == 9:
            return backtrack(index - 1, board)

def solve():
    index = 0
    board_to_entries(entries)
    fill_empty(board)
    
    while True:
        for number in range(1,10):
            if exist_in_row(number, solution_list[index][0]) == False and exist_in_col(number, solution_list[index][1]) == False and exist_in_quaderant(number, solution_list[index][1], solution_list[index][0], board) == False:
                board[solution_list[index][0]][solution_list[index][1]].insert(-1,number) 
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

# Solve Board
s = tk.Button(root, text = "Solve", comman = solve)
s.grid(row = 0, column = 16)

# Clear Board
C = tk.Button(root, text = "Clear", comman = clear_board)
C.grid(row = 3, column = 16)

root.mainloop()