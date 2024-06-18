from dijkstra import Grafo

grafo = Grafo()

# Adicionando vertices
grafo.adicionar_vertice('A','B','C','D','E','F','G','H','I')

# Arestas de A
grafo.adicionar_aresta('A','B', 8)
grafo.adicionar_aresta('A','C', 14)
# Arestas de B
grafo.adicionar_aresta('B','D', 14)
grafo.adicionar_aresta('B','E', 3)
# Arestas de C
grafo.adicionar_aresta('C','D', 4)
grafo.adicionar_aresta('C','F', 5)
# Arestas de D
grafo.adicionar_aresta('D','E', 6)
grafo.adicionar_aresta('D','F', 4)
grafo.adicionar_aresta('D','G', 8)
grafo.adicionar_aresta('D','H', 9)
grafo.adicionar_aresta('D','I', 7)
# Arestas de E
grafo.adicionar_aresta('E','H', 7)
# Arestas de F
grafo.adicionar_aresta('F','G', 6)
# Arestas de G
grafo.adicionar_aresta('G','I', 8)
# Arestas de I
grafo.adicionar_aresta('I','H', 5)

grafo.buscar_por_dijkstra('D')
grafo.mostrar_tabela_dijkstra()
