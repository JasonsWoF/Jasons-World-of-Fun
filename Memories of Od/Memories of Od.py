from tkinter import *

root = Tk()

root.title("Memories of Od")

title = Label(root, text="Memories of Od")
title.pack()

root.geometry('1050x750')

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
