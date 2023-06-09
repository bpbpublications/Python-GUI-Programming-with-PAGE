#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Dec 22, 2022 04:11:06 AM CST  platform: Linux

import sys

try:
    import plotext as plt
except:
    print("This program requires Plotext Library")
    sys.exit()

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import tkinter.font as tkfont
import plotextdemo

_debug = True  # False to eliminate debug printing from callback functions.


def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = plotextdemo.Main(_top1)
    startup()
    root.mainloop()


def startup():
    markers = [
        "sd",
        "hd",
        "dot",
        "at",
        "heart",
        "smile",
    ]  # "showflake"]  The font for the Label Widget does not support the snowflake character
    plottypes = [
        "Sine",
        "Scatter",
        "Simple Bar",
        "Horizontal Bar",
        "Multiple Bar",
        "Log Plot",
        "User Data Plot 1",
    ]
    _w1.TCombobox1["values"] = markers
    _w1.TCombobox2["values"] = plottypes
    _w1.TCombobox1.bind("<<ComboboxSelected>>", lambda e: on_Marker_Select(e))
    _w1.TCombobox2.bind("<<ComboboxSelected>>", lambda e: on_PlotType_Select(e))
    _w1.TCombobox1.current(0)
    # _w1.Label3.configure(font="-family {DejaVu Sans Mono} -size 8")
    global fontname, fontsize, font
    fontname = "DejaVu Sans Mono"
    fontsize = 8
    font = fontname + " " + str(fontsize)


def get_plot_size():
    global fontname, fontsize, font
    size = _w1.Label3.winfo_width(), _w1.Label3.winfo_height()
    font_plot = tkfont.Font(family=fontname, size=fontsize)
    font_size = font_plot.measure("m"), font_plot.metrics("linespace")  # in pixels
    # print(f"Font_size: {font_size}")
    size = [size[i] / font_size[i] for i in range(2)]
    size = list(map(int, size))
    cols, rows = size
    # print(f"Cols: {cols} - Rows: {rows}")
    return cols - 2, rows - 2


def on_btnPlot(*args):
    pass

    if _debug:
        print("CustomDemo1_support.on_btnPlot")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    command_plot()


def on_btnPlotClear(*args):
    pass

    if _debug:
        print("CustomDemo1_support.on_btnPlotClear")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    _w1.btnPlot.config(state=NORMAL)
    canv = ""
    _w1.PlotData.set(canv)


def command_plot_scatter():
    plt.clear_data()
    get_plot_size()
    y = plt.sin()
    plt.scatter(y)
    plt.title("Scatter Plot")

    y = plt.sin()
    plt.scatter(y)
    plt.title("Scatter Plot")
    _w1.Label1.configure(anchor="w")
    plt.limitsize(False, False)
    # plt.plotsize(150, 35)
    wid, hei = get_plot_size()
    plt.plotsize(wid, hei)
    plt.clc()
    canv = plt.uncolorize(plt.build())
    _w1.PlotData.set(canv)


def command_plot():
    global selected
    # -------------------------------------
    _w1.TCombobox1.config(state="normal")
    # ===================================================
    # Function data and code from Plotext Website
    # ===================================================
    plt.clear_data()
    plt.clear_plot()
    plt.clear_figure()

    selected = _w1.comboMarker.get()
    plt.plot(plt.sin(), marker=selected)

    # plt.plotsize(134, 35)
    wid, hei = get_plot_size()
    plt.plotsize(wid, hei)
    plt.limitsize(False)
    plt.clc()
    canv = plt.build()
    _w1.PlotData.set(canv)


def read_file(filename):
    # ======================================================
    # function read_file()
    # ======================================================
    # Read file, leaving end of lines
    # ======================================================
    with open(filename) as f:
        lines = f.read()
    return lines


def command_clear():
    global markers, plottypes, selected
    # -------------------------------------
    _w1.TCombobox1.config(state="normal")
    canv = ""
    _w1.PlotData.set(canv)


def on_Marker_Select(e):
    global selected
    selected = _w1.comboMarker.get()
    command_plot()


def on_PlotType_Select(e):
    global plottype, plottypes
    plottype = _w1.comboPlotType.get()
    if plottype == "Sine":
        _w1.TCombobox1.config(state="normal")
        command_plot()
    elif plottype == "Scatter":
        _w1.TCombobox1.config(state="disabled")
        command_plot_scatter()
    elif plottype == "Simple Bar":
        _w1.TCombobox1.config(state="disabled")
        command_plot_SBar()
    elif plottype == "Horizontal Bar":
        _w1.TCombobox1.config(state="disabled")
        command_plot_HBar()
    elif plottype == "Multiple Bar":
        _w1.TCombobox1.config(state="disabled")
        command_plot_MBar()
    elif plottype == "Log Plot":
        command_log_plot()
    elif plottype == "User Data Plot 1":
        command_user_data1()


def command_plot_SBar():
    global selected
    # -------------------------------------
    _w1.TCombobox1.config(state="disabled")
    plt.clear_data()
    plt.clear_plot()
    plt.clear_figure()
    # ===================================================
    # Function data and code from Plotext Website
    # ===================================================
    pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
    percentages = [14, 36, 11, 8, 7, 4]
    plt.clc()
    plt.bar(pizzas, percentages)
    plt.title("Most Favored Pizzas in the World")
    # plt.plotsize(150, 35)
    wid, hei = get_plot_size()
    plt.plotsize(wid, hei)
    plt.limitsize(False)
    plt.clc()
    canv = ""
    canv = plt.build()
    _w1.PlotData.set(canv)


def command_plot_HBar():
    global selected
    # -------------------------------------
    _w1.TCombobox1.config(state="disabled")
    plt.clear_data()
    plt.clear_plot()
    plt.clear_figure()
    # ===================================================
    # Function data and code from Plotext Website
    # ===================================================
    pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
    percentages = [14, 36, 11, 8, 7, 4]
    plt.clc()
    plt.bar(
        pizzas, percentages, orientation="horizontal"
    )  # or shorter orientation = 'h'
    plt.title("Most Favoured Pizzas in the World")
    # plt.plotsize(150, 35)
    wid, hei = get_plot_size()
    plt.plotsize(wid, hei)
    plt.limitsize(False)
    plt.clc()
    canv = ""
    canv = plt.build()
    _w1.PlotData.set(canv)


def command_plot_MBar():
    _w1.TCombobox1.config(state="disabled")
    plt.clear_data()
    plt.clear_plot()
    plt.clear_figure()
    # ===================================================
    # Function data and code from Plotext Website
    # ===================================================
    pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
    male_percentages = [14, 36, 11, 8, 7, 4]
    female_percentages = [12, 20, 35, 15, 2, 1]
    plt.multiple_bar(
        pizzas,
        [male_percentages, female_percentages],
        label=["men", "women"],
        marker=["sd", "dot"],
    )
    plt.title("Most Favored Pizzas in the World by Gender")
    # plt.plotsize(150, 35)
    wid, hei = get_plot_size()
    plt.plotsize(wid, hei)
    plt.limitsize(False)
    plt.clc()
    canv = ""
    canv = plt.build()
    _w1.PlotData.set(canv)


def command_log_plot():
    _w1.TCombobox1.config(state="disabled")
    # ===================================================
    # Function data and code from Plotext Website
    # ===================================================
    plt.clear_data()
    plt.clear_plot()
    plt.clear_figure()
    l = 10 ** 4
    x = range(1, l + 1)
    y = plt.sin(1, 2, l)
    plt.plot(x, y)
    plt.xscale("log")
    plt.yscale("linear")
    plt.grid(1, 0)
    plt.title("Logarithmic Plot")
    plt.xlabel("logarithmic scale")
    plt.ylabel("linear scale")
    # plt.plotsize(150, 35)
    wid, hei = get_plot_size()
    plt.plotsize(wid, hei)
    plt.limitsize(False)
    plt.clc()
    canv = ""
    canv = plt.build()
    _w1.PlotData.set(canv)


def command_user_data1():
    _w1.TCombobox1.config(state="disabled")
    plt.clear_data()
    plt.clear_plot()
    plt.clear_figure()
    # ===================================================
    # Covid-19 data from State of Texas Published Spreadsheet
    # ===================================================
    data = [
        21146,
        21183,
        21197,
        21220,
        21254,
        21254,
        21245,
        21245,
        21245,
        21290,
        21304,
        21329,
        21350,
        21350,
        21350,
        21472,
        21486,
        21540,
        21562,
        21621,
        21621,
        21621,
        21704,
        21761,
        21850,
        21928,
        22020,
        22020,
        22020,
        22305,
        22420,
    ]
    datedata = [
        "6/27/21",
        "6/28/21",
        "6/29/21",
        "6/30/21",
        "7/1/21",
        "7/2/21",
        "7/3/21",
        "7/4/21",
        "7/5/21",
        "7/6/21",
        "7/7/21",
        "7/8/21",
        "7/9/21",
        "7/10/21",
        "7/11/21",
        "7/12/21",
        "7/13/21",
        "7/14/21",
        "7/15/21",
        "7/16/21",
        "7/17/21",
        "7/18/21",
        "7/19/21",
        "7/20/21",
        "7/21/21",
        "7/22/21",
        "7/23/21",
        "7/24/21",
        "7/25/21",
        "7/26/21",
        "7/27/21",
    ]
    # ===================================================
    # Here we send the data into plotext.
    # ===================================================
    plt.datetime.set_datetime_form(date_form="%m/%d/%y")
    plt.plot_date(datedata, data)
    plt.title("Covid-19 Hays County, Tx. Data from 06/27/2021 - 07/27/2021")
    plt.ylabel("Confirmed Cases")
    # plt.plotsize(150, 35)
    wid, hei = get_plot_size()
    plt.plotsize(wid, hei)
    plt.limitsize(False)
    plt.clc()
    canv = ""
    canv = plt.build()
    _w1.PlotData.set(canv)


def on_btnExit(*args):
    if _debug:
        print("plotextdemo_support.on_btnExit")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    sys.exit()


if __name__ == "__main__":
    plotextdemo.start_up()
