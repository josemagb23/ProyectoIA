# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:02:45 2019

@author: Javi
"""

class Nodo:
    def __init__(self, nombre, padre, arista=None):
        self.nombre = nombre
        self.padre  = padre
        self.hijos  = []
        self.arista = arista

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def regresar_hijo(self, arista):
        for hijo in self.hijos:
            if hijo.arista == arista:
                return hijo
        return None

