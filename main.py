import tkinter as tk
from tkinter import messagebox

# Definición de palíndromos predefinidos
palindromos_definidos = [
    "ana", "arenera", "salas", "aibofobia", "reconocer", 
    "civic", "radar", "level", "rotor", "deified"
]

def es_palindromo(texto):
    """Verifica si el texto es un palíndromo."""
    texto = texto.replace(" ", "").lower()  # Elimina espacios y convierte a minúsculas
    return texto == texto[::-1]

def contar_palindromos_en_texto(texto):
    """Cuenta cuántos palíndromos definidos están presentes en el texto."""
    texto = texto.lower()  # Convierte a minúsculas
    contador = 0
    for palindromo in palindromos_definidos:
        if palindromo in texto:
            contador += 1
    return contador

def validar_input():
    """Valida el input según la opción seleccionada."""
    input_texto = entrada.get()
    if opcion_var.get() == 1:  # Opción 1: Validar palíndromos
        if es_palindromo(input_texto):
            messagebox.showinfo("Resultado", f"'{input_texto}' es un palíndromo.")
        else:
            messagebox.showinfo("Resultado", f"'{input_texto}' no es un palíndromo.")
    elif opcion_var.get() == 2:  # Opción 2: Contar palíndromos en texto
        conteo = contar_palindromos_en_texto(input_texto)
        messagebox.showinfo("Resultado", f"Se encontraron {conteo} palíndromos definidos en el texto.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Máquina de Turing - Validador de Palíndromos")

# Opción de selección
opcion_var = tk.IntVar()
opcion_var.set(1)  # Opción por defecto

tk.Label(ventana, text="Selecciona una opción:").pack()

tk.Radiobutton(ventana, text="Validar Palíndromo", variable=opcion_var, value=1).pack()
tk.Radiobutton(ventana, text="Contar Palíndromos Definidos", variable=opcion_var, value=2).pack()

# Entrada de texto
tk.Label(ventana, text="Ingresa tu texto:").pack()
entrada = tk.Entry(ventana, width=50)
entrada.pack()

# Botón para validar
boton_validar = tk.Button(ventana, text="Validar", command=validar_input)
boton_validar.pack()

# Iniciar el bucle de la interfaz
ventana.mainloop()
