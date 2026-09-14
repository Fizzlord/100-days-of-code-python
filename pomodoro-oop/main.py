from tkinter import *
from ui import Ui
from timer_mechanism import Timer
from config import Config

timer = Timer()
config = Config()
ui = Ui(timer, config)
timer.parent = ui
timer.mod = config
config.parent = ui
ui.geometry("554x405")





mainloop()

