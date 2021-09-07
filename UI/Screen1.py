from tkinter import *


class Screen1(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
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

        self.background_img = PhotoImage(file=f"resources/images/background.png")
        self.background = self.canvas.create_image(
            671.0, 381.0,
            image=self.background_img)

        self.entry0_img = PhotoImage(file=f"resources/images/img_textBox0.png")
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

        self.entry1_img = PhotoImage(file=f"resources/images/img_textBox1.png")
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

        self.entry2_img = PhotoImage(file=f"resources/images/img_textBox2.png")
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

        self.entry3_img = PhotoImage(file=f"resources/images/img_textBox3.png")
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

        self.entry4_img = PhotoImage(file=f"resources/images/img_textBox4.png")
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

        self.img0 = PhotoImage(file=f"resources/images/img0.png")
        self.img1 = PhotoImage(file=f"resources/images/img1.png")
        self.b0 = Label(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            relief=FLAT)

        self.b0.bind("<Button-1>", lambda e: self.btn_clicked ())

        self.b0.place(
            x=586, y=796,
            width=233,
            height=87)

        self.changeOnHover(self.b0, self.img1, self.img0)



    def btn_clicked(self):
        print ("Button Clicked")

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind ("<Enter>", func=lambda e: button.config (
            image=colorOnHover))
        button.bind ("<Leave>", func=lambda e: button.config (
            image=colorOnLeave))
