from tkinter import *
from tkinter.ttk import Combobox

count = 0
switch = False
x_option = 97
y_option = 209
drop_switch = False

def display():
    global count, switch
    count -= 1
    xcor = b0.winfo_x()
    ycor = b0.winfo_y()
    xcor2 = b2.winfo_x()
    ycor2 = b2.winfo_y()
    xcor3 = b3.winfo_x()
    ycor3 = b3.winfo_y()
    xcor4 = b4.winfo_x()
    ycor4 = b4.winfo_y()
    xcor5 = b5.winfo_x()
    ycor5 = b5.winfo_y()
    xcor6 = b6.winfo_x()
    ycor6 = b6.winfo_y()
    if count > 0 and not switch:
        b0.place(x=xcor + 4.8, y=ycor)
        b2.place(x=xcor2 + 4.8, y=ycor2)
        b3.place(x=xcor3 + 4.8, y=ycor3)
        b4.place(x=xcor4 + 4.8, y=ycor4)
        b5.place(x=xcor5 + 4.8, y=ycor5)
        b6.place(x=xcor6 + 4.8, y=ycor6)
        display_event = window.after(10, display)
    print(count)

def hide():
    global count, switch
    count += 1
    xcor = b0.winfo_x()
    ycor = b0.winfo_y()
    xcor2 = b2.winfo_x()
    ycor2 = b2.winfo_y()
    xcor3 = b3.winfo_x()
    ycor3 = b3.winfo_y()
    xcor4 = b4.winfo_x()
    ycor4 = b4.winfo_y()
    xcor5 = b5.winfo_x()
    ycor5 = b5.winfo_y()
    xcor6 = b6.winfo_x()
    ycor6 = b6.winfo_y()
    if count < 70 and switch:
        b0.place(x=xcor - 5, y=ycor)
        b2.place(x=xcor2 - 5, y=ycor2)
        b3.place(x=xcor3 - 5, y=ycor3)
        b4.place(x=xcor4 - 5, y=ycor4)
        b5.place(x=xcor5 - 5, y=ycor5)
        b6.place(x=xcor6 - 5, y=ycor6)
        hide_event = window.after(10, hide)
    print(count)

def animate_up(button):
    xcor = button.winfo_x()
    ycor = button.winfo_y()
    if ycor != 209:
        button.place(x=xcor, y=ycor-1)
        window.after(5, animate, button)


def animate():
    global switch
    switch = not switch
    if switch:
        hide()
    else:
        display()


options = []


def drop():
    global options, x_option, y_option
    xcor = x_option
    ycor = y_option
    for i in range(0, len(options)):
        options[i].place(x=xcor, y=ycor)
        ycor += 60

def up():
    for i in range(0, len(options)):
        options[i].place_forget()


def dropdown():
    global drop_switch
    drop_switch = not drop_switch
    if drop_switch:
        drop()
    else:
        up()

def add_option():
    global options, x_option, y_option
    option = Button(
        image=img7,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        width=220,
        height=60)

    options.append(option)


window = Tk()

window.geometry ("1440x1024")
window.configure (bg="#83568a")
canvas = Canvas (
    window,
    bg="#83568a",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place (x=0, y=0)

background_img = PhotoImage (file=f"../resources/images/screen4/background.png")
background = canvas.create_image(
    177.0, 86.0,
    image=background_img)

img0 = PhotoImage (file=f"../resources/images/screen4/img0.png")
b0 = Label(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

b0.place(
    x=-10, y=228,
    width=339,
    height=749)

img1 = PhotoImage(file=f"../resources/images/screen4/img1.png")
b1 = Label(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

b1.place(
    x=21, y=164,
    width=56,
    height=42)

funcid = b1.bind("<Button-1>", lambda e: animate())

img2 = PhotoImage (file=f"../resources/images/screen4/img2.png")
b2 = Button (
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

b2.place (
    x=35, y=279,
    width=238,
    height=86)

img3 = PhotoImage (file=f"../resources/images/screen4/img3.png")
b3 = Button (
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

b3.place (
    x=33, y=405,
    width=238,
    height=86)

img4 = PhotoImage (file=f"../resources/images/screen4/img4.png")
b4 = Button (
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

b4.place (
    x=33, y=538,
    width=238,
    height=86)

img5 = PhotoImage (file=f"../resources/images/screen4/img5.png")
b5 = Button (
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

b5.place (
    x=33, y=671,
    width=238,
    height=86)

img6 = PhotoImage (file=f"../resources/images/screen4/img6.png")
b6 = Button (
    image=img6,
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

b6.place (
    x=33, y=798,
    width=238,
    height=86)

img7 = PhotoImage(file = f"../resources/images/screen4/img7.png")
add_option()
add_option()
entry0_img = PhotoImage(file = f"../resources/images/screen4/img_textBox0.png")
entry0_bg = canvas.create_image(
    213.0, 185.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 127.0, y = 155,
    width = 172.0,
    height = 58)


img9 = PhotoImage (file=f"../resources/images/screen4/img9.png")
b9 = Button (
    image=img9,
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

b9.place(
    x=318, y=153,
    width=62,
    height=62)

b9.bind("<Button-1>", lambda e: dropdown())

img10 = PhotoImage(file=f"../resources/images/screen4/img10.png")
b10 = Button(
    image=img10,
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

b10.place (
    x=1190, y=156,
    width=208,
    height=53)

img11 = PhotoImage(file=f"../resources/images/screen4/img11.png")
b11 = Button(
    image=img11,
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

b11.place(
    x=952, y=155,
    width=208,
    height=53)

window.resizable(False, False)
window.mainloop()
