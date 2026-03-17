# calculator.py
import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        # Add this line to set the window icon
        self.root.iconbitmap("calculator.ico")  # Path to your .ico file
        
        # Display
        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(
            root, 
            textvar=self.display_var, 
            font=("Arial", 24),
            justify="right",
            state="readonly"
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # Button layout
        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C"]
        ]
        
        # Create buttons
        for row_idx, row in enumerate(buttons, start=1):
            for col_idx, btn_text in enumerate(row):
                self.create_button(btn_text, row_idx, col_idx)
        
        # Configure grid weights
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def create_button(self, text, row, col):
        btn = tk.Button(
            self.root,
            text=text,
            font=("Arial", 18),
            command=lambda: self.on_button_click(text)
        )
        
        if text == "=":
            btn.config(bg="green", fg="white")
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        elif text == "C":
            btn.config(bg="red", fg="white")
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
        else:
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    
    def on_button_click(self, char):
        current = self.display_var.get()
        
        if char == "C":
            self.display_var.set("0")
        elif char == "=":
            try:
                # Replace symbols with Python operators for eval
                expression = current.replace("×", "*").replace("÷", "/")
                result = eval(expression)
                self.display_var.set(str(result))
            except:
                self.display_var.set("Error")
        else:
            if current == "0" and char not in ["+", "-", "×", "÷" , "."]:
                self.display_var.set(char)
            else:
                self.display_var.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
