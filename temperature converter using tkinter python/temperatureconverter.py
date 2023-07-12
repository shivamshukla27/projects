import tkinter
from tkinter import messagebox
from functools import partial

temp_Val = "Celsius"

def store_temp(set_temp):
    global temp_Val
    temp_Val = set_temp

def call_convert(rlabel, inputn):
    temp = inputn.get()
    if temp_Val == "Celsius":
        f = float((float(temp)*9/5)+32)
        rlabel.config(text = "%.1f Fahrenheit"%f)
        messagebox.showinfo("Temperature Converter","Successfully Converted to Fahrenheit " , )

    if temp_Val == 'Fahrenheit':
        c = float((float(temp)-32)*5/9)
        rlabel.config(text = "%.1f Celsius" % c)
        messagebox.showinfo("Temperature Converter","Successfully Converted to Fahrenheit ")
    return

top = tkinter.Tk()
top.geometry('300x150+600+200')
top.title('Temperatuer Converter')
top.grid_columnconfigure(1, weight = 1)
top.grid_rowconfigure(1, weight = 1)

inputNumber = tkinter.StringVar()
var = tkinter.StringVar()

input_label = tkinter.Label(top, text ="Enter temperture")
input_entry = tkinter.Entry(top, textvariable = inputNumber)
input_label.grid(row = 1)
input_entry.grid(row = 1, column = 1)
result_label = tkinter.Label(top)
result_label.grid(row = 3, column = 2)

dropDownList = ["Celsius", "Fahrenheit"]
drop_down = tkinter.OptionMenu(top, var, *dropDownList, command = store_temp)
var.set(dropDownList[0])
drop_down.grid(row = 1, column = 2)

call_convert = partial(call_convert, result_label, inputNumber)
result_button = tkinter.Button(top, text ="Convert", command = call_convert)
result_button.grid(row = 2, columnspan = 2)
top.mainloop()