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

        self.mouse_x = 0
        self.mouse_y = 0

        self.character = "0"

        self.create_widgets()
        self.place_widgets()

        self.interval()

        self.bind("<Motion>", self.mouse_set)
        self.bind("<B1-Motion>", self.mouse_set, "+")
        self.bind("<B1-Motion>", self.draw, "+")

    def create_widgets(self):
        self.canvas = tk.Canvas(width=self.canvas_width, height=self.canvas_height,
                                background="white")

    def place_widgets(self):
        self.canvas.grid(row=0, column=0)

    def interval(self, wait=10):
        for i in self.canvas.find_withtag("mouse"):
            self.canvas.delete(i)

        self.canvas.create_text(self.mouse_x, self.mouse_y, text=self.character, tag="mouse")

        self.after(wait, self.interval)

    def mouse_set(self, event=None):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def draw(self, event=None):
        self.canvas.create_text(self.mouse_x, self.mouse_y, text=self.character, tag="drawn")
