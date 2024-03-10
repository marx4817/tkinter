import tkinter as tk

root = tk.Tk()
root.title('Tkinter Place Geometry Manager')
root.geometry("600x400")

#absolute
label1 = tk.Label(master=root, text="Place",bg='red',fg='white')
label1.place(x=0,y=0,width=120, height=60)

#relatives
label2 = tk.Label(master=root, text="Place",bg='red',fg='white')
label2.place(relx=0.5, rely=0.5, width=100, height=50, anchor=tk.CENTER)

root.mainloop()