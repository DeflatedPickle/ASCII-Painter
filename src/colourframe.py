#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

from .colourpicker import ColourPicker


class ColourFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self._interval = 1

        self.rowconfigure(0, weight=1)

        self.colour_var = tk.IntVar()
        self.colour_var.set(0)

        frame = ttk.Frame(self)

        ttk.Style().configure("PrimaryColour.Toolbutton")
        self.primary_colour = ttk.Radiobutton(frame, width=2, variable=self.colour_var, value=0, style="PrimaryColour.Toolbutton")
        self.primary_colour.grid(row=0, column=0)
        self.primary_colour.invoke()

        # self.secondary_colour = ttk.Radiobutton(frame, text="S", variable=self.colour_var, value=1, style="Toolbutton")
        # self.secondary_colour.grid(row=1, column=0)

        frame.grid(row=0, column=0)

        self.colour_picker = ColourPicker(self)
        self.colour_picker.grid(row=0, column=1, padx=2, pady=2, sticky="nesw")

        self.loop = None

        self.colour_picker.bind("<Enter>", self.change_colour_button)
        self.colour_picker.bind("<Leave>", lambda event: self.after_cancel(self.loop))

    def change_colour_button(self, *args):
        ttk.Style().configure("PrimaryColour.Toolbutton", background=self.colour_picker.final_colour_hex)

        self.loop = self.after(self._interval, self.change_colour_button)
