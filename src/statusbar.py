#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import pkinter as pk


class StatusBar(pk.Statusbar):
    def __init__(self, parent):
        pk.Statusbar.__init__(self, parent)

        self.add_sizegrip()
