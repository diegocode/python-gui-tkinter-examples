import tkinter

valores = ((80, 'red'), (300, 'blue'), (150, 'green'), (70, 'orange'))

ANCHO = 512
ALTO = 512
MARGEN = 20

def calcula_angulo(n, t):
    return (360.0 * n) / t

mw = tkinter.Tk()
cnv = tkinter.Canvas(mw, width=ANCHO, height=ALTO);

coor = MARGEN, MARGEN, ANCHO - MARGEN, ALTO - MARGEN

total = sum([x[0] for x in valores])

acumulado = 0
for valor in valores:
    cnv.create_arc(coor,
                   fill=valor[1],
                   outline=valor[1],
                   start=calcula_angulo(acumulado, total),
                   extent=calcula_angulo(valor[0], total),
                   )
    acumulado += valor[0]

cnv.grid(row=0, column=0, padx=15, pady=15)

mw.mainloop()
