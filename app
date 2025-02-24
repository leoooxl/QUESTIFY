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

        self.home_frame = Frame(self)
        self.home_frame.pack()
        self.home_frame.place(x=0, y=0, width=800, height=600)
        self.home_frame.config(bg="white")

        # Generation of the home screen title
        self.home_title = Label(self.home_frame, text="Welcome to Questify", font=("Arial", 20), bg="white")
        self.home_title.pack()
        self.home_title.place(x=300, y=50)

        # Generation of the home screen subtitle
        self.home_subtitle = Label(self.home_frame, text="Your guide through gamification", font=("Arial", 15), bg="white")
        self.home_subtitle.pack()
        self.home_subtitle.place(x=320, y=100)

        # Generation of the start button
        self.start_button = Button(self.home_frame, text="Start", font=("Arial", 15), bg="white", command=self.start_button_click)
        self.start_button.pack()
        self.start_button.place(x=370, y=200)
    
    def start_button_click(self):
        pass

if __name__ == "__main__":
    my_window = My_Window()
    my_window.mainloop()
