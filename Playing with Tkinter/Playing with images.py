from tkinter import *
from PIL import ImageTk, Image

root=Tk()

def declare_buttons(image_number):
    global button_next, button_back, button_quit
    button_quit = Button(root, text="Exit Program", command=root.quit)
    button_back = Button(root, text="<< Back", command=lambda: prev_image(image_number))
    button_next = Button(root, text="Next >>", command=lambda: next_image(image_number))


def render_buttons():
    global button_next, button_back, button_quit
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    button_quit.grid(row=1, column=1)


def set_image_holder(image_number):
    global image_holder, images
    image_holder = Label(image=images[image_number])


def render_image_holder():
    global image_holder
    image_holder.grid(row=0, column=0, columnspan=3)

def prev_image(image_number):
    global image_holder, button_back
    image_holder.grid_forget()
    set_image_holder(image_number-1)
    declare_buttons(image_number-1)
    if image_number == 1:
        button_back = Button(root, text="<< Back", state=DISABLED)
    render_image_holder()
    render_buttons()
    return


def next_image(image_number):
    global image_holder, button_next
    image_holder.grid_forget()
    set_image_holder(image_number+1)
    declare_buttons(image_number+1)
    if image_number + 1 == len(images)-1:
        button_next = Button(root, text="Next >>", state=DISABLED)

    render_image_holder()
    render_buttons()
    return


def choose_images():
    global images
    my_img1 = ImageTk.PhotoImage(Image.open('Leeds.png'))
    my_img2 = ImageTk.PhotoImage(Image.open('Rodrigo.jpg'))
    my_img3 = ImageTk.PhotoImage(Image.open('bamford.jpg'))
    images = [my_img1, my_img2, my_img3]


def main():
    root.title("Playing with Images")
    root.iconbitmap('Leeds.ico')

    choose_images()
    set_image_holder(0)
    declare_buttons(0)
    render_buttons()
    render_image_holder()

    root.mainloop()


if __name__ == "__main__":
    main()