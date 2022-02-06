import os
import tkinter as tk
from tkinter import ttk
from PIL import Image
import subprocess as s

def Watermark():
    print('Activate')
    s.Popen([r"Mark.py", ], shell=True)

def app():
    global set,var
    root = tk.Tk()
    root.title('Bulk Watermarker')
    root.resizable(False, False)
    root.geometry('300x150')
    root.iconbitmap('py_logo.ico')
    root.eval('tk::PlaceWindow . center')
    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "dark")

    spacer0 = ttk.Label(root, text='')
    spacer0.pack()
    li1 = ttk.Label(root, text=f'Image Amount: {len(os.listdir("images"))}')
    li1.pack()

    spacer1 = ttk.Label(root, text='')
    spacer1.pack()
    bulk = ttk.Button(root, text='Watermark images', command=lambda:Watermark())
    bulk.pack()
    spacer2 = ttk.Label(root, text='')
    spacer2.pack()

    tk.mainloop()

if __name__ == '__main__':
    app()

