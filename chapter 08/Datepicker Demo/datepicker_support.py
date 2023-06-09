#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Dec 21, 2022 04:47:17 AM CST  platform: Linux
#    Dec 21, 2022 04:58:25 AM CST  platform: Linux

import sys

try:
    from tkcalendar import Calendar, DateEntry
except ImportError:
    # If the library is not installed, show error message to user and abort.
    print("~" * 50)
    print('This program requires the third party library "tkcalendar". \n')
    print(
        ' You can install it by typing "pip install tk-datepicker" \n\
          in a terminal or command prompt.'
    )
    print("\n  Program ends.")
    print("~" * 50)
    sys.exit(1)

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import datepicker

_debug = True  # False to eliminate debug printing from callback functions.

def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = datepicker.Main(_top1)
    startup()
    root.mainloop()

def startup():

    # ===================================================
    # For more information see - https://pypi.org/project/tk-datepicker/
    # ===================================================
    _w1.lblPulldownReturn.set("")
    # _w1.lblPopupReturn.set("")
    _w1.lblPopupReturn.set("")
    global style
    style = ttk.Style()
    style.configure(
        "my.DateEntry",
        fieldbackground="light green",
        background="dark green",
        foreground="dark blue",
        arrowcolor="white",
    )
    # If you wish to set the date locale and pattern, this MUST be done before
    # setting the firstweekday and weekenddays attributes...
    _w1.Custom1.configure(locale="en_US")
    _w1.Custom1.configure(date_pattern="MM/dd/yyyy")
    # _w1.Custom1.configure(date_pattern='%m/%d/%Y')
    # For locations that use Sunday as the first day of the week, otherwise
    # firstweekday='monday'
    _w1.Custom1.configure(firstweekday="sunday")
    # Weekenddays in U.S.A are Sunday and Saturday.  For other locations,
    # the weekenddays would be [6, 7]
    _w1.Custom1.configure(weekenddays=[1, 7])
    # Set the ttk style for the control
    _w1.Custom1.configure(style="my.DateEntry")
    # Bind the callback
    _w1.Custom1.bind("<<DateEntrySelected>>", on_calSelect)

# def on_popupSelect(param):
#     print("PopupSelect fired")

def on_calSelect(param):
    # ======================================================
    # Callback function for Custom Control date select.  This sets
    # a global variable 'PullDownDateReturn' for use elsewhere...
    # ======================================================
    print(f"Calendar Select: {_w1.Custom1.get_date()}")
    global PullDownDateReturn
    PullDownDateReturn = _w1.Custom1.get_date()
    _w1.lblPulldownReturn.set(PullDownDateReturn.strftime("%m/%d/%Y"))

def on_showCalendar(*args):
    if _debug:
        print("datepicker_support.on_showCalendar")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()

    def print_sel():
        # print(cal.selection_get())
        dt = cal.selection_get()
        # You can use a custom date format like this...
        # frmtd = dt.strftime('%m/%d/%Y')
        # Or, use the default locale format...
        # frmtd = dt.strftime('%x')
        frmtd = dt.strftime("%m/%d/%Y")
        print(f"Formatted date: {frmtd}")
        # selection_get() returns a datetime.date object
        _w1.PopupReturn.set(frmtd)
        _w1.lblPopupReturn.set(frmtd)

    import datetime

    today = datetime.date.today()
    top = tk.Toplevel(root)
    cal = Calendar(
        top,
        font="Arial 14",
        selectmode="day",
        locale="en_US",
        firstweekday="sunday",
        weekenddays=[1, 7],
    )

    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def on_btnExit(*args):
    if _debug:
        print("datepicker_support.on_btnExit")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    sys.exit()

# Custom = tk.Frame  # To be updated by user with name of custom widget.
Custom = DateEntry

# Custom = tk.Frame  # To be updated by user with name of custom widget.

if __name__ == "__main__":
    datepicker.start_up()




