"""implementa un algoritmo de búsqueda en profundidad"""

"""importamos el módulo re para trabajar con expresiones regulares"""
import re 

"""Se define una expresión regular llamada patron que busca cualquier carácter no alfanumérico 
en una cadena, esta expresión se utilizará posteriormente para dividir la cadena V en una 
lista de vértices"""

patron=re.compile(r'\W')
def bus_profundidad(E,ni,V):
      nodos={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7} 
      n=nodos[ni] 
      
      """Se divide la cadena V en una lista de vértices utilizando la expresión regular 
      patron para separarlos por caracteres no alfanuméricos. El resultado se almacena en 
      la variable V"""
      
      V=patron.split(V) 
      
      v1=V[n] 
      Vp=[v1] 
      
      Ep=[]
      w=v1
      
      """Se inicializa un diccionario padre que se utilizará para mantener un seguimiento 
      de los padres de los vértices en el recorrido."""
      
      padre={}
      while True:
          while True:
              arista=[(w,x) for x in V if ((w,x) in E and x not in Vp)]
              if arista==[]:
                  break
              vk=arista[0]
              Ep.append(vk)
              Vp.append(vk[1])
              padre.update({vk[1]:w})
              w=vk[1]
              
          if w==v1:
              print ("Resultado:",Ep)
              break
          w=padre.get(w)  
      return Ep
 
n='e'
V=('a b c d e f g h')
 
E={('a','b'),('a','c'),('a','g'),('b','a'),('b','d'),('b','g'),('c','a'),('c','d'),('c','e'),
    ('d','b'),('d','c'),('d','f'),('e','c'),('e','f'),('e','g'),('f','d'),('f','e'),('f','h'),
    ('g','a'),('g','b'),('g','e'),('h','f')} 
bus_profundidad(E,n,V)