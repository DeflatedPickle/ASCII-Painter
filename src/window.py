#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import os

import tkinter as tk
from tkinter import font
from tkinter import ttk

import pkinter as pk
import pygame.sysfont
from PIL import Image, ImageDraw, ImageFont

from .hotbar import HotBar
from .statusbar import StatusBar
from .toolbar import ToolBar
from .optionbar import OptionBar
from .layerfill import LayerFill
from .menu import Menu
from .colourframe import ColourFrame


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("ASCII Painter")
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=2)
        self.columnconfigure(1, weight=1)

        self.canvas_width = 501
        self.canvas_height = 501

        #----------#

        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), (255, 255, 255))
        self.image_draw = ImageDraw.Draw(self.image)

        #----------#

        self.menu = Menu(self)

        #----------#

        self.option_bar = OptionBar(self)
        self.option_bar.grid(row=1, column=0, columnspan=3, sticky="we")

        self.tool_bar = ToolBar(self)
        self.tool_bar.grid(row=2, column=0, rowspan=2, sticky="ns")
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
        self.hot_bar.grid(row=0, column=0, columnspan=3, sticky="we")

        #----------#

        self.statusbar = StatusBar(self)
        self.statusbar.grid(row=4, column=0, columnspan=3, sticky="we")

        #----------#

        self.colour_frame = ColourFrame(self)
        self.colour_frame.grid(row=2, column=2, sticky="nesw")

        #----------#

        self.layer_frame = ttk.Frame(self)
        self.layer_frame.rowconfigure(0, weight=1)
        self.layer_frame.columnconfigure(0, weight=1)

        self.layer_fill = LayerFill(self.layer_frame, self)
        self.layer_fill.grid(row=0, column=0, sticky="nesw")

        self.layer_fill.current_layers.trace_add("write", self.check_layers)

        self.layer_bar = pk.Toolbar(self.layer_frame)
        self.layer_bar.add_button(text="+", command=self.layer_fill.add_layer)
        self.remove_layer = self.layer_bar.add_button(text="-", command=lambda: self.layer_fill.delete_layer(self.layer_fill.selected))
        self.layer_bar.grid(row=1, column=0, sticky="we")

        self.layer_fill.current_layers.set(0)

        self.layer_frame.grid(row=3, column=2, sticky="nesw")

    def check_layers(self, *args):
        if self.layer_fill.current_layers.get() <= 0:
            self.remove_layer.configure(state="disabled")

        else:
            self.remove_layer.configure(state="normal")

    def mouse_set(self, event=None):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def create_font(self):
        font = tk.font.Font(family=self.option_bar.font_var.get(), size=self.option_bar.size_var.get(),
                            weight=self.option_bar.bold_var.get(),
                            slant=self.option_bar.italic_var.get(),
                            underline=self.option_bar.under_var.get(),
                            overstrike=self.option_bar.strike_var.get())

        return font

    def draw(self, event=None):
        if not self.tool_bar.tool_var.get():
            font = self.create_font()

            loc = self.canvas.place_cell_location(self.canvas.create_text(0, 0, text=self.option_bar.char_var.get(), fill=self.colour_frame.colour_picker.final_colour_hex, tags=("drawn", f"layer{self.layer_fill.layer_var.get()}"), font=font), event.x, event.y)

            if loc is None:
                return

            self.image_draw.text([loc[0], loc[1]], self.option_bar.char_var.get(), self.colour_frame.colour_picker.final_colour, ImageFont.truetype(pygame.sysfont.match_font(self.option_bar.font_var.get(),
                                                                                                                                           1 if self.option_bar.bold_var.get() == "bold" else 0,
                                                                                                                                           1 if self.option_bar.italic_var.get() == "italic" else 0), self.option_bar.size_var.get() + 5))

        elif self.tool_bar.tool_var.get():
            closest = self.canvas.closest_cell(event.x, event.y)

            if closest is not None:
                coords = self.canvas.coords(closest)
                new_coords = [coords[0] if str(coords[0])[-1] == "5" else coords[0] - 5,
                              coords[1] if str(coords[1])[-1] == "5" else coords[1] - 5]

                if f"layer{self.layer_fill.layer_var.get()}" in self.canvas.itemcget(self.canvas.cells_contents[new_coords[0], new_coords[1]], "tags"):
                    loc = self.canvas.remove_cell_location(new_coords[0], new_coords[1])
                    self.image_draw.rectangle([loc[0], loc[1], loc[0] + 9, loc[1] + 9], (255, 255, 255))
