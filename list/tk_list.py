import tkinter
from tkinter import messagebox

# callback para doble-click en item
def ver_item_CB():
    item_string = lstOpciones.get(lstOpciones.curselection())
    messagebox.showinfo("item", item_string)

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
        r = messagebox.askyesno("Atención","¿Confirma borrar?\n" + s + "?", default=messagebox.NO)

        if r:
            # si confirma, borra el elemento seleccionado
            lstOpciones.delete(ind)

    # coloca el foco en txtItem
    txtItem.focus_set()


# callback para botón btnSalir
def btnSaleCB():
    # muestra pop-up de confirmación
    if messagebox.askyesno("Atención","¿Confirma cerrar el programa?", default=messagebox.NO):
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

def btnLimpiarCB():
    r = messagebox.askyesno("Atención","¿Confirma borrar?\ntodos los elementos?", default=messagebox.NO)

    if r:
        # si confirma, borra todos los elementos
        lstOpciones.delete(0, tkinter.END)


top = tkinter.Tk()
top.title("una lista")

scrVert = tkinter.Scrollbar(top, orient=tkinter.VERTICAL)

# crea Listbox
lstOpciones = tkinter.Listbox(top, yscrollcommand=scrVert.set)

scrVert.config(command=lstOpciones.yview)

frameBotones = tkinter.Frame(top, bd=1, relief=tkinter.SUNKEN)

# crea Button btnAgregar
btnAgregar = tkinter.Button(top, text="Agregar", underline=0, command=btnAgregaCB)
# vincula Alt izquierdo + a con función "btnAgregaCB"
top.bind('<Alt_L><a>', lambda e:btnAgregaCB())

# crea btnBorrar
btnBorrar = tkinter.Button(frameBotones, text="Borrar", underline=0, command=btnBorraCB)
# vincula Alt izquierdo + b con función "btnBorraCB"
top.bind('<Alt_L><b>', lambda e:btnBorraCB())

btnVer = tkinter.Button(frameBotones, text="Ver", underline=0, command=ver_item_CB)
top.bind('<Alt_L><v>', lambda e:ver_item_CB())

btnLimpiar = tkinter.Button(frameBotones, text="Limpiar", underline=0, command=btnLimpiarCB)
top.bind('<Alt_L><l>', lambda e:btnLimpiarCB())

# crea btnSalir
btnSalir = tkinter.Button(frameBotones, text="Salir", underline=0, command=btnSaleCB)
# vincula Alt izquierdo + s con función "btnSaleCB"
top.bind('<Alt_L><s>', lambda e:btnSaleCB())

txtItem = tkinter.Entry(top)


# posiciona cada widget en columna y fila correspondiente
txtItem.grid(row=0, column=0, columnspan=2, sticky="WE")
lstOpciones.grid(row=1, column=0, rowspan=4, sticky="WE")
scrVert.grid(row=1, column=1, rowspan=4, sticky="NS")
btnAgregar.grid(row=0, column=2, sticky="WE")

frameBotones.grid(row=1, column=2, sticky="NSEW")

btnVer.grid(row=0, column=0, sticky="WE")
btnBorrar.grid(row=1, column = 0, sticky='WE')
btnLimpiar.grid(row=2, column=0)
btnSalir.grid(row=3, column = 0, sticky='WE')
#frameBotones.grid_propagate(0)

# coloca el foco en txtItem
txtItem.focus_set()

# agrega algunos elementos a la lista
for item in range(1, 15):
    lstOpciones.insert(tkinter.END, str(item))

top.mainloop()     # queda esperando eventos
