#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import sys
import tkinter as tk

import menumaker as mm


class Menu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent

        self.grid_var = tk.BooleanVar()

        mm.constructor(self, [
            ("file", {"items": ["new ~ctrl+n",
                                "---",
                                "exit ~ctrl+q"]}),
            ("view", {"items": ["[grid_var]grid ~ctrl+g"]})
        ], scope=locals()["self"])

        parent.configure(menu=self)

    def new(self, *args):
        self.parent.canvas.clear_grid()

    def exit(self, *args):
        sys.exit()

    def grid(self, *args):
        self.parent.canvas.toggle_grid()

