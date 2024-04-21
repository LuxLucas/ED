from os import system, name
from Cardapio import Cardapio


class Menu:
    def limparConsole(self):
        if name == 'nt':
            system('cls')
        if name == 'posix':
            system('clear')

    def principal(self):
        self.limparConsole()
        print('1 - Fazer pedido')
        print('2 - Pedido atual')
        print('3 - Mostar pedidos')
        print('0 - Encerrar programa')
        Comando = input('\nSeu Comando: ')
        return Comando
    

    def mostrarCardapio(self):
        self.limparConsole()
        CardapioMenu = Cardapio()
        CardapioMenu.mostarCardapio()
        print(f'\n{" NOVO PEDIDO ":=^70}')
        Tipo = input('\nTipo: ')
        Identificador = input('Identificador: ')
        return Tipo, Identificador
