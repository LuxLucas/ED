from Menu import Menu
from Pedido import Pedido
from Fila import Fila
from Cardapio import Cardapio

def avisarErro(TipoErro):
    match TipoErro:
        case '#Erro_Value_Invalid':
            print('Valor Inválido')
        case _:
            print(TipoErro)
    input('\nPrecione "ENTER" para continuar...')


def receberPedido(Tipo, Identificador):



def pedidoPrincipal(Pedido):
    match Pedido:
        case '1': cadastrarPedido()
        case '2': mostrarPedidoAtual()
        case '3': mostrarFila()
        case _: avisarErro('#Erro_Value_Invalid')


def main():
    while Comando != '0':
        FilaPrincipal = Fila()
        Comando = Menu.principal()
        pedidoPrincipal(Comando)


if __name__ == "__main__":
    main()