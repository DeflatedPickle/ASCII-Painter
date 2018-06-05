#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

from OpenGL.GL import *
from OpenGL.GLU import *
import pyopengltk as ogltk


class ColourPicker(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)

        self.brightness_frame = self.create_window(0, 0, window=BrightnessFrame(self), anchor="nw", width=50, height=50)


class BrightnessFrame(ogltk.OpenGLFrame):
    def __init__(self, parent, **kwargs):
        ogltk.OpenGLFrame.__init__(self, parent, **kwargs)

        self.animate = True

    def initgl(self):
        glViewport(0, 0, 50, 50)
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glShadeModel(GL_SMOOTH)

        glColor3f(0.0, 0.0, 0.0)
        glPointSize(4.0)
        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()

    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_POLYGON)
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


if __name__ == "__main__":
    root = tk.Tk()

    cpicker = ColourPicker(root)
    cpicker.pack(fill="both", expand=True)

    root.mainloop()
