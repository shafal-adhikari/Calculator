from tkinter import *

root = Tk()
root.geometry("250x400+100+100")
root.resizable(0,0)
root.title("Calculator")

val = ""

data = StringVar()

def press(k):
    global val
    val = val + str(k)
    data.set(val)

def clear():
    global val
    val = ""
    data.set(val)

def result():
    global val
    try:
        result = eval(val)
        data.set(result)
    except:
        data.set('Error')

lbl = Label(
    root,
    font = ("Verdana", 20),
    anchor=SE,
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both")

# the frames section
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


# The buttons section
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: press(1),
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: press(2),
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: press(3),
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda:press("+"),
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)

# buttons for frame 2

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: press(4),
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: press(5),
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: press(6),
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda:press("-"),
)
btnminus.pack(side = LEFT, expand = True, fill = "both",)

# button for frame 3

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: press(7),
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: press(8),
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: press(9),
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda:press("*"),
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)

btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    bg="#e31429",
    border = 0,
    command = clear,
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: press(0),
)
btn0.pack(side = LEFT, expand = True, fill = "both",)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda:press("/"),
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)

root.mainloop()
