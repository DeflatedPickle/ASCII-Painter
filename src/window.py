#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

import pkinter as pk

from .toolbar import Toolbar
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

        self.toolbar = Toolbar(self)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="we")

        #----------#

        self.canvas = pk.GridCanvas(self, rows=self.canvas_height // 10, columns=self.canvas_width // 10,
                                    width=self.canvas_width, height=self.canvas_height,
                                    background="white")
        self.canvas.grid(row=1, column=1)

        self.canvas.bind("<Button-1>", self.draw, "+")
        self.canvas.bind("<B1-Motion>", self.draw, "+")

    def interval(self, wait=10):
        for i in self.canvas.find_withtag("mouse"):
            self.canvas.delete(i)

        self.canvas.create_text(self.mouse_x, self.mouse_y, text=self.character, tag="mouse")

        self.after(wait, self.interval)

    def mouse_set(self, event=None):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def draw(self, event=None):
        font = f"{self.toolbar.font_var.get()} {self.toolbar.size_var.get()}"

        if self.toolbar.bold_var.get():
            font += " bold"

        if self.toolbar.italic_var.get():
            font += " italic"

        if self.toolbar.under_var.get():
            font += " underline"

        if self.toolbar.strike_var.get():
            font += " overstrike"

        self.canvas.place_cell_location(self.canvas.create_text(0, 0, text=self.character, tag="drawn", font=font), event.x, event.y)
