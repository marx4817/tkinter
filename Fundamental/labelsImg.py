import tkinter as tk
from tkinter import ttk

#create the root window
root = tk.Tk()
root.geometry('400x300')
root.resizable(False, False)
root.title("Label Widget Image")

#displaying an image labe
photo = tk.PhotoImage(file='./assets/h_0.png')
imgLabel = ttk.Label(
    root,
    image=photo,
    text="Pytthon",
    compound='top',
    padding=5,
)
imgLabel.pack()

root.mainloop()