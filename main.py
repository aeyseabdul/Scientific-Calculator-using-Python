import math
import tkinter as tk
from tkinter import *
from math import *
operator = ""

def digitclick(numbers):
    global operator
    operator = operator + str(numbers)
    input.set(operator)

def sin():
    global operator
    if operator=="":
        input.set('select value first')
    else:
        operator=float(operator)
        ans=math.sin(math.radians(operator))
        input.set(ans)
        operator=""

def cos():
    global operator
    if operator=="":
        input.set('select value first')
    else:
        operator=float(operator)
        ans=math.cos(math.radians(operator))
        input.set(ans)
        operator=""

def tan():
    global operator
    if operator=="":
        input.set('select value first')
    else:
        operator=float(operator)
        ans=math.tan(math.radians(operator))
        input.set(ans)
        operator=""

def sqrt():
    global operator
    if operator == "":
        input.set('select value first')
    else:
        operator = float(operator)
        ans = math.sqrt(operator)
        input.set(ans)
        operator = ""

def cube():
    global operator
    if operator == "":
        input.set('select value first')
    else:
        operator = int(operator)
        ans = operator**3
        input.set(ans)
        operator = ""

def sq():
    global operator
    if operator == "":
        input.set('select value first')
    else:
        operator = int(operator)
        ans = operator ** 2
        input.set(ans)
        operator = ""

def inverse():
    global operator
    if operator == "":
        input.set('select value first')
    else:
        operator = int(operator)
        ans = operator ** -1
        input.set(ans)
        operator = ""

def clr():
    global operator
    operator = ""
    input.set("")

def equal():
    global operator
    try:
        answer = str(eval(operator))
        input.set(answer)
        operator=""
    except ZeroDivisionError:
        input.set('Undefined')
        operator=""
    except SyntaxError:
        input.set('Syntax Error')
        operator=""

def back():
    global operator
    operator=operator[:-1]
    input.set(operator)


calc = tk.Tk()
calc.title('Calculator')
calc.config(bg='#E6E6E6')
## Add your Directory below for icon
calc.iconbitmap("yourdirectory\calc.ico")
calc.resizable(False, False)
calc.config(bg='#dddddd')
input=StringVar()
display = Entry(calc, textvariable=input, font=('Poppins', 20), justify=RIGHT).grid(columnspan=5,pady=10)

sin=tk.Button(calc, text="sin",command=sin, width=9,font=('Poppins',10),relief='flat',activebackground='#dadbdd').grid(row=2, column=1,pady=3)
cos=tk.Button(calc, text="cos",command=cos, width=9,font=('Poppins',10),relief='flat',activebackground='#dadbdd').grid(row=2, column=2)
tan=tk.Button(calc, text="tan",command=tan, width=9,font=('Poppins',10),relief='flat',activebackground='#dadbdd').grid(row=2, column=3)
back=tk.Button(calc, text="Delete",command=back, width=9,font=('Poppins',10),relief='flat',activebackground='#dadbdd').grid(row=2, column=4)

sqrt=tk.Button(calc, text="√",command=sqrt, width=9,font=('Poppins',10),relief='flat',activebackground='#dadbdd').grid(row=3, column=1,pady=3)
cube=tk.Button(calc, text="x³",command=cube, width=9,font=('Poppins',10),relief='flat',activebackground='#dadbdd').grid(row=3, column=2)
sq=tk.Button(calc, text="x²",command=sq, width=9,font=('Poppins',10),relief='flat',activebackground='#dadbdd').grid(row=3, column=3)
inverse=tk.Button(calc, text="¹⁄ₓ",command=inverse, width=9,font=('Poppins',10),relief='flat',activebackground='#dadbdd').grid(row=3, column=4)

btn7 = tk.Button(calc, text="7",command=lambda:digitclick(7), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=4, column=1,pady=3)
btn8 = tk.Button(calc, text="8",command=lambda:digitclick(8), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=4, column=2)
btn9 = tk.Button(calc, text="9",command=lambda:digitclick(9), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=4, column=3)
Add = tk.Button(calc, text="+",command=lambda:digitclick('+'), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=4, column=4)


btn4 = tk.Button(calc, text="4",command=lambda:digitclick(4), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=5, column=1,pady=3)
btn5 = tk.Button(calc, text="5",command=lambda:digitclick(5), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=5, column=2)
btn6 = tk.Button(calc, text="6",command=lambda:digitclick(6), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=5, column=3)
Sub = tk.Button(calc, text="-",command=lambda:digitclick('-'), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=5, column=4)

btn1 = tk.Button(calc, text="1",command=lambda:digitclick(1), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=6, column=1,pady=3)
btn2 = tk.Button(calc, text="2",command=lambda:digitclick(2), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=6, column=2)
btn3 = tk.Button(calc, text="3",command=lambda:digitclick(3), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=6, column=3)
Multiply = tk.Button(calc, text="X",command=lambda:digitclick('*'), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=6, column=4)

btn0 = tk.Button(calc, text="0",command=lambda:digitclick(0), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=7, column=1,pady=3)
BrkOpen = tk.Button(calc, text="(",command=lambda:digitclick('('), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=7, column=2)
BrkClose = tk.Button(calc, text=")",command=lambda:digitclick(')'), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=7, column=3)
Divide = tk.Button(calc, text="/",command=lambda:digitclick('/'), width=6, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=7, column=4)

Clear = tk.Button(calc, text="C",command=clr, width=13, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=8, column=1,columnspan=2,pady=3)
Equal = tk.Button(calc, text="=",command=equal, width=13, font=('Poppins',15),relief='flat',activebackground='#dadbdd').grid(row=8, column=3,columnspan=2)


calc.mainloop()
