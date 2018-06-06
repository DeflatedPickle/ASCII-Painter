#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

import pkinter as pk


class LayerFill(ttk.Frame):
    def __init__(self, parent, window):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.window = window

        self.layer_dict = {}
        self.layers = 0
        self.current_layers = tk.IntVar()
        self.selected = 0

        self.layer_var = tk.IntVar()
        self.layer_var.trace_add("write", self.select_layer)

        self.add_layer()

    def add_layer(self, *args):
        self.layers = len(self.layer_dict.keys())
        self.current_layers.set(self.current_layers.get() + 1)

        frame = Layer(self, self.window, self.layers)
        frame.pack(side="top", fill="x")

        self.layer_dict[self.layers] = frame
        self.layer_dict[self.layers].layer_button.invoke()

    def delete_layer(self, layer, *args):
        self.current_layers.set(self.current_layers.get() - 1)
        self.layer_dict[layer].pack_forget()
        self.layer_dict[self.selected - 1 if self.selected > 0 else self.selected + 1].layer.invoke()

        for i in self.parent.master.canvas.find("all"):
            if "grid" not in self.parent.master.canvas.itemcget(i, "tags") and f"layer{layer}" in self.parent.master.canvas.itemcget(i, "tags"):
                self.parent.master.canvas.delete(i)

    def select_layer(self, *args):
        self.selected = self.layer_var.get()


class Layer(pk.Toolbar):
    def __init__(self, parent, window, layer):
        pk.Toolbar.__init__(self, parent)
        self.parent = parent
        self.window = window
        self.layer = layer

        self.hide_var = tk.BooleanVar()
        self.hide = self.add_checkbutton(text="Hide", width=5, variable=self.hide_var, command=self.hide_layer)

        self.layer_button = self.add_radiobutton(text=f"Layer {self.layer}", variable=parent.layer_var, value=parent.layers)
        self.layer_button.pack_configure(fill="x", expand=True)

        # self.lock = self.add_checkbutton(text="Lock", width=5)

    def hide_layer(self, event=None):
        if self.hide_var.get():
            self.window.canvas.itemconfig(f"layer{self.layer}", state="hidden")

        else:
            self.window.canvas.itemconfig(f"layer{self.layer}", state="normal")
