import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Simple GUI Calculator")

entry = tk.Entry(window, width=20, font=('Arial', 16), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3), ('C', 4, 0),
    ('=', 4, 2)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=10, height=2, font=('Arial', 14), command=calculate)
    elif text == "C":
        button = tk.Button(window, text=text, width=10, height=2, font=('Arial', 14), command=clear)
    else:
        button = tk.Button(window, text=text, width=10, height=2, font=('Arial', 14), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

window.mainloop()
