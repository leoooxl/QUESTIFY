import tkinter as tk
from tkinter import *
from tkinter import PhotoImage

class My_Window(Tk):  
    def __init__(self):
        super().__init__()

        # Fenêtre principale
        self.geometry("800x600")
        self.title("Questify")
        self.configure(bg="#0F0F0F")  # fond sombre

        # Logo
        self.logo_img = PhotoImage(file="questify_logo.png")
        self.logo_label = Label(self, image=self.logo_img, bg="#0F0F0F")
        self.logo_label.place(relx=0.5, y=80, anchor="center")

        # Titre
        self.title_label = Label(
            self, 
            text="QUESTIFY", 
            font=("Arial", 30, "bold"), 
            fg="#00FF88", 
            bg="#0F0F0F"
        )
        self.title_label.place(relx=0.5, y=200, anchor="center")

        # Slogan
        self.subtitle_label = Label(
            self, 
            text="Gamify your productivity", 
            font=("Arial", 14), 
            fg="#F0F0F0", 
            bg="#0F0F0F"
        )
        self.subtitle_label.place(relx=0.5, y=240, anchor="center")

        # Bouton Start
        self.start_button = Button(
            self, 
            text="Start your quest", 
            font=("Arial", 14, "bold"), 
            bg="#0F0F0F", 
            fg="#00FF88", 
            activebackground="#00FF88", 
            activeforeground="#0F0F0F", 
            relief="solid", 
            borderwidth=2, 
            cursor="hand2", 
            command=self.start_button_click
        )
        self.start_button.place(relx=0.5, y=320, width=180, height=45, anchor="center")

    def quest_screen(self):
        quest_name = input('What is the main task you want to focus on ?')
        
    
    def start_button_click(self):
        self.home_frame.destroy()
        self.quest_screen()

if __name__ == "__main__":
    my_window = My_Window()
    my_window.mainloop()
