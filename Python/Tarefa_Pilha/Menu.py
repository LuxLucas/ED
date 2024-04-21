from os import system


class Menu:
    def __init__(self):
        self.comando = None

    @staticmethod
    def limpar_console():
        system('cls')
    
    def opcoes_principais(self):
        self.limpar_console()
        print(f"1 - Criar pilha")
        print(f"2 - Adicionar elementos")
        print(f"3 - Remover último elemento")
        print(f"4 - Imprimir pilha")
        print(f"5 - Pilha cheia")
        print(f"6 - Pilha vazia")
        print(f"7 - Quantidade de elementos")
        print(f"0 - Sair do programa")
        
        self.comando = input('\nSeu comando: ')
        return self.comando

    def tamanho_pilha(self):
        self.limpar_console()
        try:
            self.comando = int(input(f"Tamanho da pilha: "))

            if self.comando <= 0 or self.comando == '':
                print(f'\nTamanho INVÁLIDO')
                return None
            return self.comando

        except (ValueError, TypeError):
            self.comando = None
            return self.comando

    def receber_elemento(self):
        self.limpar_console()
        self.comando = input("Elemento a adicionar: ")
        return self.comando

    @staticmethod
    def terminar_mensagem():
        terminar_mensagem = input('\nPressione "ENTER" para continuar ')

    def avisar_usuario(self, aviso):
        self.limpar_console()
        print(aviso)
        self.terminar_mensagem()
        