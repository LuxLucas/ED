<<<<<<< HEAD
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
        
=======
from collections import deque

class Fila:
    def __init__(self):
        self.Fila = deque()
    
    def enfileirar(self, elemento):
        self.Fila.append(elemento)
    
    def desenfileirar(self):
        self.Fila.popleft()

    def tamanho(self):
        Tamanho = len(self.Fila)
        return Tamanho
    
    def vazio(self):
        EstadoFila = self.tamanho() == 0
        return EstadoFila
    
    def mostrar_primeiro_elemento(self):
        if not self.vazio():
            PrimeiroElemento = self.Fila[0]
            return PrimeiroElemento
        else:
            return None
        
>>>>>>> fbe8aacedfd0e9bde2aaf0c26a699d9fa5cbf0ca
