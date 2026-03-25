import tkinter as tk

playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

color_purple = "#800080"
color_red = "#FF0000"
color_dark_blue = "#00008B"
color_light_blue = "#ADD8E6"

#window
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label()

window.mainloop()
