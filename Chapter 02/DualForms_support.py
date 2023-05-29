#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.0
#  in conjunction with Tcl version 8.6
#    Dec 28, 2021 04:42:36 AM CST  platform: Linux
#    Feb 01, 2022 02:11:35 PM CST  platform: Linux

import sys
import shared
# ===================================
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import DualForms


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = DualForms.MainForm(_top1)
    # Creates a toplevel widget.
    global _top2, _w2
    _top2 = tk.Toplevel(root)
    _w2 = DualForms.ChildForm(_top2)
    # Creates a toplevel widget.
    global _top3, _w3
    _top3 = tk.Toplevel(root)
    _w3 = DualForms.Splash(_top3)
    startup()
    root.mainloop()


def startup():
    shared.childrunning = False
    shared.childruncount = 0
    shared.passback = ''
    hide_Main()
    hide_Form2()
    _top3.overrideredirect(True)  # Hide the 'decorations'
    delay = 10000
    timerID = _top3.after(delay, on_tick)
    centre_screen(798, 450, _top3)


def centre_screen(wid, hei, which):
    ws = which.winfo_screenwidth()
    hs = which.winfo_screenheight()
    print(f'Width: {ws} - Height {hs}')
    x = (ws / 2) - (wid / 2)
    y = (hs / 2) - (hei / 2)
    which.geometry('%dx%d+%d+%d' % (wid, hei, x, y))


def on_tick():
    # ======================================================
    # Once the 'timer' hits, hide the splash screen
    # ======================================================
    # root.withdraw()
    hide_Splash()
    # ======================================================
    #   Call the ShowMe routine in the main support file
    # ======================================================
    show_Main()


def on_btnDismiss(*args):
    print('DualForms_support.on_btnDismiss')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()
    hide_Form2()
    shared.passback = _w2.PassBack.get()
    if shared.passback != '':
        _w1.SecondFormData.set(shared.passback)
    _w1.che46.set(1)
    show_Main()


def on_btnExit(*args):
    print('DualForms_support.on_btnExit')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()
    root.destroy()


def on_btnLaunch(*args):
    print('DualForms_support.on_btnLaunch')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()
    hide_Main()
    shared.childruncount += 1
    _w2.RunCount.set(shared.childruncount)
    shared.passback = ''
    _w2.PassBack.set('')
    show_Form2()


def show_Main():
    # pass
    _top1.deiconify()


def hide_Main():
    # pass
    _top1.withdraw()


def show_Form2():
    # pass
    _top2.deiconify()


def hide_Form2():
    # pass
    _top2.withdraw()


def show_Splash():
    # pass
    _top3.deiconify()


def hide_Splash():
    # pass
    _top3.withdraw()


if __name__ == '__main__':
    DualForms.start_up()
