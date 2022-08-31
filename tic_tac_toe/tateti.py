import tkinter
from tkinter import messagebox

mw = tkinter.Tk()

# lista para guardar botones
buttons = []


def reset():
    """
    establece condiciones para 
    inicio de partida
    
    """
    global turno
    
    for n, b in enumerate(buttons):
        b.config(text=str(n+1))
        
    turno = 1


def verificar():
    """
    verifica si hubo ganador o empate
    
    """
    f = []
    for b in buttons:
        f.append(b.cget("text"))
        
    ganador = ""
    if f[0] == f[1] == f[2]:
        ganador = f[0]
    elif f[3] == f[4] == f[5]:
        ganador = f[3]
    elif f[6] == f[7] == f[8]:
        ganador = f[6]
    elif f[0] == f[3] == f[6]:
        ganador = f[0]
    elif f[1] == f[4] == f[7]:
        ganador = f[1]
    elif f[2] == f[5] == f[8]:
        ganador = f[2]
    elif f[0] == f[4] == f[8]:
        ganador = f[0]
    elif f[6] == f[4] == f[2]:    
        ganador = f[2]

    if ganador != "":
        messagebox.showinfo(
            "ganador",
            "el ganador es " + ganador
            )
    
        reset()
   
    elif len(set(f)) < 3:
        messagebox.showinfo(
            "empate",
            "hubo un empate"
            )
    
        reset()        


# turno -> el jugador que tiene que jugar
# 1 para O   
# 2 para X
turno = 1


def press(n):
    """ calback de botón, 
        marca X o O 
        y verifica ganador o empate
    """
    global turno
    if buttons[n].cget("text") in "XO":
        #buttons[n].config(text=str(n + 1))
        pass
    elif turno == 1:
        buttons[n].config(text="O")
        turno = 2
    else:
        buttons[n].config(text="X")
        turno = 1

    verificar()


# crea en la lista buttons
# los botones que representan los casilleros
for n in range(9):
    b = tkinter.Button(mw,
                text=f'{n + 1}',  
                command=lambda p=n: press(p), 
        )
    buttons.append(b)
    
    
# ubica en la ventana y configura cada botón
for r in range(3):
    for c in range(3):
        buttons[r * 3 + c].grid(row=r, column=c)
        buttons[r * 3 + c].config(width=3, height=3)

    
mw.mainloop()
