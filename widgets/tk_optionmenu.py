import tkinter
from tkinter import messagebox

# lista de opciones
lista_opciones = ["alfa","beta", "gamma"]

# callback para variable optVar
def test(*args):
	# muestra un pop-up con el valor seleccionado
	messagebox.showinfo("selecciona", optVar.get())	

app = tkinter.Tk()

# título de la ventana
app.title("OptionMenu")

# tamaño de la ventana
app.geometry("300x200")
    
# variable para el OtionMenu
optVar = tkinter.StringVar()

# opción predeterminada 
optVar.set(lista_opciones[1])

# crea el widget OptionMenu
# vinculado a la variable optVar
# conteniendo las opciones de "lista_opciones"
opt = tkinter.OptionMenu(app, optVar, *lista_opciones)

# configura el ancho del OptionMenu (en caracteres)
opt.config(width=20)

# vincula el evento de cambio de valor en la variable 
# optVar con el callback "test"
optVar.trace("w", test)

# posición del widget en la ventana
opt.grid(row=0, column=0, padx=(50, 100), pady=50)


app.mainloop()
