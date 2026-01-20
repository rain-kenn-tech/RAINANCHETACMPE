import tkinter as tk

# Create main window
w = tk.Tk()
w.title("Simple Calculator")
w.geometry("300x400")
w.resizable(False, False)

# Entry widget for input/output
e = tk.Entry(w, font=("Arial", 20), bd=5, justify="right")
e.pack(fill="both", padx=10, pady=10, ipady=10)

# Function to handle button clicks
def click(x):
    if x == "=":
        try:
            expr = e.get()           # Get expression first
            result = eval(expr)      # Evaluate the expression
            e.delete(0, tk.END)
            e.insert(0, result)
        except:
            e.delete(0, tk.END)
            e.insert(0, "Error")
    elif x == "C":
        e.delete(0, tk.END)
    else:
        e.insert(tk.END, x)

# Button labels
btns = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

# Frame for buttons
f = tk.Frame(w)
f.pack()

# Create buttons in grid
r = c = 0
for b in btns:
    tk.Button(f, text=b, font=("Arial",14), width=5, height=2,
              command=lambda x=b: click(x)).grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c == 4:
        c = 0
        r += 1

# Clear button
tk.Button(w, text="Clear", font=("Arial",14), height=2,
          command=lambda: click("C")).pack(fill="both", padx=20, pady=10)

# Run the GUI loop
w.mainloop()
