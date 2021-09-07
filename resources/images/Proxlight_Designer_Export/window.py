from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#83568a")
canvas = Canvas(
    window,
    bg = "#83568a",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    312.0, 382.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry0.place(
    x = 163.0, y = 358,
    width = 298.0,
    height = 47)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    536.0, 646.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry1.place(
    x = 522.0, y = 622,
    width = 28.0,
    height = 46)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    536.0, 474.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry2.place(
    x = 522.0, y = 451,
    width = 28.0,
    height = 44)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    549.5, 383.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry3.place(
    x = 514.0, y = 360,
    width = 71.0,
    height = 45)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    673.5, 383.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry4.place(
    x = 638.0, y = 360,
    width = 71.0,
    height = 45)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    536.0, 560.0,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry5.place(
    x = 522.0, y = 538,
    width = 28.0,
    height = 42)

entry6_img = PhotoImage(file = f"img_textBox6.png")
entry6_bg = canvas.create_image(
    536.0, 728.0,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry6.place(
    x = 522.0, y = 707,
    width = 28.0,
    height = 40)

entry7_img = PhotoImage(file = f"img_textBox7.png")
entry7_bg = canvas.create_image(
    1249.0, 560.0,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry7.place(
    x = 1237.0, y = 538,
    width = 24.0,
    height = 42)

entry8_img = PhotoImage(file = f"img_textBox8.png")
entry8_bg = canvas.create_image(
    1249.0, 648.5,
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry8.place(
    x = 1237.0, y = 627,
    width = 24.0,
    height = 41)

entry9_img = PhotoImage(file = f"img_textBox9.png")
entry9_bg = canvas.create_image(
    1249.0, 729.5,
    image = entry9_img)

entry9 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry9.place(
    x = 1237.0, y = 705,
    width = 24.0,
    height = 47)

entry10_img = PhotoImage(file = f"img_textBox10.png")
entry10_bg = canvas.create_image(
    312.0, 472.5,
    image = entry10_img)

entry10 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry10.place(
    x = 163.0, y = 448,
    width = 298.0,
    height = 47)

entry11_img = PhotoImage(file = f"img_textBox11.png")
entry11_bg = canvas.create_image(
    312.0, 562.0,
    image = entry11_img)

entry11 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry11.place(
    x = 163.0, y = 538,
    width = 298.0,
    height = 46)

entry12_img = PhotoImage(file = f"img_textBox12.png")
entry12_bg = canvas.create_image(
    312.0, 645.5,
    image = entry12_img)

entry12 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry12.place(
    x = 163.0, y = 621,
    width = 298.0,
    height = 47)

entry13_img = PhotoImage(file = f"img_textBox13.png")
entry13_bg = canvas.create_image(
    312.0, 729.5,
    image = entry13_img)

entry13 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry13.place(
    x = 163.0, y = 705,
    width = 298.0,
    height = 47)

entry14_img = PhotoImage(file = f"img_textBox14.png")
entry14_bg = canvas.create_image(
    1036.0, 382.5,
    image = entry14_img)

entry14 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry14.place(
    x = 887.0, y = 358,
    width = 298.0,
    height = 47)

entry15_img = PhotoImage(file = f"img_textBox15.png")
entry15_bg = canvas.create_image(
    1036.0, 472.5,
    image = entry15_img)

entry15 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry15.place(
    x = 887.0, y = 448,
    width = 298.0,
    height = 47)

entry16_img = PhotoImage(file = f"img_textBox16.png")
entry16_bg = canvas.create_image(
    1036.0, 562.5,
    image = entry16_img)

entry16 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry16.place(
    x = 887.0, y = 538,
    width = 298.0,
    height = 47)

entry17_img = PhotoImage(file = f"img_textBox17.png")
entry17_bg = canvas.create_image(
    1036.0, 648.5,
    image = entry17_img)

entry17 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry17.place(
    x = 887.0, y = 624,
    width = 298.0,
    height = 47)

entry18_img = PhotoImage(file = f"img_textBox18.png")
entry18_bg = canvas.create_image(
    1036.0, 731.5,
    image = entry18_img)

entry18 = Entry(
    bd = 0,
    bg = "#dfdfdf",
    highlightthickness = 0)

entry18.place(
    x = 887.0, y = 707,
    width = 298.0,
    height = 47)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 892, y = 890,
    width = 209,
    height = 62)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 1140, y = 890,
    width = 209,
    height = 62)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    653.0, 492.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
