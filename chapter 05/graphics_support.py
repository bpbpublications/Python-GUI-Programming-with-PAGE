#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Sep 04, 2022 04:51:42 PM CDT  platform: Linux

import sys
import os
import platform
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox

import graphics


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = graphics.Toplevel1(_top1)
    startup()
    root.mainloop()


def startup():
    global version
    pv = platform.python_version()
    print(f"Running under Python {pv}")
    # Set the path for the icon files
    version = '0.0.2'
    print(f"Version: {version}")
    progloc = graphics._location
    global graphloc
    graphloc = os.path.join(progloc, "Assets")
    print(f'Program Location: {progloc}')
    print(f'Graphics Location: {graphloc}')
    # =====================================
    # Now manually add the graphics to the remaining widgets
    # =====================================
    # Define the global variables we need to keep
    # =====================================
    global img1, img2, img3, img4

    filename = os.path.join(graphloc, 'edit-paste.png')
    img1 = tk.PhotoImage(file=filename)
    _w1.Button2.configure(image=img1)
    _w1.Button2.configure(compound=RIGHT)
    _w1.Label7.configure(anchor=W)
    _w1.Label7.configure(text='Tk Button - Compound Right')
    _w1.Label7.configure(wraplength=145)

    filename = os.path.join(graphloc, 'edit-undo.png')
    img2 = tk.PhotoImage(file=filename)
    _w1.Label6.configure(image=img2)
    _w1.Label6.configure(compound=LEFT)
    _w1.Label8.configure(anchor=W)
    _w1.Label8.configure(text='Tk Label - Compound Left')
    _w1.Label8.configure(wraplength=125)

    filename = os.path.join(graphloc, 'insert-text.png')
    img3 = tk.PhotoImage(file=filename)
    _w1.TButton2.configure(image=img3)
    _w1.TButton2.configure(compound=BOTTOM)
    _w1.Label9.configure(anchor=W)
    _w1.Label9.configure(text='ttk TButton - Compound Bottom')
    _w1.Label9.configure(wraplength=120)

    filename = os.path.join(graphloc, 'notebook.png')
    img4 = tk.PhotoImage(file=filename)
    _w1.TLabel2.configure(image=img4)
    _w1.TLabel2.configure(compound=TOP)
    _w1.TLabel2.configure(anchor=CENTER)
    _w1.Label10.configure(anchor=W)
    _w1.Label10.configure(text='ttk TLabel - Compound Top')
    _w1.Label10.configure(wraplength=145)


def on_mnu_Click_me(*args):
    print('graphics_support.on_mnu_Click_me')
    for arg in args:
        print('    another arg:', arg)
    sys.stdout.flush()
    titl = "Graphics Demo"
    msg = "You clicked on the menu item"
    messagebox.showinfo(titl, msg, icon=messagebox.INFO, parent=_top1)


if __name__ == '__main__':
    graphics.start_up()
