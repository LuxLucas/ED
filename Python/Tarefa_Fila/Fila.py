from collections import deque

class Fila:
    def __init__(self):
        self.Fila = deque()
    
    def enfileirar(self, elemento):
        self.Fila.append(elemento)
    
    def desenfileirar(self):
        if not self.isVazio():
            self.Fila.popleft()

    def tamanho(self):
        Tamanho = len(self.Fila)
        return Tamanho
    
    def isVazio(self):
        EstadoFila = self.tamanho() == 0
        return EstadoFila
    
    def mostrarPrimeiroElemento(self):
        if not self.isVazio():
            PrimeiroElemento = self.Fila[0]
            return PrimeiroElemento
        else:
            return None
        
