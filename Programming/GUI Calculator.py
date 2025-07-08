import tkinter as tk
from tkinter import ttk
import threading
import time
from math import *

# Simulated loading steps
my_list = [0, 2, 5, 7, 10, 13, 15, 18, 21, 23, 26, 28, 31, 34, 36, 39, 42, 44, 47, 50, 52, 55, 57, 60, 63, 65, 68, 71, 73, 76, 78, 81, 84, 86, 89, 92, 94, 97, 100]

def update(percentage_index):
    loading.config(text = f"Calculating... ({my_list[percentage_index]}%)")
    if percentage_index < len(my_list) - 1:
        win.after(60, update, percentage_index + 1)

def calculator():
    try:
        time.sleep(3)
        num1 = float(x.get())
        operation = operations.get()

        # Check if this operation needs num2
        binary_ops = ["+", "-", "*", "/", "%", "**", "<", ">", "<=", ">=", "log", "nCr", "nPr", "right triangle area", "pyramid volume", "cone volume", "oval area"]
        if operation in binary_ops:
            num2 = float(y.get())

        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            result.set(num1 / num2 if num2 != 0 else "ZeroDivisionError: division by zero")
        elif operation == "%":
            result.set(num1 % num2 if num2 != 0 else "ZeroDivisionError: division by zero")
        elif operation == "**":
            result.set(num1 ** num2)
        elif operation == "<":
            result.set(f"{num1} is less than {num2}." if num1 < num2 else f"{num1} is not less than {num2}.")
        elif operation == ">":
            result.set(f"{num1} is greater than {num2}." if num1 > num2 else f"{num1} is not greater than {num2}.")
        elif operation == "<=":
            result.set(f"{num1} is either less than or equal to {num2}." if num1 <= num2 else f"{num1} is neither less than nor equal to {num2}.")
        elif operation == ">=":
            result.set(f"{num1} is either greater than or equal to {num2}." if num1 >= num2 else f"{num1} is neither greater than nor equal to {num2}.")
        elif operation == "sqrt (num1 only)":
            result.set(sqrt(num1) if num1 >= 0 else "ValueError: math domain error")
        elif operation == "cbrt (num1 only)":
            result.set(cbrt(num1))
        elif operation == "|x| (num1 only)":
            result.set(fabs(num1))
        elif operation == "! (num1 only)":
            try:
                if not num1.is_integer():
                    result.set("TypeError: 'float' object cannot be interpreted as an integer")
                elif num1 < 0:
                    result.set("ValueError: factorial() not defined for negative values")
                else:
                    result.set(factorial(int(num1)))
            except (ValueError, TypeError) as e:
                result.set(f"{type(e).__name__}: {e}")
        elif operation == "odd/even (num1 only)":
            if num1.is_integer():
                if num1 % 2 == 0:
                    result.set(f"{int(num1)} is an even number")
                else:
                    result.set(f"{int(num1)} is an odd number")
            else:
                result.set("Indeterminate")
        elif operation == "prime/composite (num1 only)":
            if num1.is_integer():
                num1 = int(num1)
                prime = True
                for i in range (2, num1):
                    if num1 % i == 0:
                        result.set(f"{num1} is composite")
                        prime = False
                        break
                if num1 <= 1:
                    result.set("Indeterminate")
                elif prime == True:
                    result.set(f"{num1} is prime")
            else:
                result.set("Indeterminate")
        elif operation == "log":
            if num1 > 0 and num2 > 0 and num2 != 1:
                result.set(log(num1, num2))
            elif num1 <= 0 or num2 <= 0:
                result.set("ValueError: math domain error")
            elif num2 == 1:
                result.set("ZeroDivisionError: float division by zero")
        elif operation == "sin (num1 only)":
            deg = num1
            rad = radians(deg)
            result.set(sin(rad))
        elif operation == "cos (num1 only)":
            deg = num1
            rad = radians(deg)
            result.set(cos(rad))
        elif operation == "tan (num1 only)":
            deg = num1
            rad = radians(deg)
            if cos(rad) == 0:
                result.set("ZeroDivisionError: float division by zero")
            else:
                result.set(tan(rad))
        elif operation == "csc (num1 only)":
            deg = num1
            rad = radians(deg)
            if sin(rad) == 0:
                result.set("ZeroDivisionError: float division by zero")
            else:
                result.set(1 / sin(rad))
        elif operation == "sec (num1 only)":
            deg = num1
            rad = radians(deg)
            if cos(rad) == 0:
                result.set("ZeroDivisionError: float division by zero")
            else:
                result.set(1 / cos(rad))
        elif operation == "cot (num1 only)":
            deg = num1
            rad = radians(deg)
            if tan(rad) == 0 or sin(rad) == 0:
                result.set("ZeroDivisionError: float division by zero")
            else:
                result.set(1 / tan(rad))
        elif operation == "nCr":
            if num1.is_integer() and num2.is_integer():
                def combination(n, r):
                    n, r = int(num1), int(num2)
                    if 0 <= r <= n:
                        result.set(factorial(n) // (factorial(r) * factorial(n - r)))
                    else:
                        result.set("Invalid input: r must be <= n and both >= 0")
                combination(num1, num2)
            else:
                result.set("TypeError: Inputs must be integers")
        elif operation == "nPr":
            if num1.is_integer() and num2.is_integer():
                def permutation(n, r):
                    n, r = int(num1), int(num2)
                    if 0 <= r <= n:
                        result.set(factorial(n) // factorial(n - r))
                    else:
                        result.set("Invalid input: r must be <= n and both >= 0")
                permutation(num1, num2)
            else:
                result.set("TypeError: Inputs must be integers")
        elif operation == "right triangle area":
            if num1 >= 0:
                result.set(0.5 * num1 * num2)
            else:
                result.set("Invalid input - num1 must not be a negative number")
        elif operation == "equiangular triangle area (num1 only)":
            if num1 >= 0:
                result.set((sqrt(3)/4) * (num1 ** 2))
            else:
                result.set("Invalid input - num1 must not be a negative number")
        elif operation == "circle area (num1 only)":
            if num1 >= 0:
                result.set(pi * (num1 ** 2))
            else:
                result.set("Invalid input - num1 must not be a negative number")
        elif operation == "sphere volume (num1 only)":
            if num1 >= 0:
                result.set((4/3) * pi * (num1 ** 3))
            else:
                result.set("Invalid input - num1 must not be a negative number")
        elif operation == "equiangular hexagon (num1 only)":
            if num1 >= 0:
                result.set(sqrt(6.75) * (num1 ** 2))
            else:
                result.set("Invalid input - num1 must not be a negative number")
        elif operation == "pyramid volume":
            if num1 >= 0:
                result.set((1/3) * num1 * num2)
            else:
                result.set("Invalid input - num1 must not be a negative number")
        elif operation == "cone volume":
            if num1 >= 0 and num2 >= 0:
                result.set((1/3) * pi * (num1 ** 2) * num2)
            else:
                result.set("Invalid input - num1 must not be negative numbers")
        elif operation == "oval area":
            if num1 >= 0 and num2 >= 0:
                result.set(pi * num1 * num2)
            else:
                result.set("Invalid input - num1 must not be negative numbers")
        elif operation == "°C to °F and K (num1 only)":
            if num1 >= -273.15:
                fahrenheit = (1.8 * num1) + 32
                kelvin = num1 + 273.15
                result.set(f"{num1}°C equals {fahrenheit}°F and {kelvin} K")
            else:
                result.set("Invalid input - the value of °C must be at least -273.15")
        elif operation == "°F to °C and K (num1 only)":
            if num1 >= -459.67:
                celsius = 5 * (num1 - 32) / 9
                kelvin = celsius + 273.15
                result.set(f"{num1}°F equals {celsius}°C and {kelvin} K")
            else:
                result.set("Invalid input - the value of °F must be at least -459.67")
        elif operation == "K to °C and °F (num1 only)":
            if num1 >= 0:
                celsius = num1 - 273.15
                fahrenheit = (1.8 * (num1 - 273.15)) + 32
                result.set(f"{num1} K equals {celsius}°C and {fahrenheit}°F")
            else:
                result.set("Invalid input - the value of K must not be negative")
    except ValueError:
        result.set("Invalid input")
    loading.grid_forget()
    result_label.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)

def begin_calculation():
    loading.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
    result_label.grid_forget()
    update(0)
    calculation_thread = threading.Thread(target = calculator)
    calculation_thread.start()

def on_operation_change(event = None):
    selected_op = operations.get()
    if "num1 only" in selected_op:
        y.delete(0, tk.END)
        y.config(state = "disabled")
    else:
        y.config(state = "normal")

win = tk.Tk()
win.title("Simple Calculator")

frame = tk.Frame(win)
frame.pack(padx = 20, pady = 20)

x = tk.Entry(frame)
x.grid(row = 0, column = 0, padx = 5, pady = 5)

operation_values = ["+", "-", "*", "/", "%", "**", "<", ">", "<=", ">=", "sqrt (num1 only)", "cbrt (num1 only)", "|x| (num1 only)", "! (num1 only)", "odd/even (num1 only)", "prime/composite (num1 only)", "log", "sin (num1 only)", "cos (num1 only)", "tan (num1 only)", "csc (num1 only)", "sec (num1 only)", "cot (num1 only)", "nCr", "nPr", "right triangle area", "equiangular triangle area (num1 only)", "circle area (num1 only)", "sphere volume (num1 only)", "equiangular hexagon (num1 only)", "pyramid volume", "cone volume", "oval area", "°C to °F and K (num1 only)", "°F to °C and K (num1 only)", "K to °C and °F (num1 only)"]
operations = ttk.Combobox(frame, values = operation_values)
operations.grid(row = 0, column = 1, padx = 5, pady = 5)
operations.bind("<<ComboboxSelected>>", on_operation_change)

y = tk.Entry(frame)
y.grid(row = 0, column = 2, padx = 5, pady = 5)

submit_button = tk.Button(frame, text = "Submit", command = begin_calculation)
submit_button.grid(row = 0, column = 3, padx = 5, pady = 5)

loading = tk.Label(frame, text = "Calculating...")

result = tk.StringVar()
result_label = tk.Label(frame, textvariable=result)
result_label.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)

win.mainloop()