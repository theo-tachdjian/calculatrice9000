import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculatrice")
        master.geometry("360x453")

        self.total = tk.StringVar()
        self.total.set("0")

        self.entry = tk.Entry(master, textvariable=self.total)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            {"text": "1", "row": 1, "column": 0, "command": lambda: self.add_number("1")},
            {"text": "2", "row": 1, "column": 1, "command": lambda: self.add_number("2")},
            {"text": "3", "row": 1, "column": 2, "command": lambda: self.add_number("3")},
            {"text": "+", "row": 1, "column": 3, "command": lambda: self.add_operator("+")},

            {"text": "4", "row": 2, "column": 0, "command": lambda: self.add_number("4")},
            {"text": "5", "row": 2, "column": 1, "command": lambda: self.add_number("5")},
            {"text": "6", "row": 2, "column": 2, "command": lambda: self.add_number("6")},
            {"text": "-", "row": 2, "column": 3, "command": lambda: self.add_operator("-")},

            {"text": "7", "row": 3, "column": 0, "command": lambda: self.add_number("7")},
            {"text": "8", "row": 3, "column": 1, "command": lambda: self.add_number("8")},
            {"text": "9", "row": 3, "column": 2, "command": lambda: self.add_number("9")},
            {"text": "*", "row": 3, "column": 3, "command": lambda: self.add_operator("*")},

            {"text": "C", "row": 4, "column": 0, "command": self.clear},
            {"text": "0", "row": 4, "column": 1, "command": lambda: self.add_number("0")},
            {"text": "=", "row": 4, "column": 2, "command": self.calculate},
            {"text": "/", "row": 4, "column": 3, "command": lambda: self.add_operator("/")},

            {"text": "^", "row": 5, "column": 0, "command": lambda: self.add_operator("**")},
            {"text": "sqrt", "row": 5, "column": 1, "command": lambda: self.add_operator("math.sqrt(")},
            {"text": "%", "row": 5, "column": 2, "command": lambda: self.add_operator("%")},
            {"text": ".", "row": 5, "column": 3, "command": lambda: self.add_operator(".")},
        ]

        for button in buttons:
            tk.Button(self.master, text=button["text"], command=button["command"], width=6, height=2, padx=20, pady=20).grid(row=button["row"], column=button["column"], sticky="nsew")

    def insert_number(self, number):
        self.equation.set(self.equation.get() + "{}".format(number))

    def decimal_point(self):
        if "." not in self.equation.get():
            self.equation.set(self.equation.get() + ".")

    def clear(self):
        self.equation.set("")

    def evaluate(self):
        try:
            self.equation.set(eval(self.equation.get()))
        except:
            self.equation.set("error")

    def add_button(self, text, row, column, command):
        tk.Button(self, text=text, width=10, height=5, command=command,).grid(row=row, column=column, padx=5, pady=5)

    def add_number(self, number):
        current_total = self.total.get()
        if current_total == "0":
            self.total.set(number)
        else:
            self.total.set(current_total + number)

    def add_operator(self, operator):
        current_total = self.total.get()
        if operator == "sqrt":
            current_total += "math.sqrt("
        elif operator == "%":
            current_total += "/100*"
        else:
            current_total += operator
        self.total.set(current_total)

    def clear(self):
        self.total.set("0")

    def calculate(self):
        current_total = self.total.get()
        try:
            self.total.set(eval(current_total))
        except:
            self.total.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
