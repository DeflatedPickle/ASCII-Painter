#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

import pkinter as pk


class HotBar(pk.Toolbar):
    def __init__(self, parent):
        pk.Toolbar.__init__(self, parent)

        self.add_button(text="New", command=parent.menu.new)

        self.add_separator()

        check = self.add_checkbutton(text="Grid", command=parent.menu.grid, variable=parent.menu.grid_var)
        parent.canvas._hidden = True
        check.invoke()
        check.invoke()
