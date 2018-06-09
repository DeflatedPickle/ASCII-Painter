#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import textwrap

import tkinter as tk
from tkinter import ttk

import pkinter as pk

class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("About ASCII Painter")
        self.transient(parent)
        self.grab_set()
        self.geometry("320x340")

        self.frame = ttk.Frame(self)

        self.text = tk.Text(self.frame, width=0, height=0, relief="flat", background="SystemButtonFace")
        self.text.insert("end", textwrap.dedent("""\
                                                ASCII Painter
                                                
                                                Version 1.20.11
                                                Colour Picker Version 1.0.6
                                                
                                                Copyright (c) 2018 DeflatedPickle. MIT.
                                                
                                                Python 3.6.4
                                                Tk 8.6.6
                                                
                                                Depends On:
                                                    pkinter 1.36.3
                                                    menumaker 1.4.1
                                                    pillow 5.1.0
                                                    pygame 1.9.3
                                                    pyopengl 3.1.0
                                                    pyopengltk 0.0.2
                                                """))
        self.text.configure(state="disabled")
        self.text.pack(fill="both", expand=True)

        self.frame.pack(side="top", fill="both", expand=True)

        self.button_frame = ttk.Frame(self)

        self.ok_button = pk.BoundButton(self, text="OK", command=self.ok)
        self.ok_button.pack(side="right")

        self.button_frame.pack(side="bottom", fill="y")

        pk.center_on_parent(self)

    def ok(self, *args):
        self.destroy()
