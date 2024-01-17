import tkinter as tk
import customtkinter as ctk
import funciones as fn
import pyperclip

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Information")
        self.crear_interfaz()

    def crear_interfaz(self):
        token = fn.leerArchivoToken()

        self.github_token = ctk.CTkLabel(self, text="GitHub Token:")
        self.github_token.grid(column=0, row=0, pady=5, padx=5)

        self.token_label = ctk.CTkLabel(self, text=token)
        self.token_label.grid(column=1, row=0, pady=5, padx=5)

        self.new_token_entry = ctk.CTkEntry(self)
        self.new_token_entry.grid(column=0, row=1, pady=5, padx=5)
        self.new_token_entry.insert(0, "Ingrese su nuevo token")

        self.new_token_button = ctk.CTkButton(self, text="Cambiar Token", command=self.cambiar_token)
        self.new_token_button.grid(column=1, row=1, pady=5, padx=5)

        self.task_button = ctk.CTkButton(self, text="Add Task")
        self.task_button.grid(column=1, row=2, pady=5, padx=5)

        self.copy_token = ctk.CTkButton(self, text = "Copiar Token", command=self.copiar_token)
        self.copy_token.grid(column = 2, row = 0, pady = 5, padx = 5)

        self.quit_button = ctk.CTkButton(self, text="Quit", command=self.quitar)
        self.quit_button.grid(column=1, row=3, pady=5, padx=5)

    def quitar(self):
        self.destroy()

    def cambiar_token(self):
        path = '/home/gerardohuerta1502/Escritorio/Python/informacion.txt'
        nueva_linea = self.new_token_entry.get()

        try:
            with open(path, 'r') as file:
                linea = file.readlines()

            if linea:
                linea[0] = nueva_linea + '\n'

            with open(path, 'w') as file:
                file.writelines(linea)

        except FileNotFoundError:
            return f'El archivo {path} no se encontró'

        except IOError:
            return f"Error al intentar abrir o modificar el archivo {path}"

        except Exception as e:
            return "Error inesperado"

    def copiar_token(self):
        token = self.token_label.cget("text")
        self.clipboard_clear()
        self.clipboard_append(token)
        self.update()

if __name__ == "__main__":
    app = Interface()
    app.mainloop()

