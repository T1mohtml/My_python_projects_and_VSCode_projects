import tkinter as tk
from tkinter import Toplevel


def open_calculator():
    # Create a new window for the calculator
    calculator_window = Toplevel()
    calculator_window.title("Calculator")
    calculator_window.geometry("350x350")

    # Variables for input
    expression = ""

    def press(key):
        nonlocal expression
        expression += key
        input_text.set(expression)

    def clear():
        nonlocal expression
        expression = ""
        input_text.set(expression)

    def calculate():
        nonlocal expression
        try:
            # Evaluate the expression and display the result
            result = str(eval(expression))
            input_text.set(result)
            expression = result  # Update for further calculations
        except:
            input_text.set("Error")
            expression = ""

    # Entry widget to display current input
    input_text = tk.StringVar()
    input_box = tk.Entry(calculator_window, textvariable=input_text, font=('Arial', 18), bd=10, insertwidth=2, width=14,
                         justify='right')
    input_box.grid(row=0, column=0, columnspan=4)

    # Button layout
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for (text, row, col) in buttons:
        if text == "=":
            # Add calculate functionality for '=' button
            button = tk.Button(calculator_window, text=text, padx=20, pady=20, font=('Arial', 16), command=calculate)
        elif text == "C":
            # Add clear functionality for 'C' button
            button = tk.Button(calculator_window, text=text, padx=20, pady=20, font=('Arial', 16), command=clear)
        else:
            # Add digit/operator functionality
            button = tk.Button(calculator_window, text=text, padx=20, pady=20, font=('Arial', 16),
                               command=lambda key=text: press(key))

        button.grid(row=row, column=col)


# Main application window
root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

# Button to open calculator window
open_calc_button = tk.Button(root, text="Open Calculator", padx=20, pady=10, font=('Arial', 14),
                             command=open_calculator)
open_calc_button.pack(expand=True)

root.mainloop()