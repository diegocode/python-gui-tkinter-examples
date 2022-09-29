import tkinter as tk
import datetime

SEG_CUENTA = 10

def dar_fecha_hora_iso8601():
    return datetime.datetime.now().replace(microsecond=0).isoformat()

def descuenta():
    if segundos.get() >0:
        segundos.set(segundos.get() - 1)

    tiempo.set(dar_fecha_hora_iso8601())
    mw.after(1000, descuenta)


mw = tk.Tk()
mw.title("timer")

segundos = tk.IntVar()
segundos.set(SEG_CUENTA)
lblTiempo = tk.Label(mw, textvar=segundos, font='Arial 36 bold')

tiempo = tk.StringVar()
tiempo.set(dar_fecha_hora_iso8601())
lblHora = tk.Label(mw, textvar=tiempo, font='Arial 18 bold')

lblTiempo.grid(row=0, column=0, pady=10)
lblHora.grid(row=2, column=0, pady=10)

mw.after(1000, descuenta)

mw.mainloop()
