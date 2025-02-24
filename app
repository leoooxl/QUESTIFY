import tkinter as tk 
from tkinter import * 

class My_Window(Tk):  
    def __init__(self):
        # Generation of the main window (opening screen)
        super().__init__()
        img = PhotoImage(file='questify_logo.png')
        self.iconphoto(False, img)
        self.geometry("800x600")
        self.title("Questify")

if __name__ == "__main__":
    my_window = My_Window()
    my_window.mainloop()