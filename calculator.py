from tkinter import *

# function section

calculation = ''

def add_to_calculation(value):
    global calculation
    calculation += value
    textbox.delete(1.0, END)
    textbox.insert(1.0, calculation)

def evaluate_calculation():
    global calculation

    try:
        calculation = str(eval(calculation)) 
        textbox.delete(1.0, END)
        textbox.insert(1.0, calculation)    
    except:
        clear_field()
        textbox.insert(1.0, 'ERROR')
        
def clear_field():
    global calculation
    calculation = ''
    textbox.delete(1.0, END)

def backspace_handler():
    global calculation
    calculation = calculation[:-1]
    textbox.delete(1.0, END)
    textbox.insert(1.0, calculation)








# window section

window = Tk()
window.config(bg='white')
window.geometry('600x400+50+50')
window.title('Calculator')

# textbox section

textbox = Text(window, height=2, font=('Arial', 12))
textbox.pack(padx=10)

buttonframe = Frame()
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)


# 1st row
open = Button(buttonframe, text='(', font=('Arial', 12), command=lambda: add_to_calculation('('))
open.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

close = Button(buttonframe, text=')', font=('Arial', 12), command=lambda: add_to_calculation(')'))
close.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

clearAll = Button(buttonframe, text='CA', font=('Arial', 12), command= clear_field)
clearAll.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)

backspace = Button(buttonframe, text='<', font=('Arial', 12), command=backspace_handler)
backspace.grid(row=0, column=3, sticky='nsew', padx=5, pady=5)



# 2nd row
btn1 = Button(buttonframe, text='1', font=('Arial', 12), command=lambda: add_to_calculation('1'))
btn1.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

btn2 = Button(buttonframe, text='2', font=('Arial', 12), command=lambda: add_to_calculation('2'))
btn2.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

btn3 = Button(buttonframe, text='3', font=('Arial', 12), command=lambda: add_to_calculation('3'))
btn3.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

div = Button(buttonframe, text='/', font=('Arial', 12), command=lambda: add_to_calculation('/'))
div.grid(row=1, column=3, sticky='nsew', padx=5, pady=5)

# 3rd row
btn4 = Button(buttonframe, text='4', font=('Arial', 12), command=lambda: add_to_calculation('4'))
btn4.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)

btn5 = Button(buttonframe, text='5', font=('Arial', 12), command=lambda: add_to_calculation('5'))
btn5.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)

btn6 = Button(buttonframe, text='6', font=('Arial', 12), command=lambda: add_to_calculation('6'))
btn6.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)

minus = Button(buttonframe, text='-', font=('Arial', 12), command=lambda: add_to_calculation('-'))
minus.grid(row=2, column=3, sticky='nsew', padx=5, pady=5)

#4th

btn7 = Button(buttonframe, text='7', font=('Arial', 12), command=lambda: add_to_calculation('7'))
btn7.grid(row=3, column=0, sticky='nsew', padx=5, pady=5)

btn8 = Button(buttonframe, text='8', font=('Arial', 12), command=lambda: add_to_calculation('8'))
btn8.grid(row=3, column=1, sticky='nsew', padx=5, pady=5)

btn9 = Button(buttonframe, text='9', font=('Arial', 12), command=lambda: add_to_calculation('9'))
btn9.grid(row=3, column=2, sticky='nsew', padx=5, pady=5)

plus = Button(buttonframe, text='+', font=('Arial', 12), command=lambda: add_to_calculation('+'))
plus.grid(row=3, column=3, sticky='nsew', padx=5, pady=5)

# 5th row
zero = Button(buttonframe, text='0', font=('Arial', 12), command=lambda: add_to_calculation('0'))
zero.grid(row=4, column=0, sticky='nsew', padx=5, pady=5)

dot = Button(buttonframe, text='.', font=('Arial', 12), command=lambda: add_to_calculation('.'))
dot.grid(row=4, column=1, sticky='nsew', padx=5, pady=5)

mul = Button(buttonframe, text='*', font=('Arial', 12), command=lambda: add_to_calculation('*'))
mul.grid(row=4, column=2, sticky='nsew', padx=5, pady=5)

equal = Button(buttonframe, text='=', font=('Arial', 12), command=evaluate_calculation)
equal.grid(row=4, column=3, sticky='nsew', padx=5, pady=5)
 
buttonframe.pack(padx=10, pady=10, fill='both', expand=True)


window.mainloop()