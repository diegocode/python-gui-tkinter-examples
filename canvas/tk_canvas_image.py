#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
from tkinter import Canvas, PhotoImage

filename = "images/tux.gif"

root = tkinter.Tk()
root.title(filename)

img = PhotoImage(file=filename)

img_width = int(img.width() )
img_height = int(img.height() )

root.geometry(f"{img_width}x{img_height}")

cnv = tkinter.Canvas(root, bg="#dddddd", height=img_height, width=img_width)

cnv.create_image(0, 0 , image=img, anchor=tkinter.NW)

cnv.grid(column=0, row=0)

root.mainloop()

