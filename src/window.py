#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import font

import pkinter as pk

from .hotbar import HotBar
from .colourbar import ColourBar
from .statusbar import StatusBar
from .toolbar import ToolBar
from .optionbar import OptionBar


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("ASCII Painter")
        self.rowconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)

        self.canvas_width = 501
        self.canvas_height = 501

        self.mouse_x = 0
        self.mouse_y = 0

        #----------#

        self.colour_bar = ColourBar(self)
        # self.colourbar.grid(row=1, column=0, sticky="ns")

        #----------#

        self.option_bar = OptionBar(self)
        self.option_bar.grid(row=1, column=0, columnspan=2, sticky="we")

        self.tool_bar = ToolBar(self)
        self.tool_bar.grid(row=2, column=0, sticky="ns")
        self.tool_bar.pencil.invoke()

        #----------#

        self.canvas = pk.GridCanvas(self, rows=self.canvas_height // 10, columns=self.canvas_width // 10,
                                    width=self.canvas_width, height=self.canvas_height,
                                    background="white")
        self.canvas.grid(row=2, column=1, rowspan=2)

        self.canvas.bind("<Button-1>", self.draw, "+")
        self.canvas.bind("<B1-Motion>", self.draw, "+")

        #----------#

        self.hot_bar = HotBar(self)
        self.hot_bar.grid(row=0, column=0, columnspan=2, sticky="we")

        #----------#

        self.statusbar = StatusBar(self)
        self.statusbar.grid(row=3, column=0, columnspan=2, sticky="we")

    def interval(self, wait=10):
        for i in self.canvas.find_withtag("mouse"):
            self.canvas.delete(i)

        self.canvas.create_text(self.mouse_x, self.mouse_y, text=self.character, tag="mouse")

        self.after(wait, self.interval)

    def mouse_set(self, event=None):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def draw(self, event=None):
        if self.tool_bar.tool_var.get() == 0:
            font = tk.font.Font(family=self.option_bar.font_var.get(), size=self.option_bar.size_var.get(),
                                weight=self.option_bar.bold_var.get(),
                                slant=self.option_bar.italic_var.get(),
                                underline=self.option_bar.under_var.get(),
                                overstrike=self.option_bar.strike_var.get())

            self.canvas.place_cell_location(self.canvas.create_text(0, 0, text=self.option_bar.char_var.get(), fill=self.colour_bar.colour_var.get().lower(), tag="drawn", font=font), event.x, event.y)

        elif self.tool_bar.tool_var.get() == 1:
            self.canvas.remove_cell_location(event.x, event.y)
