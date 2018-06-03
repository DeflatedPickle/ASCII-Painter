#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import font
import string

import pkinter as pk


class OptionBar(pk.Toolbar):
    def __init__(self, parent):
        pk.Toolbar.__init__(self, parent)

    def change_tool(self):
        for i in self.pack_slaves():
            i.pack_forget()

        if self.parent.tool_bar.tool_var.get() == 0:
            self.pencil_options()

    def pencil_options(self):
        self.char_var = tk.StringVar()
        self.char_var.set("0")
        self.add_combobox(values=list(string.ascii_letters + string.digits + string.punctuation), textvariable=self.char_var, width=3)

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
