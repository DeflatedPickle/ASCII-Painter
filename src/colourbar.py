#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

import pkinter as pk


class Colourbar(pk.Toolbar):
    def __init__(self, parent):
        pk.Toolbar.__init__(self, parent)

        self.colours = ["Black", "White", "---", "Red", "Yellow", "Blue", "---", "Green", "Orange", "Purple"]
        self.colour_var = tk.StringVar()
        self.colour_var.set("black")

        for n, i in enumerate(self.colours):
            if i == "---":
                self.add_separator(orient="horizontal", side="top")

            else:
                self.add_radiobutton(text=i, side="top", variable=self.colour_var, value=i)
