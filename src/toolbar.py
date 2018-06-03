#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import font

import pkinter as pk


class Toolbar(pk.Toolbar):
    def __init__(self, parent):
        pk.Toolbar.__init__(self, parent)

        self.add_button(text="New", command=parent.canvas.clear_grid)

        self.add_separator()

        self.font_var = tk.StringVar()
        self.font_var.set("Courier")
        self.add_combobox(values=font.families(), textvariable=self.font_var, width=10)

        self.size_var = tk.IntVar()
        self.size_var.set(10)
        self.add_combobox(values=list(range(2, 74, 2)), textvariable=self.size_var, width=3)

        self.add_separator()

        self.bold_var = tk.StringVar()
        self.bold_var.set("normal")
        self.add_checkbutton(text="Bold", variable=self.bold_var, onvalue="bold", offvalue="normal")

        self.italic_var = tk.StringVar()
        self.italic_var.set("roman")
        self.add_checkbutton(text="Italic", variable=self.italic_var, onvalue="italic", offvalue="roman")

        self.under_var = tk.BooleanVar()
        self.add_checkbutton(text="Underline", variable=self.under_var)

        self.strike_var = tk.BooleanVar()
        self.add_checkbutton(text="Overstrike", variable=self.strike_var)

        self.add_separator()

        self.grid_var = tk.BooleanVar()
        check = self.add_checkbutton(text="Grid", command=parent.canvas.toggle_grid, variable=self.grid_var)
        parent.canvas._hidden = True
        check.invoke()
        check.invoke()
