from tkinter import *
from UI.Screen1 import Screen1
from UI.Screen2 import Screen2


class Window(Tk):
    def __init__(self, *args):
        Tk.__init__(self)
        self.title("Potfolio Maker App")
        self.geometry("1440x1024")
        self.configure(bg="#83568a")
        self.currentScreen = None
        self.change_to_screen(Screen1)
        self.mainloop()
        
    def change_to_screen(self, Screen):
        screen = Screen(self)
        screen.pack(fill="both", expand=True)
        if self.currentScreen is not None:
            self.currentScreen.forget()
        self.currentScreen = screen




win = Window()



