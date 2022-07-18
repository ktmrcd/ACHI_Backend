from tkinter import *


def btn_clicked():
    print("Button Clicked")


frame2 = Tk()

frame2.geometry("1280x720")
frame2.configure(bg = "#ffffff")
f2_canvas = Canvas(
    frame2,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f2_canvas.place(x = 0, y = 0)

f2_background_img = PhotoImage(file = f"f2-background.png")
f2_background = f2_canvas.create_image(
    640.0, 522.5,
    image=f2_background_img)

f2_canvas.create_rectangle(
    255, 307, 255+772, 307+258,
    fill = "#d9d9d9",
    outline = "")

label_symp= Label(frame2, text="", bg = "white")
label_symp.config(font=('Raleway', 16, 'bold'))
label_symp.place(x=255, y=307,
    width = 772,
    height = 258)

f2_img0 = PhotoImage(file = f"f2-img0.png")
f2_b0 = Button(frame2,
    image = f2_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

f2_b0.place(
    x = 944, y = 630,
    width = 157,
    height = 61)

frame2.resizable(False, False)
frame2.mainloop()
