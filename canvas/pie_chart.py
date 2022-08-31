def ang(n, t):
    return 360.0 * n / t

import tkinter

ancho = 512
alto = 512
margen = 2

v1 = 25
v2 = 25
v3 = 50
v4 = 25
total = v1 + v2 + v3 + v4

c = tkinter.Canvas(width=ancho, height=alto);

coor = margen, margen, ancho - margen, alto - margen

c.create_arc(coor, fill="red", start=0, extent=ang(v1, total))
c.create_arc(coor, fill="blue", start=ang(v1, total), extent=ang(v2, total))
c.create_arc(coor, fill="green", start=ang(v1 + v2, total), extent=ang(v3, total))
c.create_arc(coor, fill="light sea green", start=ang(v1 + v2+v3, total), extent=ang(v4, total))

c.grid(row=0, column=0)

c.mainloop()
