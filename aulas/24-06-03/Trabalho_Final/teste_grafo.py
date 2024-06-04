import networkx as nx

# Inicializa um grafo
G = nx.Graph()

# Adiciona vértices

lista = [cidade for cidade in range(8)]

def add(list_1 : list):
    for data in list:
        G.add_node(data)
        
G.add_weighted_edges_from([cidade for cidade in range(8)])
    
add(lista)

# Adiciona arestas
G.add_edge(1, 2)
G.add_edge(2, 3)

# Visualiza o grafo
nx.draw(G, with_labels=True)
