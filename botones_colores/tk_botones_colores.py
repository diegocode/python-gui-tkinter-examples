import tkinter
from tkinter import messagebox, simpledialog

mw = tkinter.Tk()
mw.title("muestra")
mw.geometry('400x250')

def calcula():
    a = simpledialog.askfloat("Número 1", "Ingrese un número entre -10.0 y 10.0", minvalue=-10, maxvalue=10)
    b = simpledialog.askfloat("Número 2", "Ingrese un número entre -10.0 y 10.0", minvalue=-10, maxvalue=10)
    messagebox.showinfo("Resultado", str(a + b))
    
def salir():
    btnSalir.configure(width=20)  # cambia el ancho del botón
    btnSalir.configure(bg='red')  # cambia el color del boton
    ans = messagebox.askyesno("Atención", "¿Confirma salir?")
    if ans == True:
        mw.destroy()  # termina y borra la aplicación de la memoria
    else:
        btnSalir.configure(width=40)  # restaura ancho original del boton
        btnSalir.configure(bg='#00CC33')  # restaura color original del boton

btnSalir = tkinter.Button(mw, text="salir", command=salir, width=40, height=4, bd=3, bg='#00CC33',  fg='blue')
btnCalcular = tkinter.Button(mw, text="calcu", command=calcula, width=40, height=4, bd=3, bg='#00CC33',  fg='blue')

btnSalir.grid(row=0, column=0, padx=20, pady=20)
btnCalcular.grid(row=1, column=0, padx=20, pady=20)

mw.mainloop()

