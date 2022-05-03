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
opt1_text = StringVar()
opt2_text = StringVar()
opt3_text = StringVar()
opt4_text = StringVar()
btn_disabled = False  # Buttons do nothing if btn_disabled = True
num = 0
current_question = StringVar()
current_question.set(f"{num}/10")


def option_selected():
    global num
    if not btn_disabled:
        if num < 10:
            num += 1

            # If correct...

            # Update buttons and labels
            current_question.set(f"{num}/10")
            opt1_text.set(eval(f"qst_{num}.btn1_text"))
            opt2_text.set(eval(f"qst_{num}.btn2_text"))
            opt3_text.set(eval(f"qst_{num}.btn3_text"))
            opt4_text.set(eval(f"qst_{num}.btn4_text"))
            output_box_txt.set(eval(f"qst_{num}.question"))


def opt_btn_framework(text):
    return Button(frame, bg="light green", command=option_selected, textvariable=text, font=("Comic Sans MS", 14, "bold"))


class Options:
    def __init__(self, qst_num, question, btn1_text, btn2_text, btn3_text, btn4_text, answer):
        self.qst_num = qst_num
        self.question = question
        self.btn1_text = btn1_text
        self.btn2_text = btn2_text
        self.btn3_text = btn3_text
        self.btn4_text = btn4_text
        self.answer = answer


# Questions
qst_0 = Options(0, "Welcome to the Te Reo Maori Quiz! "
                   "Press any of the buttons below to begin the quiz.",
                   "Click", "One", "Of", "Us", "answer")  # qst_0 is the welcome screen
qst_1 = Options(1, "What is 'red' in Maori ?", "Kahurangi", "Whero", "Rohi", "Rongo", "Whero")
qst_2 = Options(2, "What colour is 'kākāriki' ?", "Yellow", "Blue", "Green", "Orange", "Green")
qst_3 = Options(3, "What is 'orange' in Maori ?", "Karaka", "Kahurangi", "Kākāriki", "Ngako", "Karaka")
qst_4 = Options(4, "What colour is 'papura' ?", "Red", "Violet", "Yellow", "Purple", "Purple")
qst_5 = Options(5, "What is 'yellow' in Maori ?", "Whero whero", "Kōwhai", "Koura", "karekau", "Kōwhai")
qst_6 = Options(6, "What colour is 'Karekau' ?", "Silver", "Black", "Turquoise", "Crimson", "Turquoise")
qst_7 = Options(7, "What is 'lime' in Maori ?", "Pokarekare", "Ma", "Kotakota", "kākāriki", "Kotakota")
qst_8 = Options(8, "What colour is 'pango' ?", "Black", "Red", "White", "Yellow", "Black")
qst_9 = Options(9, "What is 'White' in Maori ?", "Kōwhai", "Ma", "Rohi", "Whero", "Ma")
qst_10 = Options(10, "What colour is 'parauri' ?", "Gold", "Purple", "Pink", "Brown", "Brown")


# Declaring widgets
output_box = Label(frame, textvariable=output_box_txt,
                   font=("Comic Sans MS", 13), bg="white", fg="black")
cur_que_border = Label(frame, bg="black")
current_question_box = Label(frame, textvariable=current_question, font=("Comic Sans MS", 9, "bold"), bg="green", fg="black")
option1 = opt_btn_framework(opt1_text)
option2 = opt_btn_framework(opt2_text)
option3 = opt_btn_framework(opt3_text)
option4 = opt_btn_framework(opt4_text)

# Placing widgets
output_box.place(x=150, y=100, width=725, height=80)
cur_que_border.place(x=17.25, y=17, width=55.5, height=35.5)
current_question_box.place(x=20, y=20, width=50, height=30)
option1.place(x=150, y=250, width=320, height=80)
option2.place(x=555, y=250, width=320, height=80)
option3.place(x=150, y=400, width=320, height=80)
option4.place(x=555, y=400, width=320, height=80)


# Welcome screen
output_box_txt.set(f"{qst_0.question}")
opt1_text.set(eval(f"qst_{num}.btn1_text"))
opt2_text.set(eval(f"qst_{num}.btn2_text"))
opt3_text.set(eval(f"qst_{num}.btn3_text"))
opt4_text.set(eval(f"qst_{num}.btn4_text"))

frame.pack(fill=BOTH, expand=YES)
win.mainloop()
