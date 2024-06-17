class Grafo:
    def __init__(self):
        self.grafo = dict()

    def vertice_existe(self, vertice):
        return vertice in self.grafo

    def adicionar_vertice(self, vertice):
        if not self.vertice_existe(vertice):
            self.grafo[vertice] = list()

    def adicionar_aresta(self, vertice_inicial, vertice_final = None, distancia:float = None):
        if not self.vertice_existe(vertice_inicial):
            self.adicionar_vertice(vertice_inicial)
        self.grafo[vertice_inicial].append((vertice_final, distancia))

from classes import Grafo

def validar_atualizacao_da_distancia(distancia, linha_da_distancia):
    return (linha_da_distancia is None) or (distancia < linha_da_distancia)


def obter_indice_da_menor_distancia_nao_visitada(tabela:dict, indices_validos:list) -> int:
    distancias = [tabela['distancias'][indice] for indice in indices_validos]
    menor_distancia = min([distancia for distancia in distancias if distancia is not None])
    for indice_valido in indices_validos: 
        if menor_distancia == tabela['distancias'][indice_valido]: indice = indice_valido 
    return indice


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


inicio = 'C'
tabela = dict()
visitados = set()

vertices = [vertice for vertice in grafo.grafo.keys()]
distancias = [0 if vertice == inicio else None for vertice in vertices]
anteriores = [inicio if vertice == inicio else None for vertice in vertices]

tabela['vertices'] = vertices
tabela['distancias'] = distancias
tabela['anteriores'] = anteriores

vertice = inicio
while len(visitados) < len(tabela['vertices']):
    for aresta in grafo.grafo[vertice]: 
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
