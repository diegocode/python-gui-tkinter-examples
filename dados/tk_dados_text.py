import tkinter
import random

CANT_DADOS = 3

mw = tkinter.Tk()

# lista donde guardo los dados
dados = []


def tira_dados():
    # genera número aleatorio para cada dado
    for d in dados:
        d.config(text=str(random.randint(1, 6)))


# crea los dados
for n in range(CANT_DADOS):
    b = tkinter.Button(mw, text="?")
    dados.append(b)

# crea botón
btnJuega = tkinter.Button(mw, text="Jugar", command=tira_dados)

# ubica los dados en la ventana
c = 0
for d in dados:
    d.grid(row = 0, column = c)
    d.config(width=3, height=3)
    c += 1

# ubica el botón en la ventana
btnJuega.grid(row=1, column=0, columnspan=c, pady=(10, 10), sticky="WE")
btnJuega.config(width=10)

mw.mainloop()
