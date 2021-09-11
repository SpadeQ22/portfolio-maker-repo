import os
from tkinter import *
from UI.Screen2 import Screen2

class Screen1(Frame):

    def __init__(self, window):
        Frame.__init__(self, window)
        self.win = window
        self.configure(bg="#83568a")
        self.canvas = Canvas(
            self,
            bg="#83568a",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"resources/images/screen1/background.png")
        self.background = self.canvas.create_image(
            671.0, 381.0,
            image=self.background_img)

        self.entry0_img = PhotoImage(file=f"resources/images/screen1/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            708.5, 318.0,
            image=self.entry0_img)

        self.entry0 = Entry(
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry0.place(
            x=484.0, y=298,
            width=449.0,
            height=38)

        self.entry1_img = PhotoImage(file=f"resources/images/screen1/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            708.5, 410.0,
            image=self.entry1_img)

        self.entry1 = Entry(
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry1.place(
            x=484.0, y=390,
            width=449.0,
            height=38)

        self.entry2_img = PhotoImage(file=f"resources/images/screen1/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image (
            708.5, 511.0,
            image=self.entry2_img)

        self.entry2 = Entry(
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry2.place(
            x=484.0, y=491,
            width=449.0,
            height=38)

        self.entry3_img = PhotoImage(file=f"resources/images/screen1/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(
            708.5, 600.0,
            image=self.entry3_img)

        self.entry3 = Entry(
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry3.place(
            x=484.0, y=580,
            width=449.0,
            height=38)

        self.entry4_img = PhotoImage(file=f"resources/images/screen1/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image (
            708.5, 694.0,
            image=self.entry4_img)

        self.entry4 = Entry(
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry4.place(
            x=484.0, y=674,
            width=449.0,
            height=38)

        self.img0 = PhotoImage(file=f"resources/images/screen1/img0.png")
        self.img1 = PhotoImage(file=f"resources/images/screen1/img1.png")
        self.b0 = Label(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            relief=FLAT)

        self.b0.bind("<Button-1>", lambda e: self.btn_clicked())

        self.b0.place(
            x=586, y=796,
            width=233,
            height=87)

        self.changeOnHover(self.b0, self.img1, self.img0)

        self.img4 = PhotoImage (file=f"resources/images/screen1/img4.png")
        self.img4_hover = PhotoImage (file=f"resources/images/screen1/img4_hover.png")
        self.b4 = Label (
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")
        self.b4.place (
            x=1393, y=0,
            width=48,
            height=37)

        self.img6 = PhotoImage (file=f"resources/images/screen1/img6.png")
        self.img6_hover = PhotoImage (file=f"resources/images/screen1/img6_hover.png")
        self.b6 = Label (
            image=self.img6,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")
        self.b6.place (
            x=1346, y=0,
            width=48,
            height=37)

        self.changeOnHover (self.b4, self.img4_hover, self.img4)
        self.changeOnHover (self.b6, self.img6_hover, self.img6)
        self.b4.bind("<Button-1>", lambda e: self.close())
        self.b6.bind("<Button-1>", lambda e: self.minimize())
        self.win.focus_force()
        self.win.bind("<Alt-KeyPress-Tab>", lambda e: self.minimize2())
        self.bind("<Map>", self.frame_mapped)

    def btn_clicked(self):
        self.win.change_to_screen(Screen=Screen2)

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind ("<Enter>", func=lambda e: button.config (
            image=colorOnHover))
        button.bind ("<Leave>", func=lambda e: button.config (
            image=colorOnLeave))

    def close(self):
        os._exit (0)

    def frame_mapped(self, e):
        self.win.update_idletasks ()
        self.win.overrideredirect (True)
        self.win.state('normal')

    def minimize(self):
        self.win.update_idletasks ()
        self.win.overrideredirect (False)
        self.win.state ('iconic')

    def minimize2(self):
        self.win.update_idletasks ()
        self.win.overrideredirect (False)
        self.win.state ('iconic')




