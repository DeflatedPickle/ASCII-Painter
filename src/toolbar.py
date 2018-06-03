#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

import pkinter as pk


class ToolBar(pk.Toolbar):
    def __init__(self, parent):
        pk.Toolbar.__init__(self, parent)

        self.tool_var = tk.IntVar()

        self.pencil = self.add_radiobutton(text="Pencil", side="top", command=parent.option_bar.change_tool, variable=self.tool_var, value=0)
        self.add_radiobutton(text="Rubber", side="top", command=parent.option_bar.change_tool, variable=self.tool_var, value=1)
