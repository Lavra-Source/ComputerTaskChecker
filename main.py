from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Пользование компьютером на практике")
selectframe = ttk.Frame(root, padding="3 3 3 3")
selectframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)

root.mainloop()