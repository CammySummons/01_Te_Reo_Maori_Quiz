"""
Purpose: Allows user to type their guess and submit to go to the next question
Creator: Sammy Cummins
Trial: 2
"""

# Imports
from tkinter import *

# Set up the interface
win = Tk()
win.title("Te Reo Maori Quiz")
win.geometry('1000x600+280+100')
win.resizable(False, False)
try:
    win.iconbitmap(
        "C:\\Users\sammy\OneDrive - Middleton Grange School\DTC\Year 13"
        " 2022\AS3.7 91906 Programming\Assessment\Documents\logo.ico")
except TclError:
    pass
frame = Frame(win, bg="dark green")  # Grid in which objects/widgets are held

# Variable Declaration
btn_disabled = False  # Buttons do nothing if btn_disabled = True
num = 0  # Question number
current_question = StringVar()
current_question.set(f"{num}/10")


# Changing to next question
def option_selected():
    global num, btn_disabled
    inp = input_lbl.get(1.0, "end-1c")
    if inp == "" and not btn_disabled:
        print("can't be blank")
    else:
        if not btn_disabled:
            num += 1
            current_question.set(f"{num}/10")
            input_lbl.delete("1.0", "end")
            if num == 10:
                btn_disabled = True


# Declaring widgets
cur_que_border = Label(frame, bg="black")
current_question_box = Label(frame, textvariable=current_question,
                             font=("Comic Sans MS", 9, "bold"), bg="green",
                             fg="black")
submit_btn = Button(frame, bg="light green", command=option_selected,
                    text="Submit", font=("Comic Sans MS", 14, "bold"))
input_lbl = Text(frame, font=("Comic Sans MS", 34, "bold"))

# Placing widgets
cur_que_border.place(x=17.25, y=17, width=55.5, height=35.5)
current_question_box.place(x=20, y=20, width=50, height=30)
submit_btn.place(x=410, y=400, width=150, height=50)
input_lbl.place(x=290, y=300, width=400, height=70)

frame.pack(fill=BOTH, expand=YES)
win.mainloop()
