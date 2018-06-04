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

        if file is None:
            return

        self.parent.image.save(fix_extension(file.filename, "png"))

    def exit(self, *args):
        sys.exit()

    def grid(self, *args):
        self.parent.canvas.toggle_grid()

