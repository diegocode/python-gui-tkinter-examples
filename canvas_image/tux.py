#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter 
from tkinter import Canvas, PhotoImage

posx = 0
posy = 0
margen = 5

root = tkinter.Tk()

img = PhotoImage(file="tux.gif")

w = int(img.width() )
h = int(img.height() )

root.geometry(f"{w}x{h + 100}")

cnv = tkinter.Canvas(root, bg="#dddddd", height=h + 100, width=w)

t = cnv.create_text(w // 2, h + 50, text="Tux", fill="#cc0000", font="Arial 48 bold")

cnv.create_rectangle(posx, 
                     posy, 
                     posx + w, 
                     posy + h, 
                     fill="white", 
                     outline="#cc0000", 
                     width=3)
                     
image = cnv.create_image(
                     w // 2 + posx, 
                     h // 2 + posy, 
                     image= img)

cnv.grid(column=0, row=0)

root.mainloop()

