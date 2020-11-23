import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Favourite Programming Language")
window.geometry("400x200")


def show_best():
    user_selection.configure(text=languages.get(best.get()))

languages = {1:"Python", 2:"Perl", 3:"Java", 4:"C++", 5:"Ruby"}

best = tk.IntVar()
best.set(1)
tk.Label(window, text='Choose a language:').pack()

for val, language in languages.items():
    tk.Radiobutton(window, text=language, variable=best, value=val, command=show_best).pack()

tk.Label(window, text='You selected:').pack()
user_selection = tk.Label(window, text='none')
user_selection.pack()
window.mainloop()