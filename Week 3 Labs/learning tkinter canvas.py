from tkinter import *
window = Tk()
window.title("Canvas Example")

c = Canvas(window, width=600, height=600)
c.pack()

# coordinates: x-y top-left, followed by x-y bottom right
c.create_rectangle(40, 40, 110, 110, fill="#FD6707", outline='#C5D906',)

# coordinates are: x-y top-left, followed by x-y bottom right (as a rectangle)
c.create_oval(90, 120, 190, 170, width=10, outline='#FD6707')

# each pair of values is x-y for a specified point within the canvas space
star = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
c.create_polygon(star, outline='#925BCC', fill='#C5D906', width=3)

img = PhotoImage(file="myFirstWireframe.png")
c.create_image(20,180, anchor=NW, image=img)
window.mainloop()
