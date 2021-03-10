#!/usr/bin/env python3

class ActionList():
    def __init__(self):
        self.__accion = []

    def add_accion(self, accion):
        self.__accion.append(accion)

    def del_accion(self, accion):
        self.__accion.remove(accion)

    def execute_accion(self, accion):
        if accion in self.__accion:
            self.__accion[self.__accion.index(accion)]()
