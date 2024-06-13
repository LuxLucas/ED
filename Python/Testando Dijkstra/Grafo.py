def hello():
     print('Bom dia!')

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

    def __repr__(self):
            return f'{self.grafo}'
