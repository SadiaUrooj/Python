#Tkinter for the GUI
import tkinter as tk

#importing the message box for showing the message windows to the user
from tkinter import messagebox

# 1. defining a check click button that will going to check wather a player won or not
# 2. Make a list that has 8 different combinations for a player to won
def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac_Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

# For when the user click somewhere, it will make a sign/Symbol for the current user
def button_click(index):
    if buttons[index]["text"]== "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

#The toggle function is responsible for changing the current player
# For this we use a global keyword that will help us to change the current player
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root=tk.Tk()
root.title("Tic-Tac-Toe")

# 1. For command parameter ww will pass a lambda function
#       A lambda function is an anynomus function that is written in one line
#       lambda function will call the button_click funcation and return it's index
# 2. Will save these buttons into a list named as button
# 3. For making this list, will use a list comprehension (it's a python trick used to make a list in one line)

buttons =[tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
# arranging the buttons into a 3x3 grid using grid method
# row and column will be calculated using the button's index
# Use the enumerate function that will return button with it's index

for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3)

current_player = 'X'
winner= False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

#main loop method is used to manage the user input and show the window on screen
root.mainloop()