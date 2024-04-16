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
        
