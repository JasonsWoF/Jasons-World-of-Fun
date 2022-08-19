from tkinter import *

root = Tk()

root.title("Jasons World of Fun")

title = Label(root, text="Jasons World of Fun")
title.pack()


# Function for pressing "Birth"
def first_click():
    loading_screen = Frame(root, bg="grey")
    loading_screen.pack()


'''
birth_name = Entry(root)
birth_name.pack

'''

firstGameButton = Button(root, text="Birth", command=first_click)
firstGameButton.pack()

root.mainloop()
