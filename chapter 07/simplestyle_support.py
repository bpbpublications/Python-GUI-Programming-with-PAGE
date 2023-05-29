#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Dec 15, 2022 11:28:03 AM CST  platform: Linux
#    Dec 15, 2022 12:10:10 PM CST  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import simplestyle

_debug = True  # False to eliminate debug printing from callback functions.


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = simplestyle.Toplevel1(_top1)
    startup()
    root.mainloop()


def startup():
    style = ttk.Style()

    my_styles(style)
    global plain
    plain = True


def my_styles(sty):
    sty.map('my.TButton',
            background=[("disabled", "#d9d9d9"), ("active", "seagreen2")],
            foreground=[
                ("disabled", "gray45"),
                ("active", "gray6"),
            ])

    my_map = sty.map('my.TButton',
                     background=[("disabled", "#d9d9d9"),
                                 ("active", "seagreen2")],
                     foreground=[
                         ("disabled", "gray45"),
                         ("active", "gray6"),
                     ])
    print(type(my_map))
    sty.configure(
        "my.TButton",
        foreground="white",
        background="cornflowerblue",
        relief=RAISED,
        borderwidth=3,
        padding=[4, 4, 4, 4],
        font="Ubuntu 12 bold",
    )


def on_btnMyStyle(*args):
    if _debug:
        print('simplestyle_support.on_btnMyStyle')
        for arg in args:
            print('    another arg:', arg)
        sys.stdout.flush()
    global plain
    if plain:
        _w1.TButton1.configure(text="My TButton Style", style="my.TButton")
        _w1.btnMyStyle.configure(text="Remove My Style")
        plain = False
    else:
        _w1.TButton1.configure(text="My TButton Style", style="TButton")
        _w1.btnMyStyle.configure(text="Apply My Style")
        plain = True


if __name__ == '__main__':
    simplestyle.start_up()