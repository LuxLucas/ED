from Menu import Menu
from Pedido import Pedido
from Fila import Fila
from Cardapio import Cardapio

def avisar_usuario(tipo_de_aviso):
    menu_erro = Menu()
    menu_erro.limpar_console()
    match tipo_de_aviso:
        case '#Valor_Invalido':
            print(f'{"=":=^70}')
            print(f'{" VALOR INVÁLIDO ":=^70}')
            print(f'{"=":=^70}')

        case '#Fila_Vazia':
            print(f'{"=":=^70}')
            print(f'{" FILA DE PEDIDOS VAZIA ":=^70}')
            print(f'{"=":=^70}')


        case '#Tipo_Ou_Id_Invalido':
            print(f'{"=":=^70}')
            print(f'{" TIPO E/OU IDENTIFICADOR INVÁLIDO ":=^70}')
            print(f'{"=":=^70}')


        case '#Sucesso_Cadastro':
            print(f'{"=":=^70}')
            print(f'{" PEDIDO CADASTRADO ":=^70}')
            print(f'{"=":=^70}')

        case '#Proximo_Pedido':
            print(f'{"=":=^70}')
            print(f'{" PRÓXIMO PEDIDO ":=^70}')
            print(f'{"=":=^70}')

        case _:
            print(tipo_de_aviso)
    input('\nPrecione "ENTER" para continuar...')


def transformar_em_inteiro(elemento):
    try:
        elemento = int(elemento)
        return elemento
    except (ValueError, TypeError):
        return -1


def cadastrar_pedido(fila):
    menu_pedido = Menu()
    cardapio_de_pedidos = Cardapio()
    tipo_de_pedido, identificador_de_pedido = menu_pedido.mostrar_cardapio()
    tipo_de_pedido = transformar_em_inteiro(tipo_de_pedido)
    identificador_de_pedido = transformar_em_inteiro(identificador_de_pedido)
    if cardapio_de_pedidos.validar_identificador(identificador_de_pedido, tipo_de_pedido):
        novo_pedido = Pedido(tipo_de_pedido, identificador_de_pedido)
        fila.enfileirar(novo_pedido)
        avisar_usuario('#Sucesso_Cadastro')
    else:
        avisar_usuario('#Tipo_Ou_Id_Invalido')


def mostrar_informacao_de_pedido(pedido):
    print(f'Tipo: {pedido.nome_tipo_pedido}')
    print(f'Identificador: {pedido.identificador_pedido}')
    print(f'Nome: {pedido.nome_pedido}')
    print(f'Preço: R${pedido.preco_pedido:,.2f}')


def mostrar_informacao_primeiro_pedido(fila):
    ultimo_pedido = fila.obter_primeiro_elemento()
    if not ultimo_pedido is None:
        print(f'{" PEDIDO ATUAL ":=^70}')
        mostrar_informacao_de_pedido(ultimo_pedido)
        print(f'{"=":=^70}')


def obter_resposta_do_usuario_para_proximo_pedido():
    escolha_do_usuario = input('\nV:Voltar | OK:Concluir Pedido: ').upper()
    return escolha_do_usuario == 'OK'


def remover_primeiro_pedido_da_fila(fila):
    fila.desenfileirar()


def mostrar_primeiro_pedido_e_proximo_se_usuario_desejar(fila):
    escolha_do_usuario = True
    menu_pedido = Menu()
    while escolha_do_usuario:
        if not fila.is_vazio():
            menu_pedido.limpar_console()
            mostrar_informacao_primeiro_pedido(fila)
            escolha_do_usuario = obter_resposta_do_usuario_para_proximo_pedido()
            if escolha_do_usuario:
                remover_primeiro_pedido_da_fila(fila)
                avisar_usuario('#Proximo_Pedido')
            else:
                break
        else:
            avisar_usuario('#Fila_Vazia')
            break


def mostrar_todos_os_pedidos(fila):
    menu_pedido = Menu()
    menu_pedido.limpar_console()
    ordem_de_pedido = 0
    for pedido in fila.fila:
        ordem_de_pedido += 1
        print(f'\n{f" PEDIDO {ordem_de_pedido} ":=^70}')
        mostrar_informacao_de_pedido(pedido)
    input('\nPrecione "ENTER" para continuar...')


def main():
    menu_pedido = Menu()
    fila_de_pedidos = Fila()
    while True:
        escolha_do_usuario = menu_pedido.mostrar_principal_opcoes()
        if escolha_do_usuario == '0':
            break
        match escolha_do_usuario:
            case '1': 
                cadastrar_pedido(fila_de_pedidos)

            case '2': 
                if not fila_de_pedidos.is_vazio():
                    mostrar_primeiro_pedido_e_proximo_se_usuario_desejar(fila_de_pedidos)
                else:
                    avisar_usuario('#Fila_Vazia')

            case '3': 
                if not fila_de_pedidos.is_vazio():
                    mostrar_todos_os_pedidos(fila_de_pedidos)
                else:
                    avisar_usuario('#Fila_Vazia')

            case _: 
                avisar_usuario('#Valor_Invalido')


if __name__ == "__main__":
    main()