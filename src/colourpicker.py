#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from ctypes import windll

from OpenGL.GL import *
from OpenGL.GLU import *
import pyopengltk as ogltk


class ColourPicker(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent, width=160, height=10)
        parent.update_idletasks()

        # self.brightness = (0, 0, 0)
        self.colour = (255, 0, 0)

        self.final_colour = (255, 0, 0)
        self.final_colour_hex = "#ff0000"

        self._cframe_x = 154

        self.brightness_frame = self.create_window(0, 0, window=BrightnessFrame(self), anchor="nw", width=150, height=150)
        self.colour_frame = self.create_window(self._cframe_x, 0, window=ColourFrame(self), anchor="nw", width=20, height=150)

        self.brightness_finder = self.create_rectangle(145, 0, 148, 5)
        self.colour_finder = self.create_rectangle(self._cframe_x, 0, self._cframe_x + 5, 5)

        # self.bind("<Button-1>", self.move_bfinder)
        # self.bind("<B1-Motion>", self.move_bfinder)

        # self.bind("<Button-1>", self.move_cfinder, "+")
        # self.bind("<B1-Motion>", self.move_cfinder, "+")

    def canvas_to_window(self, loc_x, loc_y):
        wx = loc_x + self.winfo_rootx()
        wy = loc_y + self.winfo_rooty()

        return wx, wy

    def move_cfinder(self, event):
        if 0 < event.y < 145:
            self.coords(self.colour_finder, self._cframe_x, event.y, self._cframe_x + 5, event.y + 5)

    def move_bfinder(self, event):
        if 0 < event.x < 145:
            self.coords(self.brightness_finder, event.x - 3, self.coords(self.brightness_finder)[1], event.x + 2, self.coords(self.brightness_finder)[1] + 5)

        if 0 < event.y < 145:
            self.coords(self.brightness_finder, self.coords(self.brightness_finder)[0], event.y - 4, self.coords(self.brightness_finder)[0] + 5, event.y + 2)

    # Credit: atlasologist
    # Link: https://stackoverflow.com/questions/22647120/return-rgb-color-of-image-pixel-under-mouse-tkinter
    def get_colour(self, loc_x, loc_y):
        dc = windll.user32.GetDC(0)
        rgb = windll.gdi32.GetPixel(dc, int(loc_x + 1), int(loc_y + 1))
        r = rgb & 0xff
        g = (rgb >> 8) & 0xff
        b = (rgb >> 16) & 0xff

        # print(r, g, b)

        return r, g, b

    def get_colour_window(self, target):
        x, y, _, _ = self.coords(target)
        cx, cy = self.canvas_to_window(x + 1, y + 1)

        return self.get_colour(cx, cy)

    def get_event_colour(self, event):
        return self.get_colour(event.x_root, event.y_root)

    def set_final_colour(self, event):
        colour = self.get_colour_window(self.brightness_finder)
        self.final_colour = colour
        self.final_colour_hex = f"#{colour[0]:02x}{colour[1]:02x}{colour[2]:02x}"

    def set_colour(self, value, event):
        self.colour = value

    def colour_to_float(self, value):
        return value / 256


class BrightnessFrame(ogltk.OpenGLFrame):
    def __init__(self, parent, width=100, height=100, **kwargs):
        ogltk.OpenGLFrame.__init__(self, parent, **kwargs)
        self.parent = parent

        self._brightness = (0, 0, 0)

        self.bind("<Button-1>", parent.move_bfinder)
        self.bind("<B1-Motion>", parent.move_bfinder)

        # self.bind("<Button-1>", parent.set_final_colour)
        # self.bind("<B1-Motion>", parent.set_final_colour, "+")

        self.bind("<Button-1>", lambda event: parent.set_final_colour(event), "+")
        self.bind("<B1-Motion>", lambda event: parent.set_final_colour(event), "+")

        self.animate = True

    def set_colour(self, event):
        self._brightness = self.parent.get_colour_window(self.parent.brightness_finder)

    def initgl(self):
        glViewport(0, 0, 170, 170)
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

        pcoords = self.parent.coords(self.parent.brightness_finder)
        pc = gluUnProject(pcoords[0], pcoords[1], 0)
        # Pointer
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(pc[0], -pc[1] - 0.35)  # Bottom Left
        glVertex2f(pc[0] + 0.09, -pc[1] - 0.35)  # Bottom Right
        glVertex2f(pc[0] + 0.09, -pc[1] - 0.25)  # Top Right
        glVertex2f(pc[0], -pc[1] - 0.25)  # Top Left
        glEnd()

        glFlush()


class ColourFrame(ogltk.OpenGLFrame):
    def __init__(self, parent, **kwargs):
        ogltk.OpenGLFrame.__init__(self, parent, **kwargs)
        self.parent = parent

        self._colour = (0, 0, 0)

        self.bind("<Button-1>", parent.move_cfinder)
        self.bind("<B1-Motion>", parent.move_cfinder)

        self.bind("<Button-1>", self.set_colour, "+")
        self.bind("<Button-1>", lambda event: parent.set_colour(self._colour, event), "+")

        self.bind("<B1-Motion>", self.set_colour, "+")
        self.bind("<B1-Motion>", lambda event: parent.set_colour(self._colour, event), "+")

        self.animate = True

        self.loop = None

        self.bind("<Enter>", self.set_parent_colour)
        self.bind("<Leave>", lambda event: self.after_cancel(self.loop))

        # self.parent.after(1, self.set_parent_colour)

    def set_colour(self, event):
        self._colour = self.parent.get_colour_window(self.parent.colour_finder)

    def set_parent_colour(self, *args):
        self.parent.set_final_colour(None)
        self.loop = self.parent.after(1, self.set_parent_colour)

    def initgl(self):
        glViewport(0, 0, 50, 150)
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

        pcoords = self.parent.coords(self.parent.colour_finder)
        pc = gluUnProject(pcoords[0], pcoords[1], 0)
        pc = [pc[0] / 50, pc[1] - 0.3]
        # Pointer
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(pc[0] - 1.2, -pc[1] - 0.35)  # Bottom Left
        glVertex2f(pc[0] + 0.6, -pc[1] - 0.35)  # Bottom Right
        glVertex2f(pc[0] + 0.6, -pc[1] - 0.25)  # Top Right
        glVertex2f(pc[0] - 1.2, -pc[1] - 0.25)  # Top Left
        glEnd()

        glFlush()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")

    cpicker = ColourPicker(root)
    cpicker.pack(fill="both", expand=True)

    root.mainloop()
