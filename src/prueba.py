import tkinter as tk
from tkinter import messagebox
def valides(input : str) -> bool:
    return input.removeprefix("-").isnumeric() and int(input)>= -255 and int(input) <=255

def ingresar_datos():
    velocidad = entrada_velocidad.get()
    sentido1 = var_horario.get()
    sentido2 = var_antihorario.get()
    apagar = var_apagar.get()
    if sentido1 != sentido2:
        if sentido1:
            sentido="horario"
        else:
            sentido="antihorario"
    if not valides(velocidad):
      messagebox.showinfo("Datos ingresados", "La velocidad no se ha ingresado de manera correcta")
    else:
     if sentido1 != sentido2:
        print(f"Velocidad: {velocidad} rpm")
        print(f"Sentido de giro: {sentido}")
        print(f"Apagar motor: {'Sí' if apagar else 'No'}")

        messagebox.showinfo("Datos ingresados", "Los datos se han ingresado correctamente.")
     else:
        messagebox.showinfo("Datos ingresados", "El sentido no se ha ingresado de manera correcta")

ventana = tk.Tk()
ventana.title("Control de Motor")

tk.Label(ventana, text="Velocidad (-255 a 255):").grid(row=0, column=0, padx=10, pady=10)
entrada_velocidad = tk.Entry(ventana)
entrada_velocidad.grid(row=0, column=1, padx=10, pady=10)

var_horario = tk.BooleanVar()
tk.Checkbutton(ventana, text="Sentido Horario", variable=var_horario).grid(row=1, column=0, columnspan=2, pady=10)
var_antihorario = tk.BooleanVar()
tk.Checkbutton(ventana, text="Sentido Antihorario", variable=var_antihorario).grid(row=2, column=0, columnspan=2, pady=10)

var_apagar = tk.BooleanVar()
tk.Checkbutton(ventana, text="Apagar motor", variable=var_apagar).grid(row=3, column=0, columnspan=2, pady=10)

boton_ingresar = tk.Button(ventana, text="Ingresar datos", command=ingresar_datos)
boton_ingresar.grid(row=5, column=0, columnspan=2, pady=10)

ventana.mainloop()