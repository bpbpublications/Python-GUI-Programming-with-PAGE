#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Dec 21, 2022 05:06:43 AM CST  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import datepicker_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class Main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+893+500")
        top.minsize(1, 1)
        top.maxsize(4225, 1410)
        top.resizable(0,  0)
        top.title("Tk DatePicker Demo")
        top.configure(background="skyblue")
        top.configure(highlightcolor="black")

        self.top = top
        self.PopupReturn = tk.StringVar()
        self.lblPopupReturn = tk.StringVar()
        self.lblPulldownReturn = tk.StringVar()

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(x=40, y=140, height=23, width=136)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(textvariable=self.PopupReturn)
        self.Button1 = tk.Button(self.top)
        self.Button1.place(x=179, y=136, height=33, width=143)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(command=datepicker_support.on_showCalendar)
        self.Button1.configure(compound='left')
        self.Button1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Button1.configure(text='''Show Calendar''')
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(x=352, y=140, height=25, width=190)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Custom1 = datepicker_support.Custom(self.Frame1)
        self.Custom1.place(x=0, y=0, height=25, width=190)
        self.btnExit = tk.Button(self.top)
        self.btnExit.place(x=470, y=20, height=33, width=93)
        self.btnExit.configure(activebackground="springgreen3")
        self.btnExit.configure(borderwidth="2")
        self.btnExit.configure(command=datepicker_support.on_btnExit)
        self.btnExit.configure(compound='left')
        self.btnExit.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.btnExit.configure(text='''Exit''')
        self.Label1 = tk.Label(self.top)
        self.Label1.place(x=40, y=117, height=21, width=140)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="skyblue")
        self.Label1.configure(compound='left')
        self.Label1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label1.configure(text='''Popup Datepicker''')
        self.Label2 = tk.Label(self.top)
        self.Label2.place(x=350, y=117, height=21, width=161)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="skyblue")
        self.Label2.configure(compound='left')
        self.Label2.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label2.configure(text='''Pulldown Datepicker''')
        self.Label3 = tk.Label(self.top)
        self.Label3.place(x=40, y=250, height=21, width=119)
        self.Label3.configure(anchor='e')
        self.Label3.configure(background="skyblue")
        self.Label3.configure(compound='left')
        self.Label3.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label3.configure(text='''Popup Return:''')
        self.Label4 = tk.Label(self.top)
        self.Label4.place(x=20, y=305, height=21, width=143)
        self.Label4.configure(anchor='e')
        self.Label4.configure(background="skyblue")
        self.Label4.configure(compound='left')
        self.Label4.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label4.configure(text='''Pulldown Return:''')
        self.Label5 = tk.Label(self.top)
        self.Label5.place(x=170, y=245, height=31, width=159)
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="skyblue")
        self.Label5.configure(compound='left')
        self.Label5.configure(relief="sunken")
        self.Label5.configure(text='''Label''')
        self.Label5.configure(textvariable=self.lblPopupReturn)
        self.lblPopupReturn.set('''Label''')
        self.Label6 = tk.Label(self.top)
        self.Label6.place(x=170, y=300, height=31, width=159)
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="skyblue")
        self.Label6.configure(compound='left')
        self.Label6.configure(relief="sunken")
        self.Label6.configure(text='''Label''')
        self.Label6.configure(textvariable=self.lblPulldownReturn)
        self.lblPulldownReturn.set('''Label''')

def start_up():
    datepicker_support.main()

if __name__ == '__main__':
    datepicker_support.main()




