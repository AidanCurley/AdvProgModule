import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Grid Layout")
window.geometry("400x200")


# generate 12 labels each with the same attributes,
# in the same row, in consecutive columns
for i in range(0, 12):
    ttk.Label(window, text='A'+str(i), anchor="center").grid(row=0, column=i, sticky='NSEW')
    window.grid_columnconfigure(i, weight=1)

# generate 6 labels each spanning 2 columns
for i in range(0,6):
    ttk.Label(window, text='B'+str(i), anchor="center").grid(row=1, column=i+(1*i), columnspan=2, sticky='NSEW')

# a single label spanning all 12 columns
ttk.Label(window, text='C'+str(i), anchor="center").grid(row=2, column=0, columnspan=12, sticky='NSEW')

# rowconfigure and colconfigure weight set to 1 to give equal priority when window adjusted in size
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)

window.mainloop()
