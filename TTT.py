#Podle tutorialu https://www.youtube.com/watch?v=nbRpDXV7QDM
from distutils import command
import tkinter as tk

def set_tile(row, column):
    pass

def new_game():
    pass
    
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

color_purple = "#400060"
color_red = "#FF0080"
color_dark_blue = "#00008B"
color_light_blue = "#ADD8E6"

#window
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text=curr_player+"'s turn", font=("Calibri", 20), background=color_purple, foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font=("Calibri", 50, "bold"), background=color_purple, foreground=color_red, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1,column=column)

button = tk.Button(frame, text="restart", font=("Calibri", 20), background=color_dark_blue, foreground="white", command=new_game)
button.grid(row=4, column=0)

frame.pack()

window.mainloop()
