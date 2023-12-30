import tkinter as tk
import customtkinter as ctk

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Information")
        self.crear_interfaz()

    def crear_interfaz(self):
        self.github_token = ctk.CTkLabel(self, text = "GitHub Token: ")
        self.github_token.grid(column = 0, row = 0)
        self.task_button = ctk.CTkButton(self, text = "Add Task")
        self.task_button.grid(column = 1, row = 1) 

        self.quit_button = ctk.CTkButton(self, text="Quit", command = self.quitar)
        self.quit_button.grid(column = 1, row = 2)
    def quitar(self):
        self.destroy()

if __name__ == "__main__":
    app = Interface()
    app.mainloop()
