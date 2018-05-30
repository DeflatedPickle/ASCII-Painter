#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("ASCII Painter")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.canvas_width = 500
        self.canvas_height = 500

        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(width=self.canvas_width, height=self.canvas_height,
                                background="white")

    def place_widgets(self):
        self.canvas.grid(row=0, column=0)
