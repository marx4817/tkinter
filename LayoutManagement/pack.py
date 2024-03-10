import tkinter as tk

root = tk.Tk()
root.title('Tkinter Pack Layout')
root.geometry('600x400')

label1 = tk.Label(master=root, text='Tkinter',bg='red',fg='white')
label2 = tk.Label(master=root,text='Pack Layout',bg='green', fg='white')
label3 = tk.Label(master=root, text='Demo',bg='blue', fg='white')

label1.pack(side=tk.TOP, expand=True, fill='x', ipady=10)
label2.pack(side=tk.TOP, anchor=tk.W, expand=True, fill='y', ipadx=10)
label3.pack(side=tk.TOP, expand=True, fill='both', padx=10, pady=10)

root.mainloop()