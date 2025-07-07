import tkinter as tk
from tkinter import ttk
import threading
import time

my_list = [0, 2, 5, 7, 10, 13, 15, 18, 21, 23, 26, 28, 31, 34, 36, 39, 42, 44, 47, 50, 52, 55, 57, 60, 63, 65, 68, 71, 73, 76, 78, 81, 84, 86, 89, 92, 94, 97, 100]

def update(percentage_index):
    loading.config(text = f"Calculating... ({my_list[percentage_index]}%)")
    if percentage_index < len(my_list) - 1:
        win.after(60, update, percentage_index + 1)

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
    loading.grid_forget()
    result_label.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)

def begin_calculation():
    loading.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
    result_label.grid_forget()
    update(0)
    calculation_thread = threading.Thread(target=calculator)
    calculation_thread.start()

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

submit_button = tk.Button(frame, text = "Submit", command = begin_calculation)
submit_button.grid(row = 0, column = 3, padx = 5, pady = 5)

loading = tk.Label(frame, text = "Calculating...")

result = tk.StringVar()
result_label = tk.Label(frame, textvariable = result)
result_label.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)

win.mainloop()