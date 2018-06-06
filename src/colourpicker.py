#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from ctypes import windll

from OpenGL.GL import *
import pyopengltk as ogltk


class ColourPicker(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent, width=120, height=110)
        parent.update_idletasks()

        self._brightness = (0, 0, 0)
        self.colour = (0, 0, 0)

        self.final_colour = (1, 1, 1)
        self.final_colour_hex = "#000000"

        self.brightness_frame = self.create_window(0, 0, window=BrightnessFrame(self), anchor="nw", width=200, height=200)
        self.colour_frame = self.create_window(204, 0, window=ColourFrame(self), anchor="nw", width=20, height=200)

        self.colour_finder = self.create_rectangle(208, 0, 208 + 5, 5)

    def canvas_to_window(self, loc_x, loc_y):
        wx = loc_x + self.winfo_rootx()
        wy = loc_y + self.winfo_rooty()

        return wx, wy

    def move_finder(self, event):
        if 1 < event.y < 195:
            self.coords(self.colour_finder, 208, event.y, 208 + 5, event.y + 5)

    # Credit: atlasologist
    # Link: https://stackoverflow.com/questions/22647120/return-rgb-color-of-image-pixel-under-mouse-tkinter
    def get_colour(self, loc_x, loc_y):
        dc = windll.user32.GetDC(0)
        rgb = windll.gdi32.GetPixel(dc, int(loc_x), int(loc_y))
        r = rgb & 0xff
        g = (rgb >> 8) & 0xff
        b = (rgb >> 16) & 0xff

        # print(r, g, b)

        return r, g, b

    def get_colour_window(self):
        x, y, _, _ = self.coords(self.colour_finder)
        cx, cy = self.canvas_to_window(x, y)
        print(cx, cy)

        return self.get_colour(cx, cy)

    def get_event_colour(self, event):
        return self.get_colour(event.x_root, event.y_root)

    def set_final_colour(self, event, rgb=()):
        colour = self.get_event_colour(event)
        self.final_colour = colour
        self.final_colour_hex = f"#{colour[0]:02x}{colour[1]:02x}{colour[2]:02x}"

    def set_colour(self, value, event):
        self.colour = value

    def colour_to_float(self, value):
        return value / 255


class BrightnessFrame(ogltk.OpenGLFrame):
    def __init__(self, parent, width=100, height=100, **kwargs):
        ogltk.OpenGLFrame.__init__(self, parent, **kwargs)
        self.parent = parent

        self.bind("<Button-1>", parent.set_final_colour)
        self.bind("<B1-Motion>", parent.set_final_colour)

        self.animate = True

    def initgl(self):
        glViewport(0, 0, self.width * 2, self.height * 2)
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glShadeModel(GL_SMOOTH)

        glColor3f(0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()

    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT)

        red = self.parent.colour_to_float(self.parent.colour[0])
        green = self.parent.colour_to_float(self.parent.colour[1])
        blue = self.parent.colour_to_float(self.parent.colour[2])

        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        glVertex2i(-1, -1)  # Bottom left
        glColor3f(0.0, 0.0, 0.0)
        glVertex2i(1, -1)  # Bottom right
        glColor3f(red, green, blue)
        glVertex2i(1, 1)  # Top right
        glColor3f(1.0, 1.0, 1.0)
        glVertex2i(-1, 1)  # Top left
        glEnd()

        glFlush()


class ColourFrame(ogltk.OpenGLFrame):
    def __init__(self, parent, **kwargs):
        ogltk.OpenGLFrame.__init__(self, parent, **kwargs)
        self.parent = parent

        self._colour = (0, 0, 0)

        self.bind("<Motion>", parent.move_finder)
        self.bind("<B1-Motion>", parent.move_finder)

        self.bind("<Button-1>", self.set_colour, "+")
        self.bind("<Button-1>", lambda event: parent.set_colour(self._colour, event), "+")

        self.bind("<B1-Motion>", self.set_colour, "+")
        self.bind("<B1-Motion>", lambda event: parent.set_colour(self._colour, event), "+")

        # self.bind("<Button-1>", lambda event: parent.set_colour(parent.get_event_colour(event), event), "+")
        # self.bind("<B1-Motion>", lambda event: parent.set_colour(parent.get_event_colour(event), event), "+")

        self.animate = True

    def set_colour(self, event):
        self._colour = self.parent.get_colour_window()

    def initgl(self):
        glViewport(0, 0, 50, 200)
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glShadeModel(GL_SMOOTH)

        glColor3f(0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()

    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT)

        # TODO: Make this more efficient
        for i in reversed([n / 30 for n in range(0, 30)]):
            i = -i

            glBegin(GL_LINE_STRIP)

            glColor3f(1.0, 0.0, 0.0)
            glVertex2f(i, 1)  # Top left

            # - Middle Left -#
            glColor3f(1.0, 0.0, 1.0)
            glVertex2f(i, 0.8)  # Purple

            glColor3f(0.0, 0.0, 1.0)
            glVertex2f(i, 0.4)  # Blue

            glColor3f(0.0, 1.0, 1.0)
            glVertex2f(i, 0.2)  # Cyan

            glColor3f(0.0, 1.0, 0.0)
            glVertex2f(i, -0.0)  # Green

            glColor3f(1.0, 1.0, 0.0)
            glVertex2f(i, -0.4)  # Yellow
            # ---------------#

            glColor3f(1.0, 0.0, 0.0)
            glVertex2f(i, -0.99)  # Bottom left
            glEnd()

        glFlush()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")

    cpicker = ColourPicker(root)
    cpicker.pack(fill="both", expand=True)

    root.mainloop()
