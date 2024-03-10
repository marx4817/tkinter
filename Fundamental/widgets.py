import tkinter as tk
from tkinter import ttk

root = tk.Tk()


tk.Label(root, text="Classic Label").pack()

widg = ttk.Label()
widg['text'] = "Hi, I'm there"
widg.pack()

label = ttk.Label()
label.config(text="Hi, there")
label.pack()

root.mainloop()