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
win.title("Simple Calculator")
win.geometry("2568x2025")

frame = tk.Frame(win)
frame.pack(pady=20)

x = tk.Entry(frame)
x.pack(side = tk.TOP, padx = 100)

operations = ttk.Combobox(frame, values = ["+", "-", "*", "/", "%"])
operations.pack(side = tk.TOP, padx = 5)

y = tk.Entry(frame)
y.pack(side = tk.TOP, padx = 5)

submit_button = tk.Button(frame, text="Submit", command=calculator)
submit_button.pack(side = tk.TOP, padx = 5)

result = tk.StringVar()
result_label = tk.Label(frame, textvariable=result)
result_label.pack(side = tk.TOP, padx = 5)

win.mainloop()