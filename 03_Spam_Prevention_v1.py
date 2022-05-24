from tkinter import *

root = Tk()
root.geometry("660x200")
root.title("Prevent multiple clicks")
count = 0


def prevent():
    global count, time
    count += 1
    label.config(text=f"Total clicks of button are:{count}")
    if count == 1:
        click.config(state=DISABLED)
        time = 4
        count = 0

        def countdown():
            global time
            if time >= 0:
                label.config(text=f"Button will be Enabled in {time} seconds")
                time -= 1
                label.after(1000, countdown)
            else:
                global count
                label.config(text=f"Total clicks of button are: 0")
                click.config(state=NORMAL)

        countdown()


label = Label(root, text="Total clicks of button are: 0", font="ariel 25 bold")
label.pack(padx=30, pady=30)
click = Button(root, text="Click Here", font="ariel 25 bold",
               width=10, bg="black", fg="white", command=prevent)
click.pack(padx=30, pady=10)
root.mainloop()
