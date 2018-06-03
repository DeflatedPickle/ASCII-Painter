#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

import pkinter as pk


class Tools(pk.Toolbar):
    def __init__(self, parent):
        pk.Toolbar.__init__(self, parent)

        self.tool_var = tk.IntVar()

        self.add_radiobutton(text="Pencil", side="top", variable=self.tool_var, value=0)
        self.add_radiobutton(text="Rubber", side="top", variable=self.tool_var, value=1)
