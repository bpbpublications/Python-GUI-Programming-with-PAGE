#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Sep 29, 2022 04:28:40 AM CDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import graphics_support

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

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x474+745+399")
        top.minsize(1, 1)
        top.maxsize(4225, 1410)
        top.resizable(1,  1)
        top.title("Chapter 5 Graphics")
        top.configure(highlightcolor="black")

        self.top = top
        self.che46 = tk.IntVar()
        self.selectedButton = tk.IntVar()

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.283, rely=0.063, height=48, width=116)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(compound='left')
        photo_location = os.path.join(_location,"./Assets/applications-graphics.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img0)
        self.Button1.configure(text='''Button''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.283, rely=0.232, height=42, width=102)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(borderwidth="2")
        self.Label1.configure(compound='right')
        photo_location = os.path.join(_location,"./Assets/edit-clear.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img1)
        self.Label1.configure(padx="8")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='''Label''')

        _style_code()
        self.TButton1 = ttk.Button(self.top)
        self.TButton1.place(relx=0.283, rely=0.35, height=64, width=83)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Tbutton''')
        photo_location = os.path.join(_location,"./Assets/internet.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.TButton1.configure(image=_img2)
        self.TButton1.configure(compound='top')

        self.TLabel1 = ttk.Label(self.top)
        self.TLabel1.place(relx=0.283, rely=0.549, height=62, width=82)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="groove")
        self.TLabel1.configure(anchor='center')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Tlabel''')
        photo_location = os.path.join(_location,"./Assets/system-run.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.TLabel1.configure(image=_img3)
        self.TLabel1.configure(compound='bottom')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top, activebackground='beige'
                ,activeforeground='black', tearoff=0)
        self.menubar.add_cascade(label='Image Menu Item',menu=self.sub_menu,)
        photo_location = os.path.join(_location,"./Assets/information.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.sub_menu.add_command(command=graphics_support.on_mnu_Click_me
                ,compound='left', image=_img4, label='Click me!')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.083, rely=0.021, height=91, width=109)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='e')
        self.Label2.configure(compound='left')
        self.Label2.configure(justify='right')
        self.Label2.configure(text='''Tk Button - Compound left, Anchor w''')
        self.Label2.configure(wraplength="140")

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.083, rely=0.232, height=38, width=108)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='e')
        self.Label3.configure(compound='left')
        self.Label3.configure(justify='right')
        self.Label3.configure(text='''Tk Label - Compound right''')
        self.Label3.configure(wraplength="130")

        self.Label4 = tk.Label(self.top)
        self.Label4.place(relx=0.083, rely=0.373, height=38, width=102)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor='e')
        self.Label4.configure(compound='left')
        self.Label4.configure(justify='right')
        self.Label4.configure(text='''ttk Button - Compound Top''')
        self.Label4.configure(wraplength="145")

        self.Label5 = tk.Label(self.top)
        self.Label5.place(relx=0.033, rely=0.57, height=38, width=126)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(anchor='e')
        self.Label5.configure(compound='left')
        self.Label5.configure(justify='right')
        self.Label5.configure(text='''ttk TLabel - Compound Bottom''')
        self.Label5.configure(wraplength="145")

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.5, rely=0.063, height=48, width=116)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(compound='left')
        self.Button2.configure(text='''Button''')

        self.Label6 = tk.Label(self.top)
        self.Label6.place(relx=0.5, rely=0.232, height=42, width=102)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(anchor='w')
        self.Label6.configure(compound='left')
        self.Label6.configure(relief="groove")
        self.Label6.configure(text='''Label''')

        self.TButton2 = ttk.Button(self.top)
        self.TButton2.place(relx=0.5, rely=0.35, height=64, width=83)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Tbutton''')
        self.TButton2.configure(compound='left')

        self.TLabel2 = ttk.Label(self.top)
        self.TLabel2.place(relx=0.5, rely=0.549, height=62, width=82)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="groove")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Tlabel''')
        self.TLabel2.configure(compound='left')

        self.Label7 = tk.Label(self.top)
        self.Label7.place(relx=0.75, rely=0.015, height=91, width=109)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(anchor='w')
        self.Label7.configure(compound='left')
        self.Label7.configure(text='''Label''')

        self.Label8 = tk.Label(self.top)
        self.Label8.place(relx=0.733, rely=0.181, height=91, width=109)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(anchor='w')
        self.Label8.configure(compound='left')
        self.Label8.configure(text='''Label''')

        self.Label9 = tk.Label(self.top)
        self.Label9.place(relx=0.733, rely=0.329, height=91, width=109)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(anchor='w')
        self.Label9.configure(compound='left')
        self.Label9.configure(text='''Label''')

        self.Label10 = tk.Label(self.top)
        self.Label10.place(relx=0.717, rely=0.517, height=91, width=109)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(anchor='w')
        self.Label10.configure(compound='left')
        self.Label10.configure(text='''Label''')

        self.Checkbutton1 = tk.Checkbutton(self.top)
        self.Checkbutton1.place(relx=0.167, rely=0.759, relheight=0.07
                , relwidth=0.212)
        self.Checkbutton1.configure(activebackground="beige")
        self.Checkbutton1.configure(anchor='w')
        self.Checkbutton1.configure(borderwidth="0")
        self.Checkbutton1.configure(compound='left')
        photo_location = os.path.join(_location,"./Assets/checkbox-unchecked.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.Checkbutton1.configure(image=_img5)
        self.Checkbutton1.configure(indicatoron="0")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(padx="4")
        self.Checkbutton1.configure(selectcolor="#d9d9d9")
        photo_location = os.path.join(_location,"./Assets/checkbox-checked.png")
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        self.Checkbutton1.configure(selectimage=_img6)
        self.Checkbutton1.configure(text='''Check''')
        self.Checkbutton1.configure(variable=self.che46)

        self.Radiobutton1 = tk.Radiobutton(self.top)
        self.Radiobutton1.place(relx=0.167, rely=0.844, relheight=0.07
                , relwidth=0.23)
        self.Radiobutton1.configure(activebackground="beige")
        self.Radiobutton1.configure(anchor='w')
        self.Radiobutton1.configure(borderwidth="0")
        self.Radiobutton1.configure(compound='left')
        photo_location = os.path.join(_location,"./Assets/radio-unchecked.png")
        global _img7
        _img7 = tk.PhotoImage(file=photo_location)
        self.Radiobutton1.configure(image=_img7)
        self.Radiobutton1.configure(indicatoron="0")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(padx="4")
        self.Radiobutton1.configure(selectcolor="#d9d9d9")
        photo_location = os.path.join(_location,"./Assets/radio-checked.png")
        global _img8
        _img8 = tk.PhotoImage(file=photo_location)
        self.Radiobutton1.configure(selectimage=_img8)
        self.Radiobutton1.configure(text='''Radio''')
        self.Radiobutton1.configure(value='1')
        self.Radiobutton1.configure(variable=self.selectedButton)

def start_up():
    graphics_support.main()

if __name__ == '__main__':
    graphics_support.main()




