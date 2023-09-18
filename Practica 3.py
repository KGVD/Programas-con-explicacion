"""aqui implementamos el algoritmo de Dijkstra"""
graph = {
'a':{'b':2, 'f':1},
'b':{'a':2, 'c':2, 'd':2},
'c':{'b':2, 'e':3, 'z':1},
'd':{'b':2, 'e':4, 'f':3},
'e':{'c':3, 'd':4, 'g':7},
'f':{'a':1, 'd':3, 'g':5},
'g':{'e':7, 'f':5, 'z':6},
'z':{'c':1, 'g':6}
}

"""" Se define una función llamada dijikstra que toma tres argumentos: el grafo graph, 
    el nodo de inicio start, y el nodo de destino goal"""

def dijikstra (graph, start, goal):
    
     shortest_distance = {}
     track_predecessor = {}
     unseenNodes = graph
     infinity = 9999999
     track_path =[]
     
     for node in unseenNodes:
         shortest_distance[node] = infinity
     shortest_distance[start] = 0
     
     """En cada iteración, se busca el nodo no visitado con la distancia más corta 
     (min_distance_node) de shortest_distance"""
     
     while unseenNodes: 
         min_distance_node = None
         for node in unseenNodes:
             if min_distance_node is None:
                 min_distance_node = node
             elif shortest_distance[node] < shortest_distance[min_distance_node]:
                 min_distance_node = node
         path_options = graph[min_distance_node].items()
         
         """Para cada nodo vecino y su peso, se verifica si la suma de la distancia desde el nodo
         de inicio a min_distance_node y el peso de la arista es menor que la distancia actual
         almacenada en shortest_distance. Si es así, se actualiza la distancia y se 
         registra min_distance_node como el predecesor de ese nodo"""
         
         for child_node, weight in path_options:
             if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                 shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                 track_predecessor[child_node] = min_distance_node
         unseenNodes.pop(min_distance_node)        
     currentNode = goal
     
     """Si se encuentra un camino válido, se imprime la distancia más corta y el camino más seguro
     desde el nodo de inicio al nodo de destino, si no suelta que es imposible"""

     while currentNode != start:         
         try:
             track_path.insert(0, currentNode)
             currentNode =track_predecessor[currentNode]
         except KeyError:
             print("Es imposible encontrar el camino")
             
     track_path.insert(0,start)
     
     if shortest_distance[goal] != infinity:
         print("La distancia mas corta es: " + str(shortest_distance[goal]))
         print("Camino mas seguro es: " + str(track_path))
         
         
dijikstra(graph, 'e', 'a')