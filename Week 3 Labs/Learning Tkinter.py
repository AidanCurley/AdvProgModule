import tkinter
import sys


def add_reminder(title, text, x, y, notes, reminders):
    note_window = tkinter.Toplevel()
    note_window.resizable(width=False, height=False)
    note_window.geometry("+" + str(x) + "+" + str(y))
    note_window.title(title)

    reminder = tkinter.Text(note_window, bg="yellow", width=30, height=15)
    reminder.insert(tkinter.END, text)
    reminder.pack()

    notes.append(note_window)
    reminders.append(reminder)

    def delete_window_handler():
        print("Window Deleted")
        note_window.withdraw()
        notes.remove(note_window)
        reminders.remove(reminder)

    note_window.protocol("WM_DELETE_WINDOW", delete_window_handler)


def open_file():
    print("You opened a file")
    return


def save_file():
    return


def close_file():
    return


def quit():
    return


def view_file():
    return


def view_record():
    return


def main():
    def post():
        print("Post")
        add_reminder(title_text.get(), note.get("1.0", tkinter.END), root.winfo_rootx() + 5, root.winfo_rooty() + 5, notes, reminders)
        note.delete("1.0", tkinter.END)
        title_text.delete(0,tkinter.END)

    # open a root window, set title and size
    root = tkinter.Tk()
    root.title("Reminder!")
    root.resizable(width=500, height=500)

    notes = []
    reminders = []

    # create a Menu called bar
    bar = tkinter.Menu(root)
    fileMenu = tkinter.Menu(bar, tearoff=0)
    viewMenu = tkinter.Menu(bar, tearoff=0)

    # add menu itels to the menus
    file_menu_items = {"Open": open_file, "Save": save_file, "Close": close_file, "Quit": quit}
    view_menu_items = {"View file": view_file, "View record": view_record}
    menus = [file_menu_items, view_menu_items]

    for item in file_menu_items:
        fileMenu.add_command(label=item, command=file_menu_items[item])
    for item in view_menu_items:
        viewMenu.add_command(label=item, command=view_menu_items[item])

    # add a menu label in the main bar and add menu items to cascade from it
    bar.add_cascade(label='File', menu=fileMenu)
    bar.add_cascade(label='View', menu=viewMenu)
    root.config(menu=bar)

    # Creating a main frame to group items together
    main_frame = tkinter.Frame(root, borderwidth=10, padx=5, pady=5)
    main_frame.pack()
    # Creating a title frame to hold the title entry box
    title_frame = tkinter.Frame(main_frame)
    title_frame.pack()

    # Create an entry and text widget for the title
    note_title = tkinter.StringVar()
    title_label = tkinter.Label(title_frame, text="Title: ")
    title_label.grid(row=1, column=1, sticky=tkinter.E)
    title_text = tkinter.Entry(title_frame, textvariable=note_title)
    title_text.grid(row=1, column=2, columnspan=2,sticky=tkinter.E+tkinter.W)

    # Create a text widget
    note = tkinter.Text(main_frame, bg="light green", width=30, height=15)
    note.pack()

    tkinter.Button(main_frame, text="New Reminder!", command=post).pack()

    # add text to the text box
    def now():
        note.insert(tkinter.END, "Now you've gone and done it!")
    tkinter.Button(main_frame, text="Now", command=now).pack()

    try:
        print("reading reminders.txt file")
        file = open(r"C:\Users\redye\MASTERS YORK\Advanced Programming\Week 3 Labs\reminders.txt", "r")
        x = int(file.readline())
        y = int(file.readline())
        root.geometry("+" + str(x) + "+" + str(y))

        line = file.readline()
        while line.strip() != "":
            x = int(line)
            y = int(file.readline())
            title = file.readline()
            text = ""
            line = file.readline()
            while line.strip() != "____....____._._._":
                text = text + line
                line = file.readline()
            text = text.strip()
            add_reminder(title, text, x, y, notes, reminders)
            line = file.readline()
    except FileNotFoundError:
        print("reminders.txt not found")

    def app_closing():
        print("Application closing")
        file = open(r"C:\Users\redye\MASTERS YORK\Advanced Programming\Week 3 Labs\reminders.txt", "w")
        file.write(str(root.winfo_x()) + "\n")
        file.write(str(root.winfo_y()) + "\n")

        for i in range(len(notes)):
            file.write(str(notes[i].winfo_rootx()) + "\n")
            file.write(str(notes[i].winfo_rooty()) + "\n")
            file.write(notes[i].title() + "\n")
            file.write(reminders[i].get("1.0", tkinter.END) + "\n")
            file.write("____....____._._._\n")

        file.close()
        root.quit()
        sys.exit()

    root.protocol("WM_DELETE_WINDOW", app_closing)

    tkinter.mainloop()


if __name__ == "__main__":
    main()
