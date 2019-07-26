# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:14:45 2019

@author: Javi
"""
import numpy as np
from nodo import Nodo


class ID3:
    def __init__(self):
        self.raiz        = None
        self.atributos   = None

    def crear_nodo(self, nombre, padre, arista=None, ):
        return Nodo(nombre, padre, arista)
    
    def establecer_atributos(self, atributos):
        self.atributos = atributos
    
    def seleccionar_atributo(self, X, Y, antecedente):
        ganancia = []
        for i, atributo in enumerate(X.T):
            if i not in antecedente:
                ganancia.append(self.calcular_ganancia(atributo, Y))
            else:
                ganancia.append(float("-inf"))
    
        return ganancia.index(max(ganancia))
    
    def calcular_ganancia(self, atributo, Y):
        entropia_atributos = 0
        for valor in np.unique(atributo):
            y          = Y[atributo == valor]
            proporcion = y.size/Y.size
            entropia_atributos +=  proporcion * self.calcular_entropia(y)
    
        return self.calcular_entropia(Y) - entropia_atributos
    
    def calcular_entropia(self, Y):
        entropia = 0
        for valor in np.unique(Y):
            y           = Y[Y == valor]
            proporcion  = y.size/Y.size
            entropia   -= proporcion * np.log2(proporcion)
    
        return entropia
    
    def entrena(self, X, Y):
    
        # Establecemos etiquetas por defecto
        if self.atributos is None:
            self.atributos = [str(x) for x in range(X.shape[1])]
    
        # Comprobamos si solo existe una clase. (1)
        #if np.all(Y == Y[0]):
        i=0
        for y in Y:
            i=i+1
            if i>1:
                self.raiz = self.crear_nodo(Y[0], None)
        
        # De lo contrario, buscamos el mejor atributo. (2)
        else:
            atributo         = self.seleccionar_atributo(X, Y, [])
            nombre_atributo  = self.atributos[atributo]
            self.raiz        = self.crear_nodo(nombre_atributo, None)
    
            # Encontramos los hijos del nodo raiz. (3), (4) y (5)
            self.encontrar_hijos(X, Y, atributo, [atributo], self.raiz)
    
    def encontrar_hijos(self, X, Y, atributo, antecedente, nodo_actual):
        columna_atributo = X[:, atributo]
        valores_unicos   = np.unique(columna_atributo)
        for valor in valores_unicos:
    
            # Particionamos la base de datos. (4)
            x = X[columna_atributo == valor]
            y = Y[columna_atributo == valor]
    
            # Comprobamos si nos quedamos sin atributos. 
            if len(antecedente) == X.shape[1]:
                instancia = self.instancia_mas_abundante(y)
                hijo = self.crear_nodo(instancia, nodo_actual, valor)
                nodo_actual.agregar_hijo(hijo)
    
            # Comprobamos si solo existe una clase. (1)
            elif np.all(y == y[0]):
                hijo = self.crear_nodo(y[0], nodo_actual, valor)
                nodo_actual.agregar_hijo(hijo)
    
            # Seleccionamos el mejor atributo. (2)
            else:
                hijo        = self.seleccionar_atributo(x, y, antecedente)
                nombre_hijo = self.atributos[hijo]
                nodo_hijo   = self.crear_nodo(nombre_hijo, nodo_actual, valor)
                nodo_actual.agregar_hijo(nodo_hijo)
                self.encontrar_hijos(x, y, hijo, antecedente + [hijo], nodo_hijo)
    
    def predecir(self, X):
    
        Y = np.empty(X.shape[0], dtype="<U10")
        for i, fila in enumerate(X):
            Y[i] = self.predecir_fila(fila)
        return Y
    
    def predecir_fila(self, fila):
        nodo_actual = self.raiz
        while nodo_actual.hijos: 
            atributo         = nodo_actual.nombre
            columna_atributo = self.atributos.index(atributo)
            valor_atributo   = fila[columna_atributo]
            nodo_actual      = nodo_actual.regresar_hijo(valor_atributo)
    
        return nodo_actual.nombre



