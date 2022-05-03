# Imports
from tkinter import *

# Set up the interface
win = Tk()
win.title("Te Reo Maori Quiz")
win.geometry('1000x600+280+100')
win.resizable(False, False)
win.iconbitmap("C:\\Users\sammy\OneDrive - Middleton Grange School\DTC\Year 13"
               " 2022\AS3.7 91906 Programming\Assessment\Documents\logo.ico")
frame = Frame(win, bg="dark green")  # Grid in which objects/widgets are held

# Variable Declaration
output_box_txt = StringVar()
btn_disabled = False  # Buttons do nothing if btn_disabled = True
num = 0
current_question = StringVar()
current_question.set(f"{num}/10")


def option_selected():
    global num
    if not btn_disabled:
        if num < 10:
            num += 1
            current_question.set(f"{num}/10")


def opt_btn_framework():
    return Button(frame, bg="light green", command=option_selected, text="Variable", font=("Comic Sans MS", 14, "bold"))


# Declaring widgets
output_box = Label(frame, textvariable=output_box_txt,
                   font=("Comic Sans MS", 13), bg="white", fg="black")
cur_que_border = Label(frame, bg="black")
current_question_box = Label(frame, textvariable=current_question, font=("Comic Sans MS", 9, "bold"), bg="green", fg="black")
option1 = opt_btn_framework()
option2 = opt_btn_framework()
option3 = opt_btn_framework()
option4 = opt_btn_framework()

# Placing widgets
output_box.place(x=150, y=100, width=725, height=80)
cur_que_border.place(x=17.25, y=17, width=55.5, height=35.5)
current_question_box.place(x=20, y=20, width=50, height=30)
option1.place(x=150, y=250, width=320, height=80)
option2.place(x=555, y=250, width=320, height=80)
option3.place(x=150, y=400, width=320, height=80)
option4.place(x=555, y=400, width=320, height=80)


# Welcome screen
output_box_txt.set("Welcome to the Te Reo Maori Quiz! "
                   "Press any of the buttons below to begin the quiz.")


frame.pack(fill=BOTH, expand=YES)
win.mainloop()
