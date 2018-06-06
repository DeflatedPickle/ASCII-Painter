#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

from .colourpicker import ColourPicker


class ColourFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.rowconfigure(0, weight=1)

        self.colour_var = tk.IntVar()
        self.colour_var.set(0)

        frame = ttk.Frame(self)

        self.primary_colour = ttk.Radiobutton(frame, text="P", variable=self.colour_var, value=0, style="Toolbutton")
        self.primary_colour.grid(row=0, column=0)
        self.primary_colour.invoke()

        # self.secondary_colour = ttk.Radiobutton(frame, text="S", variable=self.colour_var, value=1, style="Toolbutton")
        # self.secondary_colour.grid(row=1, column=0)

        frame.grid(row=0, column=0)

        self.colour_picker = ColourPicker(self)
        self.colour_picker.grid(row=0, column=1, padx=2, pady=2, sticky="nesw")

        # self.colour_picker.tag_bind(self.colour_picker.brightness_frame, "<Button-1>", self.change_colour_button, "+")
        # self.colour_picker.tag_bind(self.colour_picker.brightness_frame, "<B1-Motion>", self.change_colour_button, "+")

    def change_colour_button(self, event):
        print("ff")
        self.primary_colour.configure(background=self.colour_picker.final_colour_hex)
