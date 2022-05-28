"""
Purpose: Displays question and answer history in separate window
Creator: Sammy Cummins
Version: 1
"""


# Imports
from tkinter import *  # GUI
from functools import partial  # To prevent unwanted windows

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
output_box_txt = StringVar()
opt1_text = StringVar()
opt2_text = StringVar()
opt3_text = StringVar()
opt4_text = StringVar()
btn_disabled = False  # Buttons do nothing if btn_disabled = True
num = 0  # Question number
num_correct = 0  # Number of questions guest correctly
current_question = StringVar()
current_question.set(f"{num}/10")
history_string = "No history has been recorded yet.\nStart the quiz to " \
                 "gain some sweet history!\n\n\n"
guess_history = []
final_score_history = []


def option_selected(what_btn):
    global num, num_correct, btn_disabled, history_string
    if not btn_disabled:
        if num < 11:
            num += 1

            question = eval(f"qst_{num - 1}.question")
            user_ans = eval(f"qst_{num - 1}.btn{what_btn}_text")
            real_ans = eval(f"qst_{num - 1}.answer")

            # If correct...
            # If answer == button text and not welcome screen:
            if eval(f"qst_{num - 1}.answer") == eval(
                    f"qst_{num - 1}.btn{what_btn}_text") and num != 1:
                num_correct += 1
                output_box.config(bg="lime")
                output_box_txt.set("Correct!")
                guess_history.append(f"Question: {question}\nYour "
                                     f"Answer: {user_ans}\nActual Answer: "
                                     f"{real_ans}\n\n")
            elif eval(f"qst_{num - 1}.answer") != eval(
                    f"qst_{num - 1}.btn{what_btn}_text") and num != 1:
                output_box.config(bg="red")
                output_box_txt.set("Incorrect!")
                guess_history.append(f"Question: {question}\nYour "
                                     f"Answer: {user_ans}\nActual Answer: "
                                     f"{real_ans}\n\n")

            # Adding guess results to history
            try:
                if guess_history:
                    history_string = guess_history[-1] + guess_history[-2]
            except IndexError:
                if guess_history:
                    history_string = guess_history[-1]

            if num == 11:
                btn_disabled = True

            # Update buttons and labels
            def up_btn():
                if num <= 10:
                    current_question.set(f"{num}/10")
                else:
                    qst_11 = Question(11, f"You finished the quiz and got "
                                          f"{num_correct}/10 question correct."
                                          f"\nPress restart to play again.",
                                      "", "", "", "", "")
                    final_score_history.append(f"{num_correct}/10\n")
                    print(final_score_history)

                opt1_text.set(eval(f"qst_{num}.btn1_text"))
                opt2_text.set(eval(f"qst_{num}.btn2_text"))
                opt3_text.set(eval(f"qst_{num}.btn3_text"))
                opt4_text.set(eval(f"qst_{num}.btn4_text"))
                output_box_txt.set(eval(f"qst_{num}.question"))
                output_box.config(bg="white")

            # Time delay (1 sec) for button and label appearance
            if num > 1:
                output_box.after(1000, up_btn)
            else:
                up_btn()


def opt_btn_framework(text, btn_id):
    return Button(frame, bg="light green", command=lambda:
                  option_selected(btn_id), textvariable=text,
                  font=("Comic Sans MS", 14, "bold"))


def history(history_string):
    # disable history button
    history_btn.config(state=DISABLED)

    background = "#a9ef99"  # Pale green
    history_frame = Frame(win, width=300, bg=background)
    history_frame.place(x=0, y=0, height=1000, width=1000)

    # Set up history heading (row 0)
    how_heading = Label(history_frame,
                        text="\nQuiz History",
                        font="arial 14 bold", bg=background)
    how_heading.place(x=442, y=85)

    # history text (label, row 1)
    history_text = Label(history_frame,
                         text="Here are your two most recent guess results. "
                              "Please use the export button to "
                              "create a text file of all your "
                              "guesses and final scores for this session\n",
                         justify=LEFT, width=40, bg=background,
                         wraplength=250, font="arial 10 italic", )
    history_text.place(x=340, y=160)

    history_label = Label(history_frame, text=history_string,
                          bg="white", font="Arial 10", justify=LEFT,
                          wraplength=300)
    history_label.place(x=380, y=260, width=250)

    def close_history():
        history_btn.config(state=NORMAL)
        history_frame.destroy()

    dismiss_button = Button(history_frame, text="Dismiss",
                            font="arial 10 bold",
                            command=partial(close_history))
    dismiss_button.place(x=380, y=430, width=250, height=50)


class Question:
    def __init__(self, qst_num, question, btn1_text, btn2_text, btn3_text,
                 btn4_text, answer):
        self.qst_num = qst_num
        self.question = question
        self.btn1_text = btn1_text
        self.btn2_text = btn2_text
        self.btn3_text = btn3_text
        self.btn4_text = btn4_text
        self.answer = answer


# Questions
qst_0 = Question(0, "Welcome to the Te Reo Maori Colour Quiz!\n"
                    "Press any of the buttons below to begin the quiz.",
                 "🍔", "🍔", "🍔", "🍔",
                 "answer")  # qst_0 is the welcome screen
qst_1 = Question(1, "What is 'red' in Maori ?", "Kahurangi", "Whero", "Rohi",
                 "Rongo", "Whero")
qst_2 = Question(2, "What colour is 'kākāriki' ?", "Yellow", "Blue", "Green",
                 "Orange", "Green")
qst_3 = Question(3, "What is 'orange' in Maori ?", "Karaka", "Kahurangi",
                 "Kākāriki", "Ngako", "Karaka")
qst_4 = Question(4, "What colour is 'papura' ?", "Red", "Violet", "Yellow",
                 "Purple", "Purple")
qst_5 = Question(5, "What is 'yellow' in Maori ?", "Whero whero", "Kōwhai",
                 "Koura", "karekau", "Kōwhai")
qst_6 = Question(6, "What colour is 'Karekau' ?", "Silver", "Black",
                 "Turquoise", "Crimson", "Turquoise")
qst_7 = Question(7, "What is 'lime' in Maori ?", "Pokarekare", "Ma",
                 "Kotakota", "kākāriki", "Kotakota")
qst_8 = Question(8, "What colour is 'pango' ?", "Black", "Red", "White",
                 "Yellow", "Black")
qst_9 = Question(9, "What is 'White' in Maori ?", "Kōwhai", "Ma", "Rohi",
                 "Whero", "Ma")
qst_10 = Question(10, "What colour is 'parauri' ?", "Gold", "Purple", "Pink",
                  "Brown", "Brown")

# Declaring widgets
output_box = Label(frame, textvariable=output_box_txt,
                   font=("Comic Sans MS", 13), bg="white", fg="black")
cur_que_border = Label(frame, bg="black")
current_question_box = Label(frame, textvariable=current_question,
                             font=("Comic Sans MS", 9, "bold"), bg="green",
                             fg="black")
option1 = opt_btn_framework(opt1_text, 1)
option2 = opt_btn_framework(opt2_text, 2)
option3 = opt_btn_framework(opt3_text, 3)
option4 = opt_btn_framework(opt4_text, 4)
history_btn = Button(frame, bg="pink", command=lambda: history(history_string),
                     text="History", font=("Comic Sans MS", 12, "bold"))

# Placing widgets
output_box.place(x=150, y=100, width=725, height=80)
cur_que_border.place(x=17.25, y=17, width=55.5, height=35.5)
current_question_box.place(x=20, y=20, width=50, height=30)
option1.place(x=150, y=250, width=320, height=80)
option2.place(x=555, y=250, width=320, height=80)
option3.place(x=150, y=400, width=320, height=80)
option4.place(x=555, y=400, width=320, height=80)
history_btn.place(x=800, y=20, width=80, height=35)

# Welcome screen
output_box_txt.set(f"{qst_0.question}")
opt1_text.set(eval(f"qst_{num}.btn1_text"))
opt2_text.set(eval(f"qst_{num}.btn2_text"))
opt3_text.set(eval(f"qst_{num}.btn3_text"))
opt4_text.set(eval(f"qst_{num}.btn4_text"))

frame.place(x=0, y=0, width=1000, height=1000)
win.mainloop()
