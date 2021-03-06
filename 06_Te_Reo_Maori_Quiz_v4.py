"""
Creator: Sammy Cummins
Version: 4
Update: This version contains question randomisation
"""

# Imports
import random  # For question randomisation
from tkinter import *  # GUI
from functools import partial  # To prevent unwanted windows
from tkinter import filedialog  # For exporting files

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
count = 0
current_question = StringVar()
current_question.set(f"{num}/10")
history_string = "No history has been recorded yet.\nStart the quiz to " \
                 "gain some sweet history!"
guess_history = []  # Records all guesses for later display
final_score_history = []  # Contains final scores for export
qst_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # List of available questions


# Prevents button spamming
def prevent_spam(what_btn_transfer):
    global count, time
    count += 1
    if count == 1:
        eval(f"option{what_btn_transfer}").config(state=DISABLED)
        time = 0.2
        count = 0

        def countdown():
            global time
            if time >= 0:
                time -= 1
                if num != 0:
                    output_box.after(1000, countdown)
                else:
                    output_box.after(1, countdown)
                option_selected(what_btn_transfer)
            else:
                global count
                eval(f"option{what_btn_transfer}").config(state=NORMAL)

        countdown()


# Updating to next question and answer confirmation
def option_selected(what_btn):
    global num, num_correct, btn_disabled, history_string, qst_id
    if not btn_disabled:
        if num < 11:
            if num == 0:
                qst_id = 0
            num += 1

            question = eval(f"qst_{qst_id}.question")
            user_ans = eval(f"qst_{qst_id}.btn{what_btn}_text")
            real_ans = eval(f"qst_{qst_id}.answer")

            if num != 1:  # If not welcome screen
                # If answer == button text... correct or not:
                if eval(f"qst_{qst_id}.answer") == eval(
                        f"qst_{qst_id}.btn{what_btn}_text") and num != 0:
                    num_correct += 1
                    output_box.config(bg="lime")
                    output_box_txt.set("Correct!")
                    guess_history.append(f"Question: {question}\nYour "
                                         f"Answer: {user_ans}\nActual Answer: "
                                         f"{real_ans}\n\n")
                elif eval(f"qst_{qst_id}.answer") != eval(
                        f"qst_{qst_id}.btn{what_btn}_text") and num != 0:
                    output_box.config(bg="red")
                    output_box_txt.set("Incorrect!")
                    guess_history.append(f"Question: {question}\nYour "
                                         f"Answer: {user_ans}\nActual Answer: "
                                         f"{real_ans}\n\n")

            # Adding guess results to history
            try:
                if guess_history and num > 1:
                    history_string = guess_history[-1] + guess_history[-2]
            except IndexError:
                if guess_history and num > 1:
                    history_string = guess_history[-1]

            # Makes option buttons do nothing once the quiz is finished
            if num == 11:
                btn_disabled = True

            # Randomly selecting a question
            if num <= 10:
                qst_id = random.choice(qst_list)
                qst_list.remove(qst_id)
            elif num == 11:
                qst_id = 11

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

                opt1_text.set(eval(f"qst_{qst_id}.btn1_text"))
                opt2_text.set(eval(f"qst_{qst_id}.btn2_text"))
                opt3_text.set(eval(f"qst_{qst_id}.btn3_text"))
                opt4_text.set(eval(f"qst_{qst_id}.btn4_text"))
                output_box_txt.set(eval(f"qst_{qst_id}.question"))
                output_box.config(bg="white")

            # Time delay (1 sec) for button and label appearance
            if num > 1:
                output_box.after(1000, up_btn)
            else:
                up_btn()


# Framework for the option buttons to save on space
def opt_btn_framework(text, btn_id):
    return Button(frame, bg="light green", command=lambda:
                  prevent_spam(btn_id), textvariable=text,
                  font=("Comic Sans MS", 14, "bold"))


# Restarts the quiz
def restart():
    global num, num_correct, btn_disabled, qst_list
    qst_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Resets question pool
    num = 0
    num_correct = 0
    btn_disabled = False
    option_selected(1)  # Running function to change button and label text


# Opens history window and contains the functions of some widgets
def history(history_string):

    background = "#a9ef99"  # Pale green
    history_frame = Frame(win, width=300, bg=background)
    history_frame.place(x=0, y=0, height=1000, width=1000)

    how_heading = Label(history_frame,
                        text="\nQuiz History",
                        font="arial 14 bold", bg=background)
    how_heading.place(x=442, y=55)

    history_text = Label(history_frame,
                         text="Here are your two most recent guess results. "
                              "Please use the export button to "
                              "create a text file of all your "
                              "guesses and final scores for this session\n",
                         justify=LEFT, width=40, bg=background,
                         wraplength=250, font="arial 10 italic", )
    history_text.place(x=340, y=130)

    history_label = Label(history_frame, text=history_string,
                          bg="white", font="Arial 10", justify=LEFT,
                          wraplength=250)
    history_label.place(x=380, y=230, width=250, height=150)

    # Closes history screen
    def close_history():
        history_frame.destroy()

    dismiss_button = Button(history_frame, text="Dismiss",
                            font="arial 10 bold",
                            command=partial(close_history))
    dismiss_button.place(x=380, y=400, width=250, height=50)

    history.export_button = Button(history_frame, text="Export",
                                   font="arial 10 bold", command=export)
    history.export_button.place(x=380, y=470, width=250, height=50)


# To export results at end of quiz
def export():
    # Disable export button while save window is open
    history.export_button.config(state=DISABLED)

    # Strings to be compiled and displayed in the exported text file
    guess_history_string = ""
    final_score_string = ""

    for item in guess_history:
        guess_history_string += item
    for item in final_score_history:
        final_score_string += item

    # Constructing export text
    export_string = f"----Final Scores----\n{final_score_string}\n" \
                    f"\n----Guesses----\n{guess_history_string}"

    # Opens file explorer save window
    filename = filedialog.asksaveasfilename(initialdir='/Desktop',
                                            title='Save File',
                                            defaultextension=".txt")
    # Writes to text file
    try:
        my_file = open(filename, "w+", encoding="utf-8")
        my_file.write(export_string)
    except FileNotFoundError:
        history.export_button.config(state=ACTIVE)


# Holds question objects, so you can use this to add more questions
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
                 "????", "????", "????", "????",
                 "answer")  # qst_0 is the welcome screen
qst_1 = Question(1, "What is 'red' in Maori ?", "Kahurangi", "Whero", "Rohi",
                 "Rongo", "Whero")
qst_2 = Question(2, "What colour is 'k??k??riki' ?", "Yellow", "Blue", "Green",
                 "Orange", "Green")
qst_3 = Question(3, "What is 'orange' in Maori ?", "Karaka", "Kahurangi",
                 "K??k??riki", "Ngako", "Karaka")
qst_4 = Question(4, "What colour is 'papura' ?", "Red", "Violet", "Yellow",
                 "Purple", "Purple")
qst_5 = Question(5, "What is 'yellow' in Maori ?", "Whero whero", "K??whai",
                 "Koura", "karekau", "K??whai")
qst_6 = Question(6, "What colour is 'Karekau' ?", "Silver", "Black",
                 "Turquoise", "Crimson", "Turquoise")
qst_7 = Question(7, "What is 'lime' in Maori ?", "Pokarekare", "Ma",
                 "Kotakota", "k??k??riki", "Kotakota")
qst_8 = Question(8, "What colour is 'pango' ?", "Black", "Red", "White",
                 "Yellow", "Black")
qst_9 = Question(9, "What is 'White' in Maori ?", "K??whai", "Ma", "Rohi",
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
restart_btn = Button(frame, bg="pink", command=restart, text="Restart",
                     font=("Comic Sans MS", 12, "bold"))
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
restart_btn.place(x=900, y=20, width=80, height=35)
history_btn.place(x=800, y=20, width=80, height=35)

# Welcome screen
output_box_txt.set(f"{qst_0.question}")
opt1_text.set(eval(f"qst_{num}.btn1_text"))
opt2_text.set(eval(f"qst_{num}.btn2_text"))
opt3_text.set(eval(f"qst_{num}.btn3_text"))
opt4_text.set(eval(f"qst_{num}.btn4_text"))

frame.pack(fill=BOTH, expand=YES)
win.mainloop()
