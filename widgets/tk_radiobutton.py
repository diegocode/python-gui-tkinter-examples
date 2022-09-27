import tkinter

# variable para opción predeterminada
opcion_inicial = "2"

# callback para variable "muestra_opcion"
def muestra_opcion(*args):
	# obtiene el string de la variable "valor" y lo guarda en "s"
    s = valor.get()
    
    # actualiza el teto del label   
    lblSeleccion.configure(text=s)


app = tkinter.Tk()
app.title("RadioButton")

# crea variable para usar con los RadioButton
valor = tkinter.StringVar()

# valor predeterminado
valor.set(opcion_inicial)

# label para mostrar la opción seleccionada
lblSeleccion = tkinter.Label(app, text=opcion_inicial)

# ancho del Label (en caracteres)
# y tipo de letra
lblSeleccion.configure(width=20, font=('Arial', 14))

# crea tres RadioButton
r1 = tkinter.Radiobutton(app, variable = valor, text = "uno", value = "1")
r2 = tkinter.Radiobutton(app, variable = valor, text = "dos", value = "2")
r3 = tkinter.Radiobutton(app, variable = valor, text = "tres", value = "3")

# vincula el evento de cambio opción en 
# "valor" con el callback "muestra_opcion"
valor.trace("w", muestra_opcion)

# ubica widgets
lblSeleccion.grid(row=0, column= 0, pady=(10, 5))
r1.grid(row=1, column=0, pady=5)
r2.grid(row=2, column=0, pady=5)
r3.grid(row=3, column=0, pady=(5, 15))

app.mainloop()

