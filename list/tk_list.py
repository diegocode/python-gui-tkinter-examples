import tkinter
from tkinter import messagebox


# callback para botón btnBorrar
def btnBorraCB():
    # obtiene indice de elemento seleccionado
    ind = lstOpciones.curselection()
    if len(ind) > 0:
        # obtiene el string en el índice
        # indicado y lo guarda en "s"
        s = lstOpciones.get(ind)

        # muestra pop-up de confirmación
        # la respuesta se guarda en "r"
        r = messagebox.askyesno("Atención","¿Confirma borrar?\n" + s + "?")

        if r:
            # si confirma, borra el elemento seleccionado
            lstOpciones.delete(ind)

    # coloca el foco en txtItem
    txtItem.focus_set()


# callback para botón btnSalir
def btnSaleCB():
    # muestra pop-up de confirmación
    if messagebox.askyesno("Atención","¿Confirma cerrar?"):
        # si confirma, termina programa
        top.destroy()
        exit()


# callback para botón btnAgregar
def btnAgregaCB():
    # obtiene string de txtItem y lo guarda en "s"
    s = txtItem.get()

    # borra txtItem
    txtItem.delete(0, tkinter.END)

    if len(s) > 0:
        # agrega al final de la lista el string en "s"
        lstOpciones.insert(tkinter.END, s)

    # coloca el foco en txtItem
    txtItem.focus_set()

top = tkinter.Tk()
top.title("una lista")

# crea Listbox
lstOpciones = tkinter.Listbox(top)

# crea Button btnAgregar
btnAgregar = tkinter.Button(top, text="Agregar", underline=0, command=btnAgregaCB)
# vincula Alt izquierdo + a con función "btnAgregaCB"
top.bind('<Alt_L><a>', lambda e:btnAgregaCB())

# crea btnBorrar
btnBorrar = tkinter.Button(top, text="Borrar", underline=0, command=btnBorraCB)
# vincula Alt izquierdo + b con función "btnBorraCB"
top.bind('<Alt_L><b>', lambda e:btnBorraCB())

# crea btnSalir
btnSalir = tkinter.Button(top, text="Salir", underline=0, command=btnSaleCB)
# vincula Alt izquierdo + s con función "btnSaleCB"
top.bind('<Alt_L><s>', lambda e:btnSaleCB())
txtItem = tkinter.Entry(top)

# posiciona cada widget en columna y fila correspondiente
btnAgregar.grid(row=0, column=1)
txtItem.grid(row=0, column=0)
lstOpciones.grid(row=1, column=0, rowspan=3)
btnBorrar.grid(row = 2, column = 1, sticky='S')
btnSalir.grid(row = 3, column = 1, sticky='S')

# coloca el foco en txtItem
txtItem.focus_set()

top.mainloop()     # queda esperando eventos
