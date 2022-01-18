from multiprocessing.sharedctypes import Value
import tkinter as tk


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
    entries = []
    
    for row in range(grid_dim):
        for col in range(grid_dim):
        
            entry = tk.Entry(root, width=2, highlightthickness=5, highlightbackground='#000000', justify="center")
            if(board[row][col] == 0):
                entry.insert(-1," ")
            else:
                entry.insert(-1,board[row][col])
            pad_y = (0, 0)
            pad_x = (0, 0)
            
            if (row+1) % 3 == 0 and (row+1) < grid_dim: 
                pad_y = (0, 10)
                
            if (col+1) % 3 == 0 and (col+1) < grid_dim: 
                pad_x = (0, 10)

            entry.grid(row=row, column=col, ipadx=10, ipady=10, padx=pad_x, pady=pad_y)
            entries.append(entry)

    return entries
    


root = tk.Tk()
root.title('Sudoku Solver')
entries = grid_layout(root, 9)
root.mainloop()