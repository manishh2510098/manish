# Simple & Beautiful Calculator in Python using tkinter
# Easy to read and understand

import tkinter as tk

# Main Calculator Class
class Calculator:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("400x550")
        self.window.resizable(False, False)
        self.window.configure(bg="#f0f0f0")

        # This will store the current expression like "12+5*3"
        self.expression = ""

        # Create the display (where numbers and results show)
        self.display = tk.Entry(
            self.window,
            font=("Helvetica", 28, "bold"),
            justify="right",
            bd=10,
            relief="sunken",
            bg="white",
            fg="#333"
        )
        self.display.pack(fill=tk.X, padx=15, pady=20, ipady=20)

        # Create all buttons
        self.create_buttons()

    def create_buttons(self):
        # Button layout: (text, row, column, width span)
        buttons = [
            ("C", 0, 0, 1), ("±", 0, 1, 1), ("%", 0, 2, 1), ("÷", 0, 3, 1),
            ("7", 1, 0, 1), ("8", 1, 1, 1), ("9", 1, 2, 1), ("×", 1, 3, 1),
            ("4", 2, 0, 1), ("5", 2, 1, 1), ("6", 2, 2, 1), ("−", 2, 3, 1),
            ("1", 3, 0, 1), ("2", 3, 1, 1), ("3", 3, 2, 1), ("+", 3, 3, 1),
            ("0", 4, 0, 2), (".", 4, 2, 1), ("=", 4, 3, 1),
        ]

        # Create a frame for buttons
        frame = tk.Frame(self.window, bg="#f0f0f0")
        frame.pack(expand=True, fill="both")

        # Create each button
        for (text, row, col, colspan) in buttons:
            # Special style for operators and clear
            if text in "C±%÷×−+=":
                bg_color = "#ff9500"
                fg_color = "white"
            else:
                bg_color = "#ffffff"
                fg_color = "#333333"

            btn = tk.Button(
                frame,
                text=text,
                font=("Helvetica", 20, "bold"),
                bg=bg_color,
                fg=fg_color,
                relief="raised",
                bd=5,
                command=lambda t=text: self.button_click(t)
            )

            # Make the button expand nicely
            btn.grid(row=row, column=col, columnspan=colspan,
                     padx=8, pady=8, sticky="nsew", ipadx=10, ipady=20)

        # Make all rows and columns expand equally
        for i in range(5):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        if value == "C":
            # Clear everything
            self.expression = ""
            self.update_display()

        elif value == "=":
            # Calculate the result
            try:
                # Replace symbols so Python understands them
                result = str(eval(self.expression
                                .replace("×", "*")
                                .replace("÷", "/")
                                .replace("−", "-")))
                self.expression = result
                self.update_display()
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""

        elif value == "±":
            # Toggle positive/negative
            if self.expression and self.expression[0] == "-":
                self.expression = self.expression[1:]
            elif self.expression:
                self.expression = "-" + self.expression
            self.update_display()

        elif value == "%":
            # Convert to percentage
            try:
                self.expression = str(float(self.expression) / 100)
                self.update_display()
            except:
                self.expression = ""
                self.update_display("Error")

        else:
            # Add number or operator
            self.expression += value
            self.update_display()

    def update_display(self, text=None):
        self.display.delete(0, tk.END)
        self.display.insert(0, text or self.expression)

    def run(self):
        self.window.mainloop()


# Run the calculator
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()