"""
Purpose: Allows buttons to be clicked and identified on click.
         Also changes to next button values on click.
Creator: Sammy Cummins
Version: 1
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
opt1_text = StringVar()
opt2_text = StringVar()
opt3_text = StringVar()
opt4_text = StringVar()
btn_disabled = False  # Buttons do nothing if btn_disabled = True
num = 0  # Question number
current_question = StringVar()
current_question.set(f"{num}/10")


# Recognises the button clicked and changes the text on button
# (effectively changing to next question)
def option_selected(what_btn):
    global num, btn_disabled
    if not btn_disabled:
        if num < 11:
            num += 1
            print(what_btn)

            if num == 11:
                btn_disabled = True

            if num <= 10:
                current_question.set(f"{num}/10")
            else:
                qst_11 = Question(11, "", "", "", "")

            # Updating text
            opt1_text.set(eval(f"qst_{num}.btn1_text"))
            opt2_text.set(eval(f"qst_{num}.btn2_text"))
            opt3_text.set(eval(f"qst_{num}.btn3_text"))
            opt4_text.set(eval(f"qst_{num}.btn4_text"))


# Button framework
def opt_btn_framework(text, btn_id):
    return Button(frame, bg="light green", command=lambda:
                  option_selected(btn_id), textvariable=text,
                  font=("Comic Sans MS", 14, "bold"))


# Holds values of buttons etc. for each question object
class Question:
    def __init__(self, qst_num, btn1_text, btn2_text, btn3_text, btn4_text):
        self.qst_num = qst_num
        self.btn1_text = btn1_text
        self.btn2_text = btn2_text
        self.btn3_text = btn3_text
        self.btn4_text = btn4_text


# Questions
qst_0 = Question(0, "🍔", "🍔", "🍔", "🍔",)  # qst_0 is the welcome screen
qst_1 = Question(1, "Kahurangi", "Whero", "Rohi", "Rongo")
qst_2 = Question(2, "Yellow", "Blue", "Green", "Orange")
qst_3 = Question(3, "Karaka", "Kahurangi", "Kākāriki", "Ngako")
qst_4 = Question(4, "Red", "Violet", "Yellow", "Purple")
qst_5 = Question(5, "Whero whero", "Kōwhai", "Koura", "karekau")
qst_6 = Question(6, "Silver", "Black", "Turquoise", "Crimson")
qst_7 = Question(7, "Pokarekare", "Ma", "Kotakota", "kākāriki")
qst_8 = Question(8, "Black", "Red", "White", "Yellow")
qst_9 = Question(9, "Kōwhai", "Ma", "Rohi", "Whero")
qst_10 = Question(10, "Gold", "Purple", "Pink", "Brown")

# Declaring widgets
cur_que_border = Label(frame, bg="black")
current_question_box = Label(frame, textvariable=current_question,
                             font=("Comic Sans MS", 9, "bold"), bg="green",
                             fg="black")
option1 = opt_btn_framework(opt1_text, 1)
option2 = opt_btn_framework(opt2_text, 2)
option3 = opt_btn_framework(opt3_text, 3)
option4 = opt_btn_framework(opt4_text, 4)

# Placing widgets
cur_que_border.place(x=17.25, y=17, width=55.5, height=35.5)
current_question_box.place(x=20, y=20, width=50, height=30)
option1.place(x=150, y=250, width=320, height=80)
option2.place(x=555, y=250, width=320, height=80)
option3.place(x=150, y=400, width=320, height=80)
option4.place(x=555, y=400, width=320, height=80)

# Welcome screen
opt1_text.set(eval(f"qst_{num}.btn1_text"))
opt2_text.set(eval(f"qst_{num}.btn2_text"))
opt3_text.set(eval(f"qst_{num}.btn3_text"))
opt4_text.set(eval(f"qst_{num}.btn4_text"))

frame.pack(fill=BOTH, expand=YES)
win.mainloop()
