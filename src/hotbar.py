#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

import pkinter as pk


class HotBar(pk.Toolbar):
    def __init__(self, parent):
        pk.Toolbar.__init__(self, parent)

        self.add_button(text="New", command=parent.canvas.clear_grid)

        self.add_separator()

        self.grid_var = tk.BooleanVar()
        check = self.add_checkbutton(text="Grid", command=parent.canvas.toggle_grid, variable=self.grid_var)
        parent.canvas._hidden = True
        check.invoke()
        check.invoke()
