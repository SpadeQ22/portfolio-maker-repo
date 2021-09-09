import os
from tkinter import *


class Screen2(Frame):
    def __init__(self, win):
        Frame.__init__(self, win)
        self.win = win
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

        self.entry0_img = PhotoImage(file=f"resources/images/screen2/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            312.0, 382.5,
            image=self.entry0_img)

        self.entry0 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry0.place (
            x=163.0, y=358,
            width=298.0,
            height=47)

        self.entry1_img = PhotoImage (file=f"resources/images/screen2/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image (
            536.0, 646.0,
            image=self.entry1_img)

        self.entry1 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry1.place (
            x=522.0, y=622,
            width=28.0,
            height=46)

        self.entry2_img = PhotoImage (file=f"resources/images/screen2/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image (
            536.0, 474.0,
            image=self.entry2_img)

        self.entry2 = Entry(
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry2.place (
            x=522.0, y=451,
            width=28.0,
            height=44)

        self.entry3_img = PhotoImage (file=f"resources/images/screen2/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image (
            549.5, 383.5,
            image=self.entry3_img)

        self.entry3 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry3.place (
            x=514.0, y=360,
            width=71.0,
            height=45)

        self.entry4_img = PhotoImage (file=f"resources/images/screen2/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image (
            673.5, 383.5,
            image=self.entry4_img)

        self.entry4 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry4.place (
            x=638.0, y=360,
            width=71.0,
            height=45)

        self.entry5_img = PhotoImage (file=f"resources/images/screen2/img_textBox5.png")
        self.entry5_bg = self.canvas.create_image (
            536.0, 560.0,
            image=self.entry5_img)

        self.entry5 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry5.place (
            x=522.0, y=538,
            width=28.0,
            height=42)

        self.entry6_img = PhotoImage (file=f"resources/images/screen2/img_textBox6.png")
        self.entry6_bg = self.canvas.create_image (
            536.0, 728.0,
            image=self.entry6_img)

        self.entry6 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry6.place (
            x=522.0, y=707,
            width=28.0,
            height=40)

        self.entry7_img = PhotoImage (file=f"resources/images/screen2/img_textBox7.png")
        self.entry7_bg = self.canvas.create_image (
            1249.0, 560.0,
            image=self.entry7_img)

        self.entry7 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry7.place (
            x=1237.0, y=538,
            width=24.0,
            height=42)

        self.entry8_img = PhotoImage (file=f"resources/images/screen2/img_textBox8.png")
        self.entry8_bg = self.canvas.create_image (
            1249.0, 648.5,
            image=self.entry8_img)

        self.entry8 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry8.place (
            x=1237.0, y=627,
            width=24.0,
            height=41)

        self.entry9_img = PhotoImage (file=f"resources/images/screen2/img_textBox9.png")
        self.entry9_bg = self.canvas.create_image (
            1249.0, 729.5,
            image=self.entry9_img)

        self.entry9 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry9.place (
            x=1237.0, y=705,
            width=24.0,
            height=47)

        self.entry10_img = PhotoImage (file=f"resources/images/screen2/img_textBox10.png")
        self.entry10_bg = self.canvas.create_image (
            312.0, 472.5,
            image=self.entry10_img)

        self.entry10 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry10.place (
            x=163.0, y=448,
            width=298.0,
            height=47)

        self.entry11_img = PhotoImage (file=f"resources/images/screen2/img_textBox11.png")
        self.entry11_bg = self.canvas.create_image (
            312.0, 562.0,
            image=self.entry11_img)

        self.entry11 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry11.place (
            x=163.0, y=538,
            width=298.0,
            height=46)

        self.entry12_img = PhotoImage (file=f"resources/images/screen2/img_textBox12.png")
        self.entry12_bg = self.canvas.create_image (
            312.0, 645.5,
            image=self.entry12_img)

        self.entry12 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry12.place (
            x=163.0, y=621,
            width=298.0,
            height=47)

        self.entry13_img = PhotoImage (file=f"resources/images/screen2/img_textBox13.png")
        self.entry13_bg = self.canvas.create_image (
            312.0, 729.5,
            image=self.entry13_img)

        self.entry13 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry13.place (
            x=163.0, y=705,
            width=298.0,
            height=47)

        self.entry14_img = PhotoImage (file=f"resources/images/screen2/img_textBox14.png")
        self.entry14_bg = self.canvas.create_image (
            1036.0, 382.5,
            image=self.entry14_img)

        self.entry14 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry14.place (
            x=887.0, y=358,
            width=298.0,
            height=47)

        self.entry15_img = PhotoImage (file=f"resources/images/screen2/img_textBox15.png")
        self.entry15_bg = self.canvas.create_image (
            1036.0, 472.5,
            image=self.entry15_img)

        self.entry15 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry15.place (
            x=887.0, y=448,
            width=298.0,
            height=47)

        self.entry16_img = PhotoImage (file=f"resources/images/screen2/img_textBox16.png")
        self.entry16_bg = self.canvas.create_image (
            1036.0, 562.5,
            image=self.entry16_img)

        self.entry16 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry16.place (
            x=887.0, y=538,
            width=298.0,
            height=47)

        self.entry17_img = PhotoImage (file=f"resources/images/screen2/img_textBox17.png")
        self.entry17_bg = self.canvas.create_image (
            1036.0, 648.5,
            image=self.entry17_img)

        self.entry17 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry17.place (
            x=887.0, y=624,
            width=298.0,
            height=47)

        self.entry18_img = PhotoImage (file=f"resources/images/screen2/img_textBox18.png")
        self.entry18_bg = self.canvas.create_image (
            1036.0, 731.5,
            image=self.entry18_img)

        self.entry18 = Entry (
            bd=0,
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry18.place (
            x=887.0, y=707,
            width=298.0,
            height=47)

        self.img0 = PhotoImage (file=f"resources/images/screen2/img0.png")
        self.img0_hover = PhotoImage (file="resources/images/screen2/img0_hover.png")

        self.b0 = Label(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b0.place (
            x=892, y=890,
            width=209,
            height=62)

        self.changeOnHover(self.b0, self.img0_hover, self.img0)
        self.b0.bind("<Button-1>", lambda e: self.btn_clicked_add())

        self.img1 = PhotoImage (file=f"resources/images/screen2/img1.png")
        self.img1_hover = PhotoImage (file=f"resources/images/screen2/img1_hover.png")

        self.b1 = Label(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b1.place(
            x=1140, y=890,
            width=209,
            height=62)

        self.changeOnHover(self.b1, self.img1_hover, self.img1)
        self.b1.bind("<Button-1>", lambda e: self.btn_clicked_done())


        self.background_img = PhotoImage (file=f"resources/images/screen2/background.png")
        self.background = self.canvas.create_image (
            653.0, 492.0,
            image=self.background_img)

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

        self.bind("<Map>", self.frame_mapped)



    def btn_clicked_done(self):
        print("Button done Clicked")

    def btn_clicked_add(self):
        print ("Button add Clicked")

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind ("<Enter>", func=lambda e: button.config(
            image=colorOnHover))
        button.bind ("<Leave>", func=lambda e: button.config(
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