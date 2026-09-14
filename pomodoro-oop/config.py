
class Config:

    def __init__(self, timer=None):
        self.parent = timer
        self.work_min = 25
        self.short_break_min = 5
        self.long_break_min = 10
        self.config_button_is_pressed = False

    def config_button_press(self):
        """
        Changes window size when Config button is pressed

        """
        self.config_button_is_pressed = not self.config_button_is_pressed
        if self.config_button_is_pressed:
            self.parent.geometry("554x527")
        else:
            self.parent.geometry("554x405")

        print(self.config_button_is_pressed)

    def submit(self):
        self.work_min = int(self.parent.work_time_entry.get())
        self.short_break_min = int(self.parent.short_break_time_entry.get())
        self.long_break_min = int(self.parent.long_break_time_entry.get())
        self.config_button_is_pressed = not self.config_button_is_pressed


        self.parent.current_work_time_label.config(text=self.work_min)
        self.parent.current_short_break_time_label.config(text=self.short_break_min)
        self.parent.current_long_break_time_label.config(text=self.long_break_min)
        self.parent.geometry("554x405")