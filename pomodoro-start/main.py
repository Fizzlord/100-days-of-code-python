from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
work_min = 25
short_break_min = 5
long_break_min = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():

    """

    :return:
    """
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():

    """

    :return:
    """
    global reps
    reps += 1
    work_sec = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min * 60


    if reps % 8 == 0:
        timer_label.config(text="Long", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    """

    :param count: number of seconds for countdown
    :return:
    """
    global timer

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if reps % 2 == 0:
        checkmark_label.config(text="✔" * (reps // 2))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0 and reps < 8:
        start_timer()
# ---------------------------- CONFIG ------------------------------- #

#My personal
#Able to change work, break and long break time


def config():

    """

    :return:
    """

    # Labels
    work_time_label = Label(text="Work Time", bg=YELLOW)
    work_time_label.grid(row=4, column=0)

    short_break_time_label = Label(text="Short Break", bg=YELLOW)
    short_break_time_label.grid(row=5, column=0)

    long_break_time_label = Label(text="Long Break", bg=YELLOW)
    long_break_time_label.grid(row=6, column=0)

    # Current Timing Label
    current_work_time_label = Label(text=work_min, bg=YELLOW)
    current_work_time_label.grid(row=4, column=1)

    current_short_break_time_label = Label(text=short_break_min, bg=YELLOW)
    current_short_break_time_label.grid(row=5, column=1)

    current_long_break_time_label = Label(text=long_break_min, bg=YELLOW)
    current_long_break_time_label.grid(row=6, column=1)

    # Input for Time Change
    global work_time_entry
    work_time_entry = Entry(width=7)
    work_time_entry.grid(row=4, column=2)

    global short_break_time_entry
    short_break_time_entry = Entry(width=7)
    short_break_time_entry.grid(row=5, column=2)

    global long_break_time_entry
    long_break_time_entry = Entry(width=7)
    long_break_time_entry.grid(row=6, column=2)

    submit_button = Button(text="Submit", command=submit)
    submit_button.grid(row=7, column=2)

def submit():

        global work_min, short_break_min, long_break_min

        work_min = int(work_time_entry.get())
        short_break_min = int(short_break_time_entry.get())
        long_break_min = int(long_break_time_entry.get())


#--------------------------- UI SETUP -----------------------------------#

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Timer Label

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

#Tomato

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 110.5, image=tomato_img)
timer_text = canvas.create_text(100, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#Start Button

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

#Reset Button

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

#Checkmark Label
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,20,"bold"))
checkmark_label.grid(row=3, column=1)

#My personal modification

# Config Button
config_button = Button(text="Config", command=config)
config_button.grid(row=3, column=2)







window.mainloop()