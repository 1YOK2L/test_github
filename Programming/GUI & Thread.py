import tkinter as tk
from tkinter import ttk
import threading
import time

def calculator():
    try:
        time.sleep(3)

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
win.title("Simple Calculator")

frame = tk.Frame(win)
frame.pack(padx = 20, pady = 20)

x = tk.Entry(frame)
x.grid(row = 0, column = 0, padx = 5, pady = 5)

operations = ttk.Combobox(frame, values = ["+", "-", "*", "/", "%"])
operations.grid(row = 0, column = 1, padx = 5, pady = 5)

y = tk.Entry(frame)
y.grid(row = 0, column = 2, padx = 5, pady = 5)

submit_button = tk.Button(frame, text="Submit", command=calculator)
submit_button.grid(row = 0, column = 3, padx = 5, pady = 5)

result = tk.StringVar()
result_label = tk.Label(frame, textvariable=result)
result_label.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)

win.mainloop()