from tkinter import *
from UI.Screen1 import *

class Window(Tk):
    def __init__(self, *args):
        Tk.__init__(self)
        self.title("Potfolio Maker App")
        self.geometry("1440x1024")
        self.configure(bg="#83568a")
        screen1 = Screen1(self)
        screen1.pack(fill="both", expand=True)
        self.mainloop()


win = Window()



