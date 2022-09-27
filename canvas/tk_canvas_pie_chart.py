import tkinter
import math
import cmath

valores = (
           (100, 'red', 'the first label\n is red'),
           (100, 'blue', 'numer zwei'),
           (50, 'green', 'tercero'),
           (50, 'orange', 'IV')
          )

MARGEN = 20
ANCHO = 512
ALTO = ANCHO

def calcula_angulo(n, t):
    return (360.0 * n) / t

mw = tkinter.Tk()
cnv = tkinter.Canvas(mw, width=ANCHO, height=ALTO, bg='#B48662');

coor = MARGEN, MARGEN, ANCHO - MARGEN, ALTO - MARGEN

total = sum([x[0] for x in valores])

radius = (ANCHO - MARGEN) / 2
center_offset = radius

acumulado = 0
for valor in valores:
    arc_start = calcula_angulo(acumulado, total)
    arc_extent = calcula_angulo(valor[0], total)
    cnv.create_arc(coor,
                   fill=valor[1],
                   outline=valor[1],
                   start= arc_start,
                   extent=arc_extent,
                   )

    angulo = math.radians(arc_extent / 2 + arc_start)
    pos_label = cmath.rect(radius, angulo) * 0.5

    cnv.create_text(center_offset + (+1 * pos_label.real),
                   center_offset + (-1 * pos_label.imag),
                   text=valor[2],
                   anchor=tkinter.CENTER)

    acumulado += valor[0]


cnv.grid(row=0, column=0, padx=15, pady=15)

mw.mainloop()
