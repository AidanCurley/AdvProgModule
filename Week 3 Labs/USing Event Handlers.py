import tkinter as tk
from tkinter import ttk

def get_def():
    term = term_entry.get()
    # clears the text box from previous entries
    output.delete(0.0, tk.END)
    if term in computer_defs:
        definition = computer_defs[term]
    else:
        definition = "sorry that term is not in the dictionary"
    output.insert(tk.END, definition)


window = tk.Tk()
window.title("Leeds United Players")
window.configure(background='black')

# text to output to the user
instruction='Enter a player you would like to know the details of:'
# adding a logo
logo = tk.PhotoImage(file="logo.png")
tk.Label(window, image=logo, bg='black').grid(row=0,column=0, sticky='EW')

# adding instruction for user
tk.Label(window, text=instruction, bg='black', fg='white', font='none 12 bold').grid(row=1, column=0, sticky='EW')
# create a text entry box
term_entry = tk.Entry(window, width=20, bg='white')
term_entry.grid(row=2, column=0)

# add a button
ttk.Button(window, text='GET', width=6, command=get_def).grid(row=3, column=0)
# label for output
tk.Label(window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold').grid(row=4, column=0, sticky='EW')

# output for the definiton (large text box)
output = tk.Text(window, width=75, height=6, wrap='word', background='white')
output.grid(row=5, column=0, columnspan=2)

# create the dictionary to extract terms
computer_defs = {'Bamford': 'Striker - underrated', 'Meslier': 'Goalkeeper - young'}
window.mainloop()
