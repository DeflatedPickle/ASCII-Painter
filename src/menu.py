#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import sys
import os
import tkinter as tk
from tkinter import filedialog

import menumaker as mm


def fix_extension(string, ext):
    split = os.path.splitext(string)

    if not split[1]:
        return f"{string}.{ext}"

    else:
        return string


class Menu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent

        self.grid_var = tk.BooleanVar()

        mm.constructor(self, [
            ("file", {"items": ["new ~ctrl+n",
                                "---",
                                "open text ~ctrl+o",
                                "---",
                                "export text",
                                "export postscript",
                                "export image",
                                "---",
                                "exit ~ctrl+q"]}),
            ("view", {"items": ["[grid_var]grid ~ctrl+g"]})
        ], scope=locals()["self"])

        parent.configure(menu=self)

    def new(self, *args):
        self.parent.canvas.clear_grid()
        self.parent.image_draw.rectangle([0, 0, self.parent.canvas_width, self.parent.canvas_height], (255, 255, 255))

    def open_text(self, *args):
        file = filedialog.askopenfile(filetypes=[("Text", "*.txt")])

        if file is None:
            return

        self.new()

        x = 0
        y = 0

        for i in file.read():
            if i == "\n":
                x = 0
                y += self.parent.canvas._cell_height

            font = self.parent.create_font()

            self.parent.canvas.place_in_cell(self.parent.canvas.create_text(0, 0, text=i, fill=self.parent.colour_frame.colour_picker.final_colour_hex, tags=("drawn", f"layer{self.parent.layer_fill.layer_var.get()}"), font=font), x, y)

            x += self.parent.canvas._cell_width

        file.close()

    def export_text(self, *args):
        file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text", "*.txt")])

        if file is None:
            return

        string = ""

        y = 0

        for k in self.parent.canvas.cells_contents.keys():
            value = self.parent.canvas.cells_contents[k]

            if k[1] == y + self.parent.canvas._cell_height:
                string += "\r\n"
                y = k[1]

            if value is not None:
                string += self.parent.canvas.itemcget(value, "text")

            else:
                string += " "

        file.write(string)
        file.close()

    def export_postscript(self, *args):
        file = filedialog.SaveAs(filetypes=[("PostScript", "*.ps")])
        file.show()

        if file is None:
            return

        self.parent.canvas.update()
        self.parent.canvas.postscript(file=fix_extension(file.filename, "ps"), colormode="color")

    def export_image(self, *args):
        file = filedialog.SaveAs(filetypes=[("PNG", "*.png"),
                                            ("JPEG", "*.jpg;*.jpeg;*.jpe")])
        file.show()

        if file.filename is "":
            return

        self.parent.image.save(fix_extension(file.filename, "png"))

    def exit(self, *args):
        sys.exit()

    def grid(self, *args):
        self.parent.canvas.toggle_grid()

