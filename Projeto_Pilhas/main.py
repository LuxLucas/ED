import Pilha, Menu

Menu = Menu.Menu()


def confirmar_criacao_pilha(pilha):
    if not(type(pilha) is object) and pilha == None:
        Menu.avisar_usuario('Pilha Não Criada')
        return False
    else:
        return True


def criar_pilha():
    tamanho = Menu.tamanho_pilha()
    if tamanho != None:
        nova_pilha = Pilha.Pilha(tamanho)
        Menu.avisar_usuario('Pilha Criada')
        return nova_pilha
    Menu.avisar_usuario('Tamanho INVÁLIDO')


def adicionar_elemento(pilha):
    if pilha.cheia():
        Menu.avisar_usuario('Pilha Cheia')
    else:    
        elemento = Menu.receber_elemento()
        if elemento != '':
            pilha.empilhar(elemento)
        else:
            Menu.avisar_usuario('Elemento INVÁLIDO')

def remover_ultimo_elemento(pilha):
    if pilha.vazia():
        Menu.avisar_usuario('Pilha Vazia')
    else:
        elemento_removido = pilha.desempilhar()
        Menu.avisar_usuario(f"Elemento {elemento_removido} REMOVIDO")
    

def verificar_pilha_cheia(pilha):
    if pilha.cheia():
        Menu.avisar_usuario("Pilha Está CHEIA")
    else:
        Menu.avisar_usuario("Pilha Não Está CHEIA")

    
    
def verificar_pilha_vazia(pilha):
    if pilha.vazia():
        Menu.avisar_usuario("Pilha Vazia")
    else:
        Menu.avisar_usuario("Pilha Não Está VAZIA")


def mostrar_todos_elementos(pilha):
    Menu.limpar_console()
    if pilha.vazia() :
        print(f'Pilha Vazia')
    else:
        print(f'{"IMPRIMINDO PILHA":=^60}')
        while pilha.ultimo_indice != -1:
            elemento = pilha.desempilhar()
            print(f'Índice: {pilha.ultimo_indice+1} || Elemento: {elemento}')

    Menu.terminar_mensagem()


def contar_elementos(pilha):
    aviso = f'Quantidade de elementos: {pilha.ultimo_indice + 1}'
    Menu.avisar_usuario(aviso)


def main():
    Pilha = None

    while True:
        resposta = Menu.opcoes_principais()

        if resposta == '0':
            break
        match resposta:
            case '1':
                Pilha = criar_pilha()
            case '2':
                if confirmar_criacao_pilha(Pilha):
                    adicionar_elemento(Pilha)
            case '3':
                if confirmar_criacao_pilha(Pilha):
                    remover_ultimo_elemento(Pilha)
            case '4':
                if confirmar_criacao_pilha(Pilha):
                    mostrar_todos_elementos(Pilha)
            case '5':
                if confirmar_criacao_pilha(Pilha):
                    verificar_pilha_cheia(Pilha)
            case '6':
                if confirmar_criacao_pilha(Pilha):
                    verificar_pilha_vazia(Pilha)
            case '7':
                if confirmar_criacao_pilha(Pilha):
                    contar_elementos(Pilha)
            case _:
                Menu.limpar_console()
                print('Comando INVÁLIDO')
                Menu.terminar_mensagem()
    
    
if __name__ == "__main__":
    main()