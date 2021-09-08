import os
from tkinter import *
from UI.Screen1 import Screen1
from UI.Screen2 import Screen2
from UI.Screen3 import Screen3


class Application (Tk):

    def __init__(self, *args):
        Tk.__init__ (self)
        self.title("Potfolio Maker App")
        self.geometry("1440x1024")
        self.configure(bg="#83568a")
        self.currentScreen = None
        self.change_to_screen(Screen1)
        self.overrideredirect(True)
        super().bind("<Button-1>", self.clickwin)
        super().bind("<B1-Motion>", self.dragwin)



        self.resizable(False, False)
        self.mainloop()

    def dragwin(self, event):
        x = super ().winfo_pointerx () - self._offsetx
        y = super ().winfo_pointery () - self._offsety
        super ().geometry (f"+{x}+{y}")

    def clickwin(self, event):
        self._offsetx = super ().winfo_pointerx () - super ().winfo_rootx ()
        self._offsety = super ().winfo_pointery () - super ().winfo_rooty ()

    def change_to_screen(self, Screen):
        screen = Screen (self)
        screen.pack (fill="both", expand=True)
        if self.currentScreen is not None:
            self.currentScreen.forget ()
        self.currentScreen = screen

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind ("<Enter>", func=lambda e: button.config (
            image=colorOnHover))
        button.bind ("<Leave>", func=lambda e: button.config (
            image=colorOnLeave))




app = Application()
