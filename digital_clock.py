#Tkinter -  For making the Glaphical User Interface of the clock.
import tkinter as tk

#Time module for importing time function into the app/program.
from time import strftime

#Root window - in which we display the main elements of the program into the tkinter.
root=tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text =string)
    label.after(1000,time)

label = tk.Label(root, font=('calibri',50,'bold'), background='yellow', foreground='black')
#pack method is used to arrange the elements into the window
label.pack(anchor='center')

time()
#main loop method is used to take the user input
root.mainloop()


