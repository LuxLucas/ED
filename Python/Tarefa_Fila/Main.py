from Menu import Menu
from Pedido import Pedido
from Fila import Fila
from Cardapio import Cardapio

def avisarUsuario(TipoDeAviso):
    MenuErro = Menu()
    MenuErro.limparConsole()
    match TipoDeAviso:
        case '#Valor_Invalido':
            print('Valor Inválido')
        case '#Fila_Vazia':
            print('Fila De Pedidos Vazia')
        case '#Tipo_Ou_Id_Invalido':
            print('Tipo e/ou Indentificador Inválido')
        case '#Sucesso_Cadastro':
            print(f'{"=":=^70}')
            print(f'{" PEDIDO CADASTRADO ":=^70}')
            print(f'{"=":=^70}')
        case _:
            print(TipoDeAviso)
    input('\nPrecione "ENTER" para continuar...')


def transformarEmInteiro(Elemento):
    try:
        Elemento = int(Elemento)
        return Elemento
    except (ValueError, TypeError):
        return -1


def cadastrarPedido(Fila):
    MenuDePedido = Menu()
    CardapioPedido = Cardapio()
    TipoDePedido, IdentificadorDePedido = MenuDePedido.mostrarCardapio()
    TipoDePedido = transformarEmInteiro(TipoDePedido)
    IdentificadorDePedido = transformarEmInteiro(IdentificadorDePedido)
    if CardapioPedido.validarIdentificador(IdentificadorDePedido, TipoDePedido):
        NovoPedido = Pedido(TipoDePedido, IdentificadorDePedido)
        Fila.enfileirar(NovoPedido)
        avisarUsuario('#Sucesso_Cadastro')
    else:
        avisarUsuario('#Tipo_Ou_Id_Invalido')


def mostrarInformacaoDePedido(Pedido):
    print(f'Identificador: {Pedido.IdentificadorPedido}')
    print(f'Tipo: {Pedido.NomeTipoPedido}')
    print(f'Nome: {Pedido.NomePedido}')
    print(f'Preço: R${Pedido.PrecoPedido:,.2f}')


def mostrarInformacaoDoUltimoPedido(Fila):
    UltimoPedido = Fila.mostrarPrimeiroElemento()
    mostrarInformacaoDePedido(UltimoPedido)


def mostrarPedidoAtual(Fila):
    MenuDePedido = Menu()
    MenuDePedido.limparConsole()
    print(f'{" PEDIDO ATUAL ":=^70}')
    mostrarInformacaoDoUltimoPedido(Fila)
    print(f'{"=":=^70}')

    EscolhaDoUsuario = input('\nV:Voltar | C:Concluir Pedido: ').upper()
    if EscolhaDoUsuario == 'C':
        Fila.desenfileirar()


def mostrarTodosOsPedidos(Fila):
    MenuDePedido = Menu()
    MenuDePedido.limparConsole()
    OrdemDePedido = 0
    for Pedido in Fila.Fila:
        OrdemDePedido += 1
        print(f'\n{f" PEDIDO {OrdemDePedido} ":=^70}')
        mostrarInformacaoDePedido(Pedido)
    input('\nPrecione "ENTER" para continuar...')


def main():
    MenuDePedido = Menu()
    FilaPedido = Fila()
    while True:
        EscolhaDoUsuario = MenuDePedido.principal()
        if EscolhaDoUsuario == '0':
            break
        match EscolhaDoUsuario:
            case '1': 
                cadastrarPedido(FilaPedido)
            case '2': 
                if not FilaPedido.isVazio():
                    mostrarPedidoAtual(FilaPedido)
                else:
                    avisarUsuario('#Fila_Vazia')
            case '3': 
                if not FilaPedido.isVazio():
                    mostrarTodosOsPedidos(FilaPedido)
                else:
                    avisarUsuario('#Fila_Vazia')
            case _: 
                avisarUsuario('#Valor_Invalido')


if __name__ == "__main__":
    main()