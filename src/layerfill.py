#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

import pkinter as pk


class LayerFill(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        self.layer_dict = {}
        self.layers = 0
        self.selected = 0

        self.layer_var = tk.IntVar()
        self.layer_var.trace_add("write", self.select_layer)

        self.add_layer()
        self.add_layer()

    def add_layer(self, *args):
        self.layers = len(self.layer_dict.keys())

        frame = Layer(self)
        frame.pack(side="top", fill="x")

        self.layer_dict[self.layers] = frame
        self.layer_dict[self.layers].layer.invoke()

    def delete_layer(self, layer, *args):
        self.layer_dict[layer].pack_forget()
        self.layer_dict[self.selected - 1 if self.selected > 0 else self.selected + 1].layer.invoke()

        for i in self.parent.master.canvas.find("all"):
            if "grid" not in self.parent.master.canvas.itemcget(i, "tags") and f"layer{layer}" in self.parent.master.canvas.itemcget(i, "tags"):
                self.parent.master.canvas.delete(i)

    def select_layer(self, *args):
        self.selected = self.layer_var.get()


class Layer(pk.Toolbar):
    def __init__(self, parent):
        pk.Toolbar.__init__(self, parent)

        # self.hide = frame.add_checkbutton(text="Hide", width=5, side="top")
        self.layer = self.add_radiobutton(text=f"Layer {parent.layers}", variable=parent.layer_var, value=parent.layers, side="top")
        # self.lock = frame.add_checkbutton(text="Lock", width=5, side="top")
