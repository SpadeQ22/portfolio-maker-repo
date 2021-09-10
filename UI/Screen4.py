import os
from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image


class Card:

    def __init__(self, label):
        self.label = label
        self.selected = False


class Screen4(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.count = 0
        self.switch = False
        self.x_option = 97
        self.y_option = 209
        self.drop_switch = False
        self.row = 0
        self.col = 0
        self.images = []
        self.files = []
        self.selected_files = []
        self.subjects = []
        self.window = window

        self.window.configure(bg="#83568a")
        self.canvas = Canvas(
            self,
            bg="#83568a",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage (file=f"resources/images/screen4/background.png")
        self.background = self.canvas.create_image (
            177.0, 86.0,
            image=self.background_img)

        self.img0 = PhotoImage (file=f"resources/images/screen4/img0.png")
        self.b0 = Label (
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b0.place (
            x=-10, y=228,
            width=339,
            height=749)

        self.img1 = PhotoImage (file=f"resources/images/screen4/img1.png")
        self.img1_hover = PhotoImage (file=f"resources/images/screen4/img1_hover.png")
        self.b1 = Label (
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b1.place (
            x=21, y=164,
            width=56,
            height=42)

        self.b1.bind ("<Button-1>", lambda e: self.animate ())

        self.img2 = PhotoImage (file=f"resources/images/screen4/img2.png")
        self.img2_hover = PhotoImage (file=f"resources/images/screen4/img2_hover.png")
        self.b2 = Button (
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b2.place (
            x=35, y=279,
            width=238,
            height=86)

        self.img3 = PhotoImage (file=f"resources/images/screen4/img3.png")
        self.img3_hover = PhotoImage (file=f"resources/images/screen4/img3_hover.png")
        self.b3 = Button (
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b3.place (
            x=33, y=405,
            width=238,
            height=86)

        self.img4 = PhotoImage (file=f"resources/images/screen4/img4.png")
        self.img4_hover = PhotoImage (file=f"resources/images/screen4/img4_hover.png")
        self.b4 = Button (
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b4.place (
            x=33, y=538,
            width=238,
            height=86)

        self.img5 = PhotoImage (file=f"resources/images/screen4/img5.png")
        self.img5_hover = PhotoImage (file=f"resources/images/screen4/img5_hover.png")
        self.b5 = Button (
            image=self.img5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b5.place (
            x=33, y=671,
            width=238,
            height=86)

        self.img6 = PhotoImage (file=f"resources/images/screen4/img6.png")
        self.img6_hover = PhotoImage (file=f"resources/images/screen4/img6_hover.png")
        self.b6 = Button (
            image=self.img6,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b6.place (
            x=33, y=798,
            width=238,
            height=86)

        self.img7 = PhotoImage (file=f"resources/images/screen4/img7.png")
        self.entry0_img = PhotoImage (file=f"resources/images/screen4/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image (
            213.0, 185.0,
            image=self.entry0_img)

        self.entry0 = Entry (
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.entry0.place (
            x=127.0, y=155,
            width=172.0,
            height=58)

        self.img9 = PhotoImage (file=f"resources/images/screen4/img9.png")
        self.img9_hover = PhotoImage (file=f"resources/images/screen4/img8_hover.png")
        self.b9 = Label (
            image=self.img9,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b9.place (
            x=318, y=153,
            width=62,
            height=62)

        self.b9.bind ("<Button-1>", lambda e: self.dropdown ())

        self.img10 = PhotoImage (file=f"resources/images/screen4/img10.png")
        self.img10_hover = PhotoImage (file=f"resources/images/screen4/img9_hover.png")
        self.b10 = Button (
            image=self.img10,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b10.place (
            x=1190, y=156,
            width=208,
            height=53)

        self.img11 = PhotoImage (file=f"resources/images/screen4/img11.png")
        self.img11_hover = PhotoImage (file=f"resources/images/screen4/img10_hover.png")
        self.b11 = Label (
            image=self.img11,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b11.place (
            x=952, y=155,
            width=208,
            height=53)

        self.img12 = PhotoImage(file=f"resources/images/screen4/img12.png")
        self.img12_hover = PhotoImage(file=f"resources/images/screen4/img11_hover.png")
        self.b12 = Label(
            image=self.img12,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b12.place(
            x=714, y=155,
            width=208,
            height=53)

        self.b12.bind("<Button-1>", lambda e: self.remove_selected_files())

        self.wrapper = LabelFrame(self.canvas, bg="#fff", highlightthickness=0, relief="flat")

        self.canvas2 = Canvas(
            self.wrapper,
            bg="#fff",
            height=703,
            width=969,
            bd=0,
            highlightthickness=0,
            relief="flat")
        self.canvas2.pack(side="left", fill="both", expand=True)

        self.vbar = ttk.Scrollbar(self.wrapper, orient=VERTICAL, command=self.canvas2.yview)
        self.vbar.pack(side=RIGHT, fill="y")

        self.canvas2.configure (yscrollcommand=self.vbar.set)
        self.canvas2.bind("<Configure>", lambda e: self.canvas2.configure(scrollregion=self.canvas2.bbox ("all")))

        self.myframe = Frame(self.canvas2, bg="#fff")
        self.canvas2.create_window((0, 0), window=self.myframe, anchor="nw")

        self.wrapper.place(x=405, y=241)

        self.b11.bind("<Button-1>", lambda e: self.file_dialogue(self.myframe))

        self.changeOnHoverButtons (self.b1, self.img1_hover, self.img1)
        self.changeOnHoverButtons (self.b2, self.img2_hover, self.img2)
        self.changeOnHoverButtons (self.b3, self.img3_hover, self.img3)
        self.changeOnHoverButtons (self.b4, self.img4_hover, self.img4)
        self.changeOnHoverButtons (self.b5, self.img5_hover, self.img5)
        self.changeOnHoverButtons (self.b6, self.img6_hover, self.img6)
        self.changeOnHoverButtons (self.b9, self.img9_hover, self.img9)
        self.changeOnHoverButtons (self.b10, self.img10_hover, self.img10)
        self.changeOnHoverButtons (self.b11, self.img11_hover, self.img11)
        self.changeOnHoverButtons (self.b12, self.img12_hover, self.img12)

        self.img14 = PhotoImage (file=f"resources/images/screen1/img4.png")
        self.img14_hover = PhotoImage (file=f"resources/images/screen1/img4_hover.png")
        self.b14 = Label (
            image=self.img14,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")
        self.b14.place (
            x=1393, y=0,
            width=48,
            height=37)

        self.img16 = PhotoImage (file=f"resources/images/screen1/img6.png")
        self.img16_hover = PhotoImage (file=f"resources/images/screen1/img6_hover.png")
        self.b16 = Label (
            image=self.img16,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")
        self.b16.place (
            x=1346, y=0,
            width=48,
            height=37)

        self.changeOnHoverButtons(self.b14, self.img14_hover, self.img14)
        self.changeOnHoverButtons(self.b16, self.img16_hover, self.img16)

        self.b14.bind("<Button-1>", lambda e: self.close())
        self.b16.bind("<Button-1>", lambda e: self.minimize())
        self.bind("<Map>", self.frame_mapped)


    def close(self):
        os._exit (0)

    def frame_mapped(self, e):
        self.window.update_idletasks()
        self.window.overrideredirect(True)
        self.window.state('normal')

    def minimize(self):
        self.window.update_idletasks ()
        self.window.overrideredirect (False)
        self.window.state('iconic')

    def changeOnHoverButtons(self, button, colorOnHover, colorOnLeave):
        button.bind ("<Enter>", func=lambda e: button.config(
            image=colorOnHover))
        button.bind ("<Leave>", func=lambda e: button.config(
            image=colorOnLeave))

    def remove_files(self):
        for child in self.myframe.winfo_children():
            child.destroy()

    def remove_selected_files(self):
        if len(self.selected_files) > 0:
            for child in self.selected_files:
                child.label.destroy()
            self.files = list(set(self.files) - set(self.selected_files))
            self.selected_files = []
            self.row = 0
            self.col = 0
            for file in self.files:
                file.label.grid(column=self.col % 4, row=self.row, padx=35, pady=20)
                self.col += 1
                if self.col % 4 == 0:
                    self.row += 1

    def file_dialogue(self, frame):
        name = filedialog.askopenfilename()
        if name != "":
            img = Image.open(name)
            img = img.resize((175, 248), Image.ANTIALIAS)
            photoImg = ImageTk.PhotoImage(img)
            self.images.append(photoImg)
            self.add_file(frame, os.path.basename(name).replace(".png", ".pdf"), self.images[len(self.images)-1])

    def add_file(self, frame, file_name, img):
        label = Label(frame,
                      image=img,
                      bg="white",
                      height=300,
                      width=175,
                      borderwidth=0,
                      highlightthickness=0,
                      compound='top',
                      text=f"{file_name}",
                      fg="blue")
        label.grid(column=self.col % 4, row=self.row, padx=35, pady=20)
        self.col += 1
        if self.col % 4 == 0:
            self.row += 1
        card = Card(label)
        self.changeOnHover(card)
        self.files.append(card)

    def select(self, button):
        button.unbind("<Leave>")
        button.config(bg="black")

    def unselect(self, button):
        button.config(bg="white")
        button.bind("<Leave>", func=lambda e: button.config(
            bg="white"))

    def clicked_file(self, card):
        card.selected = not card.selected
        if card.selected:
            self.select(card.label)
            self.selected_files.append(card)
        else:
            self.unselect(card.label)
            self.selected_files.remove(card)

    def changeOnHover(self, card):
        card.label.bind("<Enter>", func=lambda e: card.label.configure(
            bg="black"))
        card.label.bind("<Leave>", func=lambda e: card.label.configure(
            bg="white"))
        card.label.bind("<Button-1>", lambda e: self.clicked_file(card))

    def display(self):
        self.count -= 1
        xcor = self.b0.winfo_x()
        ycor = self.b0.winfo_y()
        xcor2 = self.b2.winfo_x()
        ycor2 = self.b2.winfo_y()
        xcor3 = self.b3.winfo_x()
        ycor3 = self.b3.winfo_y()
        xcor4 = self.b4.winfo_x()
        ycor4 = self.b4.winfo_y()
        xcor5 = self.b5.winfo_x()
        ycor5 = self.b5.winfo_y()
        xcor6 = self.b6.winfo_x()
        ycor6 = self.b6.winfo_y()
        if self.count > 0 and not self.switch:
            self.b0.place(x=xcor + 4.8, y=ycor)
            self.b2.place(x=xcor2 + 4.8, y=ycor2)
            self.b3.place(x=xcor3 + 4.8, y=ycor3)
            self.b4.place(x=xcor4 + 4.8, y=ycor4)
            self.b5.place(x=xcor5 + 4.8, y=ycor5)
            self.b6.place(x=xcor6 + 4.8, y=ycor6)
            display_event = self.window.after(10, self.display)

    def hide(self):
        self.count += 1
        xcor = self.b0.winfo_x()
        ycor = self.b0.winfo_y()
        xcor2 = self.b2.winfo_x()
        ycor2 = self.b2.winfo_y()
        xcor3 = self.b3.winfo_x()
        ycor3 = self.b3.winfo_y()
        xcor4 = self.b4.winfo_x()
        ycor4 = self.b4.winfo_y()
        xcor5 = self.b5.winfo_x()
        ycor5 = self.b5.winfo_y()
        xcor6 = self.b6.winfo_x()
        ycor6 = self.b6.winfo_y()
        if self.count < 70 and self.switch:
            self.b0.place(x=xcor - 5, y=ycor)
            self.b2.place(x=xcor2 - 5, y=ycor2)
            self.b3.place(x=xcor3 - 5, y=ycor3)
            self.b4.place(x=xcor4 - 5, y=ycor4)
            self.b5.place(x=xcor5 - 5, y=ycor5)
            self.b6.place(x=xcor6 - 5, y=ycor6)
            hide_event = self.window.after(10, self.hide)

    def animate_up(self, button):
        xcor = button.winfo_x()
        ycor = button.winfo_y()
        if ycor != 209:
            button.place(x=xcor, y=ycor-1)
            self.window.after(5, self.animate, button)

    def animate(self):
        self.switch = not self.switch
        if self.switch:
            self.hide()
        else:
            self.display()

    def drop(self):
        xcor = self.x_option
        ycor = self.y_option
        for i in range(0, len(self.subjects)):
            self.subjects[i].place(x=xcor, y=ycor)
            ycor += 60

    def up(self):
        for i in range(0, len(self.subjects)):
            self.subjects[i].place_forget()

    def dropdown(self):
        self.drop_switch = not self.drop_switch
        if self.drop_switch:
            self.drop()
        else:
            self.up()

    def add_option(self):
        option = Label(
            image=self.img7,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            width=220,
            height=60)

        self.subjects.append(option)

