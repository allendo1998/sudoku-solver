from multiprocessing.sharedctypes import Value
import tkinter as tk

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

def get_new_board(list):
    row = 0
    col = 0
    for value in list:
        board[row][col] = value
        col = col + 1

        if((list.index(value) + 1) % 9 == 0):
            row = row + 1
            col = 0
    return board
        

root = tk.Tk()
root.title('Sudoku Solver')
grid_layout(root, 9)

# Clear Board
C = tk.Button(root, text = "Clear", comman = clear_board)
C.grid(row = 3, column = 16)

root.mainloop()