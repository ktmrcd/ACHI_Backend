from tkinter import *


def btn_clicked():
    print("Button Clicked")


frame3 = Tk()

frame3.geometry("1280x720")
frame3.configure(bg = "#ffffff")
f3_canvas = Canvas(
    frame3,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f3_canvas.place(x = 0, y = 0)

f3_background_img = PhotoImage(file = f"f3-background.png")
f3_background = f3_canvas.create_image(
    640.0, 517.5,
    image=f3_background_img)

#RED
# f3_canvas.create_rectangle(
#     263, 310, 263+378, 310+50,
#     fill = "#ff0000",
#     outline = "")
label_frame= Label(frame3, text="", bg = "white")
label_frame.place(x=263, y=310,
    width = 378,
    height = 50)
label_di= Label(label_frame, text="Malaria", bg = "white")
label_di.config(font=('Raleway', 32, 'bold'), justify=LEFT)
label_di.pack(side= TOP, anchor="w")

#BLUE
# f3_canvas.create_rectangle(
#     252, 429, 252+741, 429+145,
#     fill = "#00b6a0",
#     outline = "")
label_frame1= Label(frame3, text="", bg = "white")
label_frame1.place(x=252, y=429,
    width = 741,
    height = 145)
label_di= Label(label_frame1, text="JNFVKJDFVNKSDJF\nJSDFKAJSDFKSAD", bg = "white")
label_di.config(font=('Raleway', 11), justify=LEFT)
label_di.pack(side= TOP, anchor="w")

#PINK
# f3_canvas.create_rectangle(
#     765, 316, 765+182, 316+44,
#     fill = "#ff0099",
#     outline = "")
label_ac= Label(frame3, text="Very Likely", bg = "white")
label_ac.config(font=('Raleway', 16))
label_ac.place(x=765, y=316,
    width = 182,
    height = 44)

frame3.resizable(False, False)
frame3.mainloop()
