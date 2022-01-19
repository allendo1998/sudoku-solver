import enum
from html import entities
from multiprocessing.sharedctypes import Value
import tkinter as tk


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

# board = [
#     [0, 0, 0, 0, 0, 0, 4, 7, 3],
#     [0, 0, 0, 0, 0, 9, 0, 0, 0],
#     [0, 0, 0, 8, 0, 1, 9, 0, 6],
#     [9, 0, 0, 0, 2, 7, 5, 6, 8],
#     [6, 8, 0, 0, 0, 0, 0, 0, 2],
#     [0, 5, 0, 0, 8, 0, 0, 0, 7],
#     [4, 0, 9, 0, 3, 0, 0, 0, 0],
#     [0, 6, 0, 5, 0, 8, 0, 0, 0],
#     [0, 3, 0, 0, 0, 0, 2, 0, 0],
# ]


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
   

def solve():
    entries_to_board()
    print_sudoku(board)


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