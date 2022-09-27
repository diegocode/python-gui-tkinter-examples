import tkinter
from tkinter import messagebox, simpledialog

BG_COLOR = '#00CC33'
FG_COLOR = 'blue'
BG_COLOR_ALERT = 'red'

BTN_WIDTH = 40
BTN_WIDTH_ALERT = 30
BTN_HEIGHT = 4
BTN_BORDER_WIDTH = 3

mw = tkinter.Tk()
mw.title("muestra")

#mw.geometry('400x250')

def calcula():
    flg_cancel_close = False
    suma = 0
    for n_numero in 1,2:
        numero = simpledialog.askfloat(f"Número {n_numero}",
                                        "Ingrese un número entre -10.0 y 10.0",
                                       minvalue=-10,
                                       maxvalue=10)
        if numero == None:
            flg_cancel_close = True
        else:
            suma += numero

    if not flg_cancel_close:
        messagebox.showinfo("Resultado", str(suma))


def salir():
    btnSalir.configure(width=BTN_WIDTH_ALERT)  # cambia el ancho del botón
    btnSalir.configure(bg=BG_COLOR_ALERT)  # cambia el color del boton
    flg_salir = messagebox.askyesno("Atención", "¿Confirma salir?")
    if flg_salir:
        mw.destroy()  # termina y borra la aplicación de la memoria
    else:
        btnSalir.configure(width=BTN_WIDTH)  # restaura ancho original del boton
        btnSalir.configure(bg=BG_COLOR)  # restaura color original del boton


btnCalcular = tkinter.Button(mw, text="Suma de dos números",
                             command=calcula,
                             width=BTN_WIDTH,
                             height=BTN_HEIGHT,
                             bd=BTN_BORDER_WIDTH,
                             bg=BG_COLOR,
                             fg=FG_COLOR)

btnSalir = tkinter.Button(mw, text="Salir",
                          command=salir,
                          width=BTN_WIDTH,
                          height=BTN_HEIGHT,
                          bd=BTN_BORDER_WIDTH,
                          bg=BG_COLOR,
                          fg=FG_COLOR)

btnCalcular.grid(row=0, column=0, padx=20, pady=20)
btnSalir.grid(row=1, column=0, padx=20, pady=20)

mw.mainloop()

