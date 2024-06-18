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

    def adicionar_vertice(self, *args):
        for vertice in args:
            if not self.esta_no_grafo(vertice): 
                self.__grafo[vertice] = list()

    def indice_do_vertice(self, vertice, busca) -> int:
        index = -1
        if self.esta_conectado(vertice, busca):
            for aresta in self.__grafo[vertice]:
                if aresta[0] == busca: 
                    index = self.__grafo[vertice].index(aresta)
        return index

    def obter_aresta(self, arestas, busca) -> tuple:
        indice = self.indice_do_vertice(arestas, busca)
        aresta = list(self.__grafo[arestas][indice])
        return aresta

    def trocar_peso(self, inicio, fim, peso):
        aresta = self.obter_aresta(inicio, fim)
        indice = self.indice_do_vertice(inicio, fim)
        aresta[1] = peso
        self.__grafo[inicio][indice] = tuple((aresta))

    def adicionar_aresta(self, inicio, fim, peso=None):
        if self.esta_no_grafo(inicio) and self.esta_no_grafo(fim):
            if self.esta_conectado(inicio, fim):
                self.trocar_peso(inicio, fim, peso)
                aresta = self.obter_aresta(fim, inicio)
                if aresta and aresta[1] != peso:
                    self.adicionar_aresta(fim, inicio, peso)
            else: 
                self.__grafo[inicio].append((fim, peso))
                if not self.esta_conectado(fim, inicio):
                    self.adicionar_aresta(fim, inicio, peso)

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

    def criar_tabela_dijkstra(self, inicio):
        self.__tabela = TabelaDijkstra()
        self.__tabela.criar_tabela(self.vertices(), inicio)
    
    def __obter_index_dos_vertices_atual_e_vizinho(self, vertice_atual, vertice_vizinho) -> int:
        if self.__tabela:
            index_vertice_atual = self.__tabela.obter_index(vertice_atual, 'vertice')
            index_vertice_vizinho = self.__tabela.obter_index(vertice_vizinho, 'vertice')
            return index_vertice_atual, index_vertice_vizinho
        return -1, -1
    
    def __obter_peso_do_vetice_atual(self, indice_vertice_atual) -> int:
        if self.__tabela:
            linha_peso = self.__tabela.obter_linha_distancia()
            peso_vertice_atual = linha_peso[indice_vertice_atual]
            return peso_vertice_atual
        return -1, -1
    
    def __validar_atualizacao_de_peso(self, peso_atual, novo_peso, reverse=False) -> bool:
        if reverse: 
            return (peso_atual is None) or (novo_peso > peso_atual)
        return (peso_atual is None) or (novo_peso < peso_atual)
    
    def __foi_visitado(self, vertice):
        return vertice in self.__visitados
    
    def __visitar(self, vertice):
        self.__visitados.add(vertice)
        
    def obter_proximo_vertice(self) -> int:
        index_faltantes = [self.__tabela.obter_index(vertice) for vertice in self.vertices() if vertice not in self.__visitados]
        if index_faltantes:
            linha_vertice = self.__tabela.obter_linha_vertice()
            index_com_menor_distancia = self.__tabela.obter_index_com_menor_distancia(index_faltantes)
            proximo_vertice = linha_vertice[index_com_menor_distancia]
            return proximo_vertice

    def buscar_por_dijkstra(self, inicio, reverse=False):
        self.criar_tabela_dijkstra(inicio)
        self.__visitados = set()
        vertice_atual = inicio
        while len(self.__visitados) < len(self.vertices()):
            for vertice_vizinho in self.arestas_no_vertice(vertice_atual):
                if self.__foi_visitado(vertice_atual): continue
                index_vertice_atual, index_vertice_vizinho = self.__obter_index_dos_vertices_atual_e_vizinho(vertice_atual, vertice_vizinho[0])
                peso_vertice_atual, peso_vertice_vizinho = self.__obter_peso_do_vetice_atual(index_vertice_atual), vertice_vizinho[1]
                novo_peso = peso_vertice_atual + peso_vertice_vizinho
                if self.__validar_atualizacao_de_peso(self.__tabela.obter_distancia(index_vertice_vizinho), novo_peso, reverse):
                    self.__tabela.alterar_distancia(novo_peso, index_vertice_vizinho)
                    self.__tabela.alterar_antecessor(vertice_atual, index_vertice_vizinho)
            self.__visitar(vertice_atual)
            vertice_atual = self.obter_proximo_vertice()
    
    def mostrar_tabela_dijkstra(self):
        if self.__tabela:
            self.__tabela.mostrar_tabela()
            
    def mostrar_caminho_dijkstra(self, destino):
        caminho = self.__tabela.mostrar_caminho(destino)
        return caminho
        
            
            
class TabelaDijkstra():
    def __init__(self):
        self.__tabela = dict()   

    def esta_vazio(self, objeto) -> bool:
        return not bool(objeto)

    def inserir_proximos_ao_destino(self, aresta):
        if self.destino:
            self.__vertices_proximos_ao_destino = set()
            for vertice in aresta:
                self.__vertices_proximos_ao_destino.add(vertice)
                
    def __inserir_vertices(self, grafo:tuple):
        if not self.esta_vazio(grafo):
            self.__tabela['vertice'] = list()
            for vertice in grafo:
                self.__tabela['vertice'].append(vertice)
                
    def obter_linha_vertice(self) -> list:
        return self.__tabela['vertice']
                
    def alterar_distancia(self, distancia, index=0):
        if self.validar_index(index, 'distancia'):
            self.__tabela['distancia'][index] = distancia

    def __inserir_distancia(self):
        if not (self.esta_vazio(self.__tabela['vertice']) and self.esta_vazio(self.origem)):
            self.__tabela['distancia'] = list()
            for distancia in self.__tabela['vertice']:
                self.__tabela['distancia'].append(None if distancia != self.origem else 0) 
                
    def obter_linha_distancia(self) -> list:
        return self.__tabela['distancia']
                
    def validar_index(self, index, filtro='vertice') -> bool:
        return (index is not None) and (-1 < index <= len(self.__tabela[filtro]))
                
    def obter_distancia(self, index):
        if self.validar_index(index, 'distancia'):
            return self.__tabela['distancia'][index]

    def __inserir_antecessor(self):
        if not (self.esta_vazio(self.__tabela['vertice']) and self.esta_vazio(self.origem)):
            self.__tabela['antecessor'] = list()
            for _ in self.__tabela['vertice']:
                self.__tabela['antecessor'].append(None) 
                
    def obter_linha_antecessor(self) -> list:
        return self.__tabela['antecessor']
                
    def alterar_antecessor(self, antecessor, index=0):
        if self.validar_index(index, 'antecessor'):
            self.__tabela['antecessor'][index] = antecessor

    def criar_tabela(self, vertices:tuple, origem):
        self.origem = origem
        self.__inserir_vertices(vertices)
        self.__inserir_distancia()
        self.__inserir_antecessor()

    def obter_index(self, pesquisa, filtro='vertice') -> int:
        index = self.__tabela[filtro].index(pesquisa)
        return index
    
    def obter_index_com_menor_distancia(self, lista_index:list) -> int:
        linha_distancia = self.obter_linha_distancia()
        lista_distancias = list()
        for index in lista_index:
            if linha_distancia[index] is not None:
                lista_distancias.append(linha_distancia[index])
        if lista_distancias:
            indice_com_menor_distancia = self.obter_index(min(lista_distancias), 'distancia')
            return indice_com_menor_distancia
        return -1

    def mostrar_tabela(self):
        for linha in self.__tabela.keys():
            print(f'{linha}: {self.__tabela[linha]}')
            
    def mostrar_caminho(self, destino):
        caminho = list()
        if self.origem != destino:
            antecessor = destino
            caminho.append(antecessor)
            while antecessor != None:
                linha_vertice = self.obter_linha_vertice()
                index_proximo_vertice = linha_vertice.index(antecessor)
                antecessor = linha_vertice[index_proximo_vertice]
                caminho.append(antecessor)
        return caminho
                
        

grafo = Grafo()
# Adicionando vertices
grafo.adicionar_vertice('A','B','C','D','E')

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

grafo.buscar_por_dijkstra('C')
grafo.mostrar_tabela_dijkstra()
print(grafo.mostrar_caminho_dijkstra('A'))