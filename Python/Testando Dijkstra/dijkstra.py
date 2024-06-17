"""
Privei o atributo __grafo para testar a privacidade dos objetos
"""
class Grafo:
    def __init__(self):
        self.__grafo = dict()

    def obter_grafo(self) -> dict:
        return self.__grafo

    def esta_no_grafo(self, vertice) -> bool:
        return vertice in self.__grafo
    
    def esta_vazio(self) -> bool:
        return not bool(self.__grafo)
    
    def esta_conectado(self, arestas, busca) -> bool:
        for aresta in self.__grafo[arestas]:
            if aresta[0] == busca: return True
        return False
    
    def indice_do_vertice(self, vertice, busca) -> int:
        index = -1
        if self.esta_conectado(vertice, busca):
            for aresta in self.__grafo[vertice]:
                if aresta[0] == busca: 
                    index = self.__grafo[vertice].index(aresta)
        return index

    def adicionar_vertice(self, *args):
        for vertice in args:
            if not self.esta_no_grafo(vertice): 
                self.__grafo[vertice] = list()

    def obter_aresta(self, arestas, busca) -> tuple:
        indice = self.indice_do_vertice(arestas, busca)
        aresta = list(self.__grafo[arestas][indice])
        return aresta

    def trocar_tamanho(self, inicio, fim, tamanho):
        aresta = self.obter_aresta(inicio, fim)
        indice = self.indice_do_vertice(inicio, fim)
        aresta[1] = tamanho
        self.__grafo[inicio][indice] = tuple((aresta))

    def adicionar_aresta(self, inicio, fim, tamanho=None):
        if self.esta_no_grafo(inicio) and self.esta_no_grafo(fim):
            if self.esta_conectado(inicio, fim):
                self.trocar_tamanho(inicio, fim, tamanho)
                aresta = self.obter_aresta(fim, inicio)
                if aresta and aresta[1] != tamanho:
                    self.adicionar_aresta(fim, inicio, tamanho)
            else: 
                self.__grafo[inicio].append((fim, tamanho))
                if not self.esta_conectado(fim, inicio):
                    self.adicionar_aresta(fim, inicio, tamanho)

    def vertices(self) -> tuple:
        vertices = tuple(list((vertice for vertice in self.__grafo)))
        return vertices

    def arestas_no_vertice(self, vertice) -> tuple:
        aresta_total = list()
        if self.esta_no_grafo(vertice):
            aresta_total = self.__grafo[vertice]
        aresta_total = tuple(aresta_total)
        return aresta_total
    
    def __foi_mostrado(self, inicio, destino) -> bool:
        if self.mostrados:
            for aresta in self.mostrados:
                if (inicio in aresta) and (destino in aresta):
                    return True
        return False

    def mostrar_grafo(self):
        self.mostrados = list()
        for vertice in self.__grafo:
            for aresta in self.arestas_no_vertice(vertice):
                if not self.__foi_mostrado(vertice, aresta[0]):
                    print(f'{vertice} - {aresta[1]} -> {aresta[0]}')
                    self.mostrados.append(tuple((vertice, aresta[0])))
        del self.mostrados

    def criar_tabela_dijkstra(self, inicio, fim):
        self.__tabela = TabelaDijkstra()
        self.__tabela.criar_tabela(self.vertices(), inicio, fim)
        self.__tabela.inserir_proximos_ao_destino(self.arestas_no_vertice(fim))

    def __foi_visitado(self, vertice):
        return vertice in self.__vistados

    def buscar_por_dijkstra(self, inicio, fim=None, reverse=False):
        self.criar_tabela_dijkstra(inicio, fim)
        self.__vistados = set()
        vertice_atual = inicio
        while len(self.__vistados) < len(self.vertices()):
            for vertice in :
                if self.__foi_visitado(vertice_atual): continue
        

class TabelaDijkstra():
    def __init__(self):
        self.__tabela = dict()   

    def esta_vazio(self, objeto) -> bool:
        return not bool(objeto)

    def __inserir_vertices(self, grafo:tuple):
        if not self.esta_vazio(grafo):
            self.__tabela['vertice'] = list()
            for vertice in grafo:
                self.__tabela['vertice'].append(vertice)

    def inserir_proximos_ao_destino(self, aresta):
        if self.destino:
            self.__vertices_proximos_ao_destino = set()
            for vertice in aresta:
                self.__vertices_proximos_ao_destino.add(vertice)

    def __inserir_distancia(self):
        if not (self.esta_vazio(self.__tabela['vertice']) and self.esta_vazio(self.origem)):
            self.__tabela['distancia'] = list()
            for distancia in self.__tabela['vertice']:
                self.__tabela['distancia'].append(None if distancia != self.origem else 0) 

    def __inserir_antecessor(self):
        if not (self.esta_vazio(self.__tabela['vertice']) and self.esta_vazio(self.origem)):
            self.__tabela['antecessor'] = list()
            for antecessor in self.__tabela['vertice']:
                if antecessor == self.origem: 
                    self.__tabela['antecessor'].append(self.origem)
                else: self.__tabela['antecessor'].append(None) 

    def criar_tabela(self, vertices:tuple, origem, destino=None):
        self.origem = origem
        self.destino = destino 
        self.__inserir_vertices(vertices)
        self.__inserir_distancia()
        self.__inserir_antecessor()

    def obter_index(self, pesquisa, filtro) -> int:
        index = self.__tabela[filtro].index(pesquisa)
        return index

    def mostrar_tabela(self):
        for linha in self.__tabela.keys():
            print(f'{linha}: {self.__tabela[linha]}')

grafo = Grafo()
grafo.adicionar_vertice('A','B','C')
grafo.adicionar_aresta('A','B', 8)
grafo.adicionar_aresta('A','C', 14)

grafo.mostrar_grafo()