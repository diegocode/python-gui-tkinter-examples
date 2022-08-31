# importamos los módulos que necesitamos: tkinter...
import tkinter

# ...y messagebox para el cuadro de mensaje
from tkinter import messagebox

# callback del botón Saludar (btnSaludar)
# esta función se ejecuta cuando se presiona el botón saludar
def btnSaludaCB():
    if len(str(txtNombre.get()).strip()) < 1:
        # muestra popup de error 
        messagebox.showerror("Atención", 
                             "Debe ingresar un nombre")
    else:
        s = "Hola " + txtNombre.get() 

        if flgSonrisa.get() == 1:
                s = s + " :) "    
        s = s + "!!!"
        
        # muestra el popup con el saludo
        messagebox.showinfo("Saludo", s)
    
    # vuelve el foco al Entry
    txtNombre.focus_set()

# ventana principal (raíz / root) 
# va a contener el resto de los widgets
top = tkinter.Tk()    
# le cambiamos el título    
top.title("Saludador")    
# deshabilita resize
top.resizable(False, False)

# botón 
btnSaludar = tkinter.Button(top, text="Saludar", command=btnSaludaCB)

# asigna ALT izq + s como shortcut para el botón
top.bind('<Alt_L><s>', lambda e:btnSaludaCB())

# texto estático (Label)
lblAQuien = tkinter.Label(top, text = "¿A quién saludamos?")

# entrada de texto (Entry)
txtNombre = tkinter.Entry(top)

# variable para saber si checkbutton está marcado o no 
flgSonrisa = tkinter.IntVar()       
# checkbutton
chkSonrisa = tkinter.Checkbutton(top, 
                                 text = "Agregar :)", 
                                 variable = flgSonrisa, 
                                 height = 3)

# posiciona cada widget en columna y la fila correspondiente
chkSonrisa.grid(row=2, column=0, columnspan=2)
# posiciona cada widget en columna y fila correspondiente
lblAQuien.grid(row=0, column=0, sticky=tkinter.W, 
                                columnspan=2, 
                                padx=50, 
                                pady=10)
txtNombre.grid(row=1, column=0, sticky=tkinter.E, 
                                padx=5)
btnSaludar.grid(row=1, column=1, sticky=tkinter.E, 
                                 padx=(0, 5))
chkSonrisa.grid(row=2, column=0, sticky=tkinter.W, 
                                columnspan=2)
# queda esperando eventos
top.mainloop() 
