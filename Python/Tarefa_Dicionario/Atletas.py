from os import system

def limpar_console():
    system('cls')


def obter_atleta():
    nome_atleta = input('Nome do atleta: ')
    return nome_atleta.upper()


def obter_esporte():
    esporte = input('Esporte: ')
    return esporte.upper()


def cadastrar_atleta(competicao):
    nome_atleta = obter_atleta()
    esporte = obter_esporte()
    competicao[nome_atleta] = esporte


def validar_atleta(nome_atleta, competicao):
    return nome_atleta in competicao


def pesquisar_esporte(competicao):
    atleta = input('Pesquisar o esporte de qual atleta?: ').upper()
    if validar_atleta(atleta, competicao):
        esporte = competicao[atleta]
        print(f'O esporte de {atleta} é {esporte}')
    else:
        print('Erro: atleta não encontrado')


def alterar_esporte(competicao):
    atleta = input('Alterar a esporte de qual atleta?: ').upper()
    if validar_atleta(atleta, competicao):
        esporte = input(f'Novo esporte para {atleta}: ').upper()
        competicao.update({atleta:esporte})
    else:
        print('Erro: atleta não encontrado')


def remover_atleta(campeonato):
    try:
        atleta_indesejado = input('Atleta a remover: ').upper()
        if validar_atleta(atleta_indesejado, campeonato):
            del campeonato[atleta_indesejado]
            print(f"Atleta removido")
        else:
            print('Erro: atleta não encontrado')
    except ValueError as erro:
        print(f'Erro: {erro}')
        input('\nPrescione "ENTER... "')


def mostrar_atletas(competicao):
    if len(competicao) != 0:
        print(f'{"ATLETA":<30}{"ESPORTE":>30}')
        for atleta in competicao.keys():
            print(f'{atleta:<30}{competicao[atleta]:>30}')
    else:
        print('Sem estados cadastrados')


def main():
    atletas = {}
    while True:
        limpar_console()
        print('1 - Adicionar atleta')
        print('2 - Pesquisar esporte de atleta')    
        print('3 - Alterar esporte de atleta')
        print('4 - Mostrar atletas')
        print('5 - Deletar atleta')
        print('6 - Sair')
        resposta = input('\nSeu comando: ')
        
        if resposta == '6':
            break
        
        match resposta:
            case '1': 
                limpar_console()
                cadastrar_atleta(atletas)
                input('\nAtleta cadastrado... ')
            case '2':
                limpar_console()
                pesquisar_esporte(atletas)
                input('\nTentativa de pesquisa completa...')
            case '3': 
                limpar_console()
                alterar_esporte(atletas)
                input('\nTentativa de alteração completa...')
            case '4':
                limpar_console()
                mostrar_atletas(atletas)
                input('\nSeu comando...')
            case '5':
                limpar_console()
                remover_atleta(atletas)
                input('\nTentativa de remoção completa...')
                
            
if __name__ == "__main__":
    main()