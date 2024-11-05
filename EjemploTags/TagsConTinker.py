import tkinter as tk

# Funciones para los botones
def aceptar():
    print("Aceptar presionado")

def denegar():
    print("Denegar presionado")

def cerrar():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Datos")

# Crear las etiquetas
etiquetas = ["Nombre", "DNI", "Dirección"]
for i, texto in enumerate(etiquetas):
    tk.Label(root, text=texto).grid(row=i, column=0, padx=5, pady=5)

# Crear las cajas de texto
entradas = []
for i in range(len(etiquetas)):
    entrada = tk.Entry(root)
    entrada.grid(row=i, column=1, padx=5, pady=5)
    entradas.append(entrada)

# Crear los botones en la última fila de cada columna
tk.Button(root, text="Aceptar", command=aceptar).grid(row=len(etiquetas), column=0, padx=5, pady=5)
tk.Button(root, text="Denegar", command=denegar).grid(row=len(etiquetas), column=1, padx=5, pady=5)
tk.Button(root, text="Cerrar", command=cerrar).grid(row=len(etiquetas), column=2, padx=5, pady=5)

# Iniciar el bucle principal de la ventana
root.mainloop()
