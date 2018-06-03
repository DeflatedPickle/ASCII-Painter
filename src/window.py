#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import font

import pkinter as pk

from .toolbar import Toolbar
from .colourbar import Colourbar
from .statusbar import Statusbar


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("ASCII Painter")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        self.canvas_width = 501
        self.canvas_height = 501

        self.mouse_x = 0
        self.mouse_y = 0

        self.character = "0"

        #----------#

        self.colourbar = Colourbar(self)
        self.colourbar.grid(row=1, column=0, sticky="ns")

        #----------#

        self.canvas = pk.GridCanvas(self, rows=self.canvas_height // 10, columns=self.canvas_width // 10,
                                    width=self.canvas_width, height=self.canvas_height,
                                    background="white")
        self.canvas.grid(row=1, column=1)

        self.canvas.bind("<Button-1>", self.draw, "+")
        self.canvas.bind("<B1-Motion>", self.draw, "+")

        #----------#

        self.toolbar = Toolbar(self)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="we")

        #----------#

        self.statusbar = Statusbar(self)
        self.statusbar.grid(row=2, column=0, columnspan=2, sticky="we")

    def interval(self, wait=10):
        for i in self.canvas.find_withtag("mouse"):
            self.canvas.delete(i)

        self.canvas.create_text(self.mouse_x, self.mouse_y, text=self.character, tag="mouse")

        self.after(wait, self.interval)

    def mouse_set(self, event=None):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def draw(self, event=None):
        font = tk.font.Font(family=self.toolbar.font_var.get(), size=self.toolbar.size_var.get(),
                             weight=self.toolbar.bold_var.get(),
                             slant=self.toolbar.italic_var.get(),
                             underline=self.toolbar.under_var.get(),
                             overstrike=self.toolbar.strike_var.get())

        self.canvas.place_cell_location(self.canvas.create_text(0, 0, text=self.character, fill=self.colourbar.colour_var.get().lower(), tag="drawn", font=font), event.x, event.y)
