import tkinter as tk
from tkinter.ttk import Label
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Label Widget Demo')

# show a label
label = Label(root, text='This is a label')
label.pack(ipadx=10, ipady=10)

# label with a specific font
label1 = ttk.Label(
    root,
    text='A Label with the Helvetica font',
    font=("Helvetica", 14))

label1.pack(ipadx=10, ipady=10)

root.mainloop()