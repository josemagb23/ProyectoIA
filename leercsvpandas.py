# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:09:28 2019

@author: Javi
"""

import pandas
from sklearn import preprocessing
from sklearn import naive_bayes
import numpy as np
from ID3 import ID3

url = input("Escribe la ruta del archivo: ")
val = pandas.read_csv(url, header=None,)
print(val)
print("Número de filas del archivo: "+str(val.shape[0]))
print("Número de columnas del archivo: "+str(val.shape[1]))

codificadores = []
val_codificado = pandas.DataFrame()
for variable, valores in val.iteritems():
    le = preprocessing.LabelEncoder()
    le.fit(valores)
    print('Codificación de valores para {}: {}'.format(variable, le.classes_))
    codificadores.append(le)
    val_codificado[variable] = le.transform(valores)

print(val_codificado.head(10))

quorum = (val.shape[0])/10
print("Quórum seleccionado para este tamaño de archivo: "+str(quorum))

"""Y_entrenamiento = []
columnas = list(val_codificado)
for i in columnas:
    if i == (len(columnas)-1):
        Y_entrenamiento.append(val_codificado[i][:])
X_entrenamiento = val_codificado[:]
X_entrenamiento.drop(len(columnas)-1,axis=1,inplace=True)
print("Conjunto de valores para entrenar: "+str(X_entrenamiento))
print ("Conjunto de clases: "+str(Y_entrenamiento))
arbol=ID3()
arbol.entrena(X_entrenamiento,Y_entrenamiento)
salida = arbol.predecir(X_entrenamiento)
print('Porcentaje de aciertos: ', 100*sum(Y_entrenamiento == salida)/X_entrenamiento.shape[0])"""

for x,y in val_codificado.iteritems():
    numejemplos = val_codificado.groupby(x).count()
    print("Número de ejemplos para cada valor del atributo {}: ".format(x))
    i=0
    for ej in numejemplos.keys():
        valores = numejemplos[ej].values
        print(valores)
        i = i+1
    #    for val in valores:
    #        if(val<quorum):{
                #NB  
    #            }
    #        if(val>=quorum):{
                #ID3
    #        }
        if(i>=1):
            break;
            

"""columnas = list(val_codificado)
j=0
i=0
for x,y in val_codificado.iterrows():
    print("X, Y: "+str(x),str(y))
    while i<=x:
        while j<=len(columnas):
            for Y in y.keys():
                if Y == 0:
                    ejemplos0 = val_codificado.iloc[i]
            j = j+1
        i = i+1
print ("ej0: "+str(ejemplos0))"""
        
            
            
"""continuar = input("¿Desea añadir un nuevo individuo al conjunto? Escriba Si/No: ")
if(continuar == "Si"):
    ejemplo = input("Escribe los parámetros del nuevo individuo separados por comas: ")
    lista_ejemplo = ejemplo.split(",")
    nuevo_individuo = []
    for ej in lista_ejemplo:
        nuevo_individuo.append(ej)
    print ("Parámetros del ejemplo: "+str(nuevo_individuo))
    
#    clasif_NB = naive_bayes.MultinomialNB(alpha=1.0)
    ohe = preprocessing.OneHotEncoder(sparse = False)
    ohe.fit(val_codificado[0].values.reshape(-1,1))
    ohe.transform(val_codificado[0].values.reshape(-1, 1))
    
    nuevo_individuo_codif = [le.transform([valor])
                           for valor, le in zip(nuevo_individuo, codificadores)]
    
    nuevo_individuo_codif = np.reshape(nuevo_individuo_codif, (1, -1))
    print("Parámetros codificados: "+str(nuevo_individuo_codif))
   # print(nuevo_individuo_codif)
    nuevo_individuo_nb = ohe.transform([nuevo_individuo_codif])
    print(nuevo_individuo_nb)
    
#    clase_nuevo_individuo = clasif_NB.predict(nuevo_individuo_nb)
#    print(codificadores[-1].inverse_transform(clase_nuevo_individuo)) """