#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

from OpenGL.GL import *
from OpenGL.GLU import *
import pyopengltk as ogltk


class ColourPicker(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent, width=120, height=110)

        self.brightness_frame = self.create_window(0, 0, window=BrightnessFrame(self), anchor="nw", width=100, height=100)
        self.colour_frame = self.create_window(104, 0, window=ColourFrame(self), anchor="nw", width=20, height=100)


class BrightnessFrame(ogltk.OpenGLFrame):
    def __init__(self, parent, width=100, height=100, **kwargs):
        ogltk.OpenGLFrame.__init__(self, parent, **kwargs)

        self.animate = True

    def initgl(self):
        glViewport(0, 0, self.width, self.height)
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glShadeModel(GL_SMOOTH)

        glColor3f(0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()

    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex2i(-1, -1)  # Bottom left
        glColor3f(0.0, 0.0, 0.0)
        glVertex2i(1, -1)  # Bottom right
        glColor3f(1.0, 0.0, 0.0)
        glVertex2i(1, 1)  # Top right
        glColor3f(1.0, 1.0, 1.0)
        glVertex2i(-1, 1)  # Top left
        glEnd()

        glFlush()


class ColourFrame(ogltk.OpenGLFrame):
    def __init__(self, parent, **kwargs):
        ogltk.OpenGLFrame.__init__(self, parent, **kwargs)

        self.animate = True

    def initgl(self):
        glViewport(0, 0, 50, 100)
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

    cpicker = ColourPicker(root)
    cpicker.pack(fill="both", expand=True)

    root.mainloop()
