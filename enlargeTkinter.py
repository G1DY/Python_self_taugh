from tkinter import *

def enlarge_window():
    root.geometry("600x400")

def minimize_window():
    root.geometry("400x300")

root = Tk()
root.geometry("400x300")

enlarge_button = Button(root, text="Enlarge", command=enlarge_window)
enlarge_button.pack()

minimize_button = Button(root, text="Minimize", command=minimize_window)
minimize_button.pack()

root.mainloop()
