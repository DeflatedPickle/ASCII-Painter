#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import font

import pkinter as pk


class Toolbar(pk.Toolbar):
    def __init__(self, parent):
        pk.Toolbar.__init__(self, parent)

        self.font_var = tk.StringVar()
        self.font_var.set("Courier")
        self.add_combobox(values=font.families(), textvariable=self.font_var)

        self.size_var = tk.IntVar()
        self.size_var.set(10)
        self.add_combobox(values=list(range(2, 74, 2)), textvariable=self.size_var)

        self.add_separator()
        self.bold_var = tk.BooleanVar()
        self.add_checkbutton(text="Bold", variable=self.bold_var)

        self.italic_var = tk.BooleanVar()
        self.add_checkbutton(text="Italic", variable=self.italic_var)

        self.under_var = tk.BooleanVar()
        self.add_checkbutton(text="Underline", variable=self.under_var)

        self.strike_var = tk.BooleanVar()
        self.add_checkbutton(text="Overstrike", variable=self.strike_var)
        self.add_separator()


