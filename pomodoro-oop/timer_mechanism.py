import ui

class Timer:

    def __init__(self, parent=None, config=None):
        self.parent = parent
        self.mod = config
        self.reps = 0
        self.work_sec = None
        self.short_break_sec = None
        self.long_break_sec = None
        self.timer = None

    def start_timer(self):
        self.work_sec = self.mod.work_min * 60
        self.short_break_sec = self.mod.short_break_min * 60
        self.long_break_sec = self.mod.long_break_min * 60
        self.reps += 1

        if self.reps % 8 == 0:
            self.parent.timer_label.config(text="Long", fg=ui.RED)
            self.count_down(self.long_break_sec)
        elif self.reps % 2 == 0:
            self.parent.timer_label.config(text="Short", fg=ui.PINK)
            self.count_down(self.short_break_sec)
        else:
            self.parent.timer_label.config(text="Work", fg=ui.GREEN)
            self.count_down(self.work_sec)

    def count_down(self, count):

        count_min = count // 60
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        self.parent.canvas.itemconfig(self.parent.timer_text, text=f"{count_min}:{count_sec}")
        if self.reps % 2 == 0:
            self.parent.checkmark_label.config(text="✔" * (self.reps // 2))
        if count > 0:
            self.timer = self.parent.after(1000, self.count_down, count - 1)
        elif count == 0 and self.reps <8:
            self.parent.checkmark_label.config(text="✔" * (self.reps // 2))
            self.start_timer()

    def reset_timer(self):
        self.parent.after_cancel(self.timer)
        self.parent.timer_label.config(text="Timer", fg=ui.GREEN)
        self.parent.canvas.itemconfig(self.parent.timer_text, text="00:00")
        self.parent.checkmark_label.config(text="")
        self.reps = 0