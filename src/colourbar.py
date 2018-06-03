#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter.colorchooser import askcolor

import pkinter as pk


class Colourbar(pk.Toolbar):
    def __init__(self, parent):
        pk.Toolbar.__init__(self, parent)

        self.colours = ["Black", "White", "---", "Red", "Yellow", "Blue", "---", "Green", "Orange", "Purple"]
        self.colour_var = tk.StringVar()

        val = 0

        for n, i in enumerate(self.colours):
            if i == "---":
                self.add_separator(orient="horizontal", side="top")

            else:
                radio = self.add_radiobutton(text=i, side="top", variable=self.colour_var, value=i)

                if i.lower() == "black":
                    radio.invoke()

            val += 1

        self.add_separator(orient="horizontal", side="top")

        self.custom = self.add_radiobutton(text="Custom", command=self.foreground_colour, side="top", variable=self.colour_var, value=val)

    def foreground_colour(self):
        colour = askcolor()

        self.colour_var.set(colour[1])
