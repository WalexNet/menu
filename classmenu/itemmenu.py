#!/usr/bin/env python3

#import curses

class ItemMenu():
    def __init__(self, nombre, accion, des = ''):
        self.nombre    = ' '+nombre.strip()+' '
        self.des       = des
        self.accion    = accion
        