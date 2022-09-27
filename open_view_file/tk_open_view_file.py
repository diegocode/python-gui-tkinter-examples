import tkinter as tk
from tkinter import filedialog as fd

def ver_archivo():
    tipos = (
                ('archivos python', '*.py'),
                ('de texto', '*.txt'),
            )

    nombre = fd.askopenfilename(
                            title="Abrir archivo",
                            filetypes= tipos,
                        )

    if len(nombre) > 0:
        txtArchivo.delete(1.0, tk.END)
        mw.title(nombre)
        with open(nombre, "r") as f:
            s = ""
            for linea in f:
                s += linea

            txtArchivo.insert('1.0', s)

def limpiar():
    txtArchivo.delete(1.0, tk.END)
    mw.title('archivo: ?')


mw = tk.Tk()
mw.title('archivo: ?')

txtArchivo = tk.Text(mw)

btnArchivo = tk.Button(mw,
                        text="abrir",
                       command=ver_archivo,
                        )

btnLimpiar = tk.Button(mw,
                        text="limpiar",
                        command=limpiar,
                       )

txtArchivo.grid(row=0,
                 column=0,)

btnArchivo.grid(row=1,
                 column=0,
                 pady = (5, 5), padx=(10, 10),
                 sticky="WE")

btnLimpiar.grid(row=2,
                 column=0,
                 pady = (5, 15), padx=(10, 10),
                 sticky="WE")

mw.mainloop()
