import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def button_clicked():
    print("Button clicked")

button = ttk.Button(root, text="Click me", command=button_clicked)
button.pack()


def select(options):
    print(options)

ttk.Button(root, text="Rock", command=lambda: select("Rock")).pack()
ttk.Button(root, text="Marx", command=lambda: select("Marx")).pack()
ttk.Button(root, text="Lordeus", command=lambda: select("Lordeus")).pack()

root.mainloop()
