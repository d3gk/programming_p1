
from tkinter import *
from tkinter import ttk
import numpy as np

MainWindow = Tk()

MainWindow.title('SIN/COS Calculator')

MainWindow.geometry('300x100')

UsrInput = StringVar()
UsrOperFormat = StringVar()
UsrOperFunc = StringVar()
OverallResult = StringVar()
UsrOperFormat.set('rad')
UsrOperFunc.set('sin')

def rb_clicked(el):
    global UsrOperFunc
    global UsrOperFormat
    global OverallResult
        global UsrInput
    if (UsrInput.get() == ''):
        return
    try:
        inp = float(UsrInput.get())
    except:
        return
    oper = UsrOperFormat.get()
    func = UsrOperFunc.get()
    if (func == 'sin'):
        if (oper == 'deg'):
            OverallResult.set(np.sin(np.deg2rad(inp)))
        else:
            OverallResult.set(np.sin(inp))
    else:
        if (oper == 'deg'):
            OverallResult.set(np.cos(np.deg2rad(inp)))
        else:
            OverallResult.set(np.cos(inp))

input_field = Entry(master=MainWindow, textvariable=UsrInput)
rb_rad = Radiobutton(master=MainWindow, command=lambda: rb_clicked('rb_rad'), variable=UsrOperFormat, value='rad', text="RAD")
rb_deg = Radiobutton(master=MainWindow, command=lambda: rb_clicked('rb_deg'), variable=UsrOperFormat, value='deg', text="DEG")
rb_sin = Radiobutton(master=MainWindow, command=lambda: rb_clicked('rb_sin'), variable=UsrOperFunc, value='sin', text="SIN")
rb_cos = Radiobutton(master=MainWindow, command=lambda: rb_clicked('rb_cos'), variable=UsrOperFunc, value='cos', text="COS")
l_res = Label(master=MainWindow, textvariable=OverallResult)
rb_rad.grid(column=0, row=1)
rb_deg.grid(column=1, row=1)
rb_sin.grid(column=0, row=2)
rb_cos.grid(column=1, row=2)
input_field.grid(column=0, row=0)
l_res.grid(column=0, row=3)
MainWindow.mainloop()