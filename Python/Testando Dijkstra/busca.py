from Grafo import Grafo
from dijkstra import *

grafo = Grafo()
# Arestas de A
grafo.adicionar_aresta('A','B', 8)
grafo.adicionar_aresta('A','C', 14)
# Arestas de B
grafo.adicionar_aresta('B','A', 8)
grafo.adicionar_aresta('B','D', 14)
grafo.adicionar_aresta('B','E', 3)
# Arestas de C
grafo.adicionar_aresta('C','A', 4)
grafo.adicionar_aresta('C','D', 4)
grafo.adicionar_aresta('C','F', 5)
# Arestas de D
grafo.adicionar_aresta('D','B', 14)
grafo.adicionar_aresta('D','C', 11)
grafo.adicionar_aresta('D','E', 6)
grafo.adicionar_aresta('D','F', 4)
grafo.adicionar_aresta('D','G', 8)
grafo.adicionar_aresta('D','H', 9)
grafo.adicionar_aresta('D','I', 7)
# Arestas de E
grafo.adicionar_aresta('E','B', 3)
grafo.adicionar_aresta('E','D', 6)
grafo.adicionar_aresta('E','H', 7)
# Arestas de F
grafo.adicionar_aresta('F','C', 5)
grafo.adicionar_aresta('F','D', 4)
grafo.adicionar_aresta('F','G', 6)
# Arestas de G
grafo.adicionar_aresta('G','D', 8)
grafo.adicionar_aresta('G','F', 6)
grafo.adicionar_aresta('G','I', 8)
# Arestas de H
grafo.adicionar_aresta('H','D', 9)
grafo.adicionar_aresta('H','E', 6)
grafo.adicionar_aresta('H','I', 5)
# Arestas de I
grafo.adicionar_aresta('I','D', 7)
grafo.adicionar_aresta('I','H', 5)
grafo.adicionar_aresta('I','G', 8)

for vertice in grafo.grafo:
    print(f'{vertice}:{grafo.grafo[vertice]}')