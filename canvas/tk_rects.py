#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

import tkinter

root = tkinter.Tk()
root.geometry("400x300+300+300")
    
canvas = tkinter.Canvas(root)
canvas.config(width=400, height=300)
canvas.create_rectangle(20, 20, 380, 280, outline="#fb0", fill="#fb0")
canvas.create_rectangle(40, 40, 360, 260, outline="#f50", fill="#f50")
canvas.create_rectangle(60, 60, 340, 240, outline="#05f", fill="#05f")

canvas.grid(row=0, column=0)
root.mainloop()
