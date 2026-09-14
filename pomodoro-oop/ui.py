from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# work_min = 2
# short_break_min = 1
# long_break_min = 3


class Ui(Tk):

    def __init__(self, timer=None, config=None):
        super().__init__()
        self.mod = config
        self.parent = timer

        self.title("Pomodoro")
        self.config(padx=100, pady=50, bg=YELLOW)

        #Timer Label
        self.timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
        self.timer_label.grid(row=0, column=1)

        # Tomato
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 110.5, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(row=1, column=1)

        # Start Button
        self.start_button = Button(text="Start", command=self.parent.start_timer)
        self.start_button.grid(row=2, column=0)

        # Reset Button
        reset_button = Button(text="Reset", command=self.parent.reset_timer)
        reset_button.grid(row=2, column=2)

        # Checkmark Label
        self.checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        self.checkmark_label.grid(row=3, column=1)

        # My personal modification
        # Config Button
        self.config_button = Button(text="Config", command=self.mod.config_button_press)
        self.config_button.grid(row=3, column=2)

        #Submit Button
        self.submit_button = Button(text="Submit", command=self.mod.submit)
        self.submit_button.grid(row=7, column=2)

        #mods
        # Labels
        self.work_time_label = Label(text="Work Time", bg=YELLOW)
        self.work_time_label.grid(row=4, column=0)

        self.short_break_time_label = Label(text="Short Break", bg=YELLOW)
        self.short_break_time_label.grid(row=5, column=0)

        self.long_break_time_label = Label(text="Long Break", bg=YELLOW)
        self.long_break_time_label.grid(row=6, column=0)

        # Current Timing Label
        self.current_work_time_label = Label(text=self.mod.work_min, bg=YELLOW)
        self.current_work_time_label.grid(row=4, column=1)

        self.current_short_break_time_label = Label(text=self.mod.short_break_min, bg=YELLOW)
        self.current_short_break_time_label.grid(row=5, column=1)

        self.current_long_break_time_label = Label(text=self.mod.long_break_min, bg=YELLOW)
        self.current_long_break_time_label.grid(row=6, column=1)

        # Input for Time Change
        self.work_time_entry = Entry(width=7)
        self.work_time_entry.grid(row=4, column=2)

        self.short_break_time_entry = Entry(width=7)
        self.short_break_time_entry.grid(row=5, column=2)

        self.long_break_time_entry = Entry(width=7)
        self.long_break_time_entry.grid(row=6, column=2)
