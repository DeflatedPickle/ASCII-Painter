#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import sys
import tkinter as tk
from tkinter import filedialog

import menumaker as mm


class Menu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent

        self.grid_var = tk.BooleanVar()

        mm.constructor(self, [
            ("file", {"items": ["new ~ctrl+n",
                                "---",
                                "export postscript",
                                "---",
                                "exit ~ctrl+q"]}),
            ("view", {"items": ["[grid_var]grid ~ctrl+g"]})
        ], scope=locals()["self"])

        parent.configure(menu=self)

    def new(self, *args):
        self.parent.canvas.clear_grid()

    def export_postscript(self, *args):
        file = filedialog.SaveAs(filetypes=[("PostScript", "*.ps")])
        file.show()

        if file is None:
            return

        self.parent.canvas.update()
        self.parent.canvas.postscript(file=file.filename + ".ps", colormode="color")

    def exit(self, *args):
        sys.exit()

    def grid(self, *args):
        self.parent.canvas.toggle_grid()

