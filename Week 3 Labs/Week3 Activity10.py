from tkinter import ttk
import tkinter.scrolledtext as tkscrolled
import tkinter as tk


def open_main_window(title, x, y):
    # set up main window
    root = tk.Tk()
    root.title(title)
    root.geometry(f"{x}x{y}")
    return root


def make_grid_rows_and_columns(window, rows, columns):
    for i in range(rows):
        window.grid_rowconfigure(i, weight=1, uniform="group1")
    for i in range(columns):
        window.grid_columnconfigure(i, weight=1, uniform="group1")


def add_labels_to_main_window(window, labels):
    r = 1
    for l in labels:
        tk.Label(window, text=l, anchor='w', padx=10, font=("Helvetica", 14))\
            .grid(row=r, column=0, columnspan=2, sticky="nw")
        r = r + 2


def add_text_entry_box(window, row, column, text):
    entry = tk.Entry(window, font=("Helvetica", 14))
    entry.grid(row=row, column=column, columnspan=3, sticky="nw")
    entry.insert(tk.END, text)


def add_button(window, row, column, name):
    b = tk.Button(window, text=name, borderwidth=3, font=("Helvetica", 14), relief=tk.RAISED)
    b.grid(row=row, column=column, rowspan=2, columnspan=3, ipady=5, ipadx=5, pady=(15, 15), padx=(25, 25))


def add_combobox(window, row, column, values):
    combo = ttk.Combobox(window, font=("Helvetica", 14))
    combo.grid(row=row, column=column, columnspan=3, sticky="nw")
    combo.set("ComboBox")
    combo['values'] = values


def add_scrolled_textbox(window, row, column, text):
    bio = tkscrolled.ScrolledText(window, wrap=tk.WORD, font=("Helvetica", 14))
    bio.grid(row=row, column=column, padx=10, pady=5, rowspan=1, columnspan=9, sticky="nw")
    bio.insert(tk.INSERT, text)


def add_frame_with_radio_buttons(window, options):
    frame1 = tk.Frame(window, bg="light gray", relief='sunken')
    frame1.grid(row=1, column=6, rowspan=3, columnspan=3, padx=(10, 10), sticky="nwe")
    mod = tk.StringVar()
    mod.set("Currently Employed")  # initialize
    r = 0
    for option in options:
        b = tk.Radiobutton(frame1, text=option, bg="light gray", variable=mod, value=option)
        b.grid(row=r, column=1, sticky="nw")
        r += 1


def add_frame_with_checkboxes(window, options):
    frame2 = tk.Frame(window, bg="light gray", relief='sunken')
    frame2.grid(row=5, column=6, rowspan=3, columnspan=3, padx=(10, 10), sticky="nwe")
    r = 0
    for option in options:
        b = tk.Checkbutton(frame2, text=option, bg="light gray")
        b.grid(row=r, column=1, sticky="nw")
        r += 1


def main():
    # draw main window
    root = open_main_window("Register Personal Details", 650, 500)
    make_grid_rows_and_columns(root, 15, 10)

    #add labels and text entry box
    labels = ['Name:', 'Profession:', 'Position:', 'Biography:']
    add_labels_to_main_window(root,labels)
    add_text_entry_box(root, 1, 2, "Name")

    # add combo boxes
    jobs = ["Accountant", "Architect", "Doctor", "Engineer", "Teacher"]
    positions = ["Officer", "Assistant Manager", "Manager", "Managing Director", "CEO"]
    add_combobox(root, 3, 2, jobs)
    add_combobox(root, 5, 2, positions)

    text = "Secrevit fontes liquidum locoque pronaque?\nIllas semine " \
           "campoque declivia oppida corpora nam inter fuit discordia " \
           "tellus solidumque iunctarum erat: quae terrenae ubi rerum recessit iudicis aestu fixo"
    add_scrolled_textbox(root, 8, 0, text)

    # add frames to the right hand side
    buttons = ["Currently Employed", "Self Employed", "Unemployed", "Other"]
    add_frame_with_radio_buttons(root, buttons)
    checkboxes = ["Student (Part/Full-time)", "Home Owner", "Transport Owner"]
    add_frame_with_checkboxes(root, checkboxes)

    # add buttons at bottom
    add_button(root, 13, 0, 'Clear')
    add_button(root, 13, 7, 'Submit')
    add_button(root, 13, 5, 'Cancel')

    # launch the GUI
    root.mainloop()


if __name__ == "__main__":
    main()
