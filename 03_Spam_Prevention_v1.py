"""
Purpose: Stops user from being able to spam the buttons,
         removing the accidental question skip problem
Creator: Sammy Cummins
Version: 1
"""

# Imports
from tkinter import *

win = Tk()
win.geometry("660x200")
win.title("Spam Prevention")
count = 0


def prevent():
    global count, time
    count += 1
    label.config(text=f"Total clicks of button are:{count}")
    if count == 1:
        click.config(state=DISABLED)
        time = 0
        count = 0

        def countdown():
            global time
            if time >= 0:
                label.config(text=f"Button will be Enabled in {time+1} seconds")
                time -= 1
                label.after(1000, countdown)
            else:
                global count
                label.config(text=f"Total clicks of button are: 0")
                click.config(state=NORMAL)

        countdown()


label = Label(win, text="Total clicks of button are: 0", font="ariel 25 bold")
label.pack(padx=30, pady=30)
click = Button(win, text="Click Here", font="ariel 25 bold",
               width=10, bg="black", fg="white", command=prevent)
click.pack(padx=30, pady=10)
win.mainloop()
