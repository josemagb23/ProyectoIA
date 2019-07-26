# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:49:13 2019

@author: Javi
"""

#Vamos a idear el árbol basándonos en el ejercicio 3 del boletín 1,
#ya que es un ejercicio simple realizado en clase que nos puede 
#aportar un árbol con pocas ramificaciones, para así entender
#el concepto a groso modo y no complicarnos mucho en la realización
#de la representación.

#Observamos la estructura del árbol como la de una lista de listas, en la que 
#cada valor de un atributo representa un índice de la lista, y el valor de estos
#índices representa la salida del árbol de decisiones(SI LEPISTO/NO LEPISTO).
#Los atributos que vamos a tratar en este problema son el de VELOCIDAD
#y el de ALAS, escogidos mediante el cálculo de la ganancia de cada atributo 
#que se nos ofrece en la tabla de este problema. El atributo de VELOCIDAD debe 
#tener 3 valores asignados, uno para la velocidad ALTA, 
#otro para la MEDIA y otro para la BAJA. A su vez, el atributo ALAS tendrá dos 
#valores asignados, SI y NO. Cabe destacar que, según la estructura de este árbol, 
#el atributo ALAS es estudiado solo si el atributo VELOCIDAD nos da el valor ALTA, 
#ya que de ser MEDIA o BAJA, el valor asignado para la velocidad será el de NO LEPISTO.

#Dicho esto, reservaremos la primera posición de nuestra lista para la lista
#de valores del atributo ALAS, cuya lista consta de 2 posiciones, la 
#primera para el valor SI ALAS, y la segunda para el valor NO ALAS.

alas = ["SI","NO"] 

#Así podemos asignar a la primera posición de nuestro árbol la lista generada 
#a partir del atributo ALAS. Este árbol tendrá 3 posibles posiciones,
#la primera corresponderá al valor de VELOCIDAD ALTA y llevará a la lista ALAS, 
#y la segunda y tercera, correspondientes a los valores de VELOCIDAD MEDIA y 
#VELOCIDAD BAJA, llevarán al valor NO LEPISTO.

arbol = [alas,"NO","NO"]
print("Árbol: "+str(arbol))

#Si queremos obtener por tanto la clasificación para un individuo con velocidad
#alta y alas, solo debemos buscar según los índices de nuestra lista de listas

print("Búsqueda para un individuo con velocidad alta y alas: "+str(arbol[0][0]))
print("Búsqueda para un individuo con velocidad baja: "+str(arbol[1]))

#Ahora, hemos de resolver el problema sumándole la característica de árbol mixto.
#Esta característica nos dice que podemos tener un tipo de hoja que recoja
#una cantidad de ejemplos que consideremos baja. Compararemos esta cantidad
#con un parámetro llamado quorum.
#En este caso, ya que nuestro conjunto de datos consta de 10 elementos, cogeremos 
#un quorum de 3. Para todas las ramas que contengan 3 o más ejemplos,
#el árbol nos ofrecerá su clasificación directa y la consideraremos como
#fiable, mientras que si estas ramas recogen menos de 3 ejemplos, lanzaremos
#el algoritmo de Naive Bayes, que nos ofrecerá una clasificación con 
#probabildades.

#Según nuestro problema, observamos que hemos de aplicar Naive Bayes cuando los
#atributos son VELOCIDAD ALTA y ALAS NO (1 ejemplo), y VELOCIDAD BAJA (2 ejemplos).

alas = ["SI","NB"]
arbol = [alas,"NO","NB"]
print ("Árbol mixto: "+str(arbol))

#Ahora, calculamos los pares valor-probabilidad para cada atributo seleccionado
#anteriormente. En cuanto al atributo VELOCIDAD ALTA y ALAS NO, tenemos que 
#nuestro individuo será NO LEPISTO con una probabilidad del 100%.
#Por otro lado, para el atributo VELOCIDAD BAJA, nuestro individuo será
#SI LEPISTO con una probabilidad del 8,6%, es decir, será NO LEPISTO en un
#91,4% de las ocasiones.

#Podemos crear así dos diccionarios que recojan las probabilidades y los valores
#que tengan mayor proporción, ya que seran los que el algoritmo de Naive Bayes
#nos devolverá, y agregarlos posteriormente a nuestra lista.

valta_alas = {"NO":100}
vbaja ={"NO":91.4}

#Actualizamos ahora nuestro árbol con los valores de los dos diccionarios que 
#acabamos de crear, y ya tenemos la representación en Python del árbol completa.

alas = ["SI",valta_alas]
arbol=[alas,"NO",vbaja]
print("Árbol mixto tras NB: "+str(arbol))



 

