from dijkstra import Grafo

def validar_atualizacao_da_distancia(distancia, linha_da_distancia):
    return (linha_da_distancia is None) or (distancia < linha_da_distancia)


def obter_indice_da_menor_distancia_nao_visitada(tabela:dict, indices_validos:list) -> int:
    distancias = [tabela['distancias'][indice] for indice in indices_validos]
    menor_distancia = min([distancia for distancia in distancias if distancia is not None])
    for indice_valido in indices_validos: 
        if menor_distancia == tabela['distancias'][indice_valido]: indice = indice_valido 
    return indice


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

inicio = 'C'
tabela = dict()
visitados = set()
vertices = list(grafo.vertices())
distancias = [0 if vertice == inicio else None for vertice in vertices]
anteriores = [inicio if vertice == inicio else None for vertice in vertices]

tabela['vertices'] = vertices
tabela['distancias'] = distancias
tabela['anteriores'] = anteriores


vertice = inicio
while len(visitados) < len(tabela['vertices']):
    for aresta in grafo.arestas_no_vertice(vertice): 
        vertice_adjacente = aresta[0]
        if vertice_adjacente in visitados: continue

        coluna_vertice = tabela['vertices'].index(vertice)
        coluna_adjacente = tabela['vertices'].index(vertice_adjacente)

        distancia = tabela['distancias'][coluna_vertice]
        distancia_adjacente = tabela['distancias'][coluna_adjacente]
        nova_distancia_adjacente = distancia + aresta[1]

        if validar_atualizacao_da_distancia(nova_distancia_adjacente, distancia_adjacente):
            tabela['distancias'][coluna_adjacente] = nova_distancia_adjacente 
            tabela['anteriores'][coluna_adjacente] = vertice

        visitados.add(vertice)

        indices_nao_visitados = [tabela['vertices'].index(vertice) for vertice in tabela['vertices'] if vertice not in visitados]
        if indices_nao_visitados: 
            indice = obter_indice_da_menor_distancia_nao_visitada(tabela, indices_nao_visitados)
            vertice = tabela['vertices'][indice]

for item in tabela.values(): print(item)
