from os import system, name
from Cardapio import Cardapio


class Menu:
    def limpar_console(self):
        if name == 'nt':
            system('cls')
        if name == 'posix':
            system('clear')

    def mostrar_principal_opcoes(self):
        self.limpar_console()
        print('1 - Fazer pedido')
        print('2 - pedido atual')
        print('3 - Mostar pedidos')
        print('0 - Encerrar programa')
        comando = input('\nSeu Comando: ')
        return comando
    

    def mostrar_cardapio(self):
        self.limpar_console()
        cardapio_menu = Cardapio()
        cardapio_menu.mostrar_cardapio()
        print(f'\n{" NOVO PEDIDO ":=^70}')
        tipo = input('\nTipo: ')
        identificador = input('Identificador: ')
        return tipo, identificador
