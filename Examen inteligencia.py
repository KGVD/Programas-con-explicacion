# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:30:58 2023

@author: LoboM
"""

"""en este código implementamos el algoritmo de Prim para encontrar el árbol de expansión mínimo
 en un grafo ponderado no dirigido"""
 
"""Se define una función llamada prim que toma tres argumentos: W, N y S"""

def prim(w,n,s):
    v=[]
    
    """Se inicializa una lista vacía v de longitud n. Esta lista se utiliza para llevar
    un seguimiento de qué nodos se han agregado al árbol de expansión mínimo. Inicialmente, 
    todos los nodos tienen el valor 0, lo que significa que no se han agregado"""
    
    while(len(v)!= n):
        v.append(0)
    v[s]= 1
    E= []
    suma= 0
    
    """Dentro del bucle externo, se inicializa la variable minimo en un valor alto (en este caso
    9) que actúa como un marcador para encontrar el peso mínimo de las aristas"""
    
    for i in range(0,n-1):
        minimo= 9
        for j in range(0,n):
            if(v[j]==1):
                for k in range(0,n):
                    if(v[k]==0 and w[j][k]<minimo):
                        agregar_vertice=k
                        e=[j,k]
                        minimo=w[j][k]
                        
                        """Después de encontrar la arista con el peso mínimo, se suma su peso a 
                        la variable suma"""
                        
        suma += w[e[0]][e[1]]
        v[agregar_vertice]=1
        E.append(e)
    return [E,suma]
    
n=6
s=0
w=[
   [9,4,2,9,3,9],
   [4,9,9,5,9,9],
   [2,9,9,1,6,3],
   [9,5,1,9,9,6],
   [3,9,6,9,9,2],
   [9,9,3,6,2,9]
]
    
print(prim(w,n,s))
"""La función retorna una lista que contiene las aristas del árbol de expansión mínimo E y
 la suma de los pesos de las aristas suma"""
       
           