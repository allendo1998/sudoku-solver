import tkinter as tk


def drawGrid(width, height):
    box_size = width * height
    print("Drawing Grid" + box_size)





root = tk.Tk()
root.title("Sudoku Solver")
canvas = tk.Canvas(root, width=700, height=700, bg="#263D42")
canvas.pack()
root.mainloop()