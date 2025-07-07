import tkinter as tk
from tkinter import ttk

def calculator():
    try:
        num1 = float(x.get())
        num2 = float(y.get())

        operation = operations.get()
        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            try:
                result.set(num1 / num2)
            except ZeroDivisionError:
                result.set("Error: num1 cannot be divided by 0")
        elif operation == "%":
            try:
                result.set(num1 % num2)
            except ZeroDivisionError:
                result.set("Error: Cannot find remainder")
    except ValueError:
        result.set("Invalid input")
win = tk.Tk()
win.title("Calculator")

frame = tk.Frame(win)
frame.pack(pady=20)

x = tk.Entry(frame)
x.grid(row = 0, column = 0, sticky = 'w', pady = 2)

operations = ttk.Combobox(frame, values = ["+", "-", "*", "/", "%"])
operations.grid(row = 0, column = 1, sticky = 'w', pady = 2)

y = tk.Entry(frame)
y.grid(row = 0, column = 2, sticky = 'w', pady = 2)

submit_button = tk.Button(frame, text="Submit", command=calculator)
y.grid(row = 0, column = 3, sticky = 'w', pady = 2)

result = tk.StringVar()
result_label = tk.Label(frame, textvariable=result)
result_label.grid(row = 0, column = 4, sticky = 'w', pady = 2)

win.mainloop()