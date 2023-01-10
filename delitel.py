from tkinter import *

def animate():
    for i in range (100):
        c.move(ball, 4, 0)
        root.after(15)


root = Tk()
c = Canvas(root, width = 200, height = 100)
c.pack()
ball = c.create_oval(0, 25, 50, 75)
animate()
root.mainloop()