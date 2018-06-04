#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

import menumaker as mm


class Menu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent

        mm.constructor(self, [
            ("file", {"items": ["new ~ctrl+n"]})
        ], scope=locals()["self"])

        parent.configure(menu=self)

    def new(self, *args):
        self.parent.canvas.clear_grid()
