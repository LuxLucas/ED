from os import system

def limpar_console():
    system('cls')


def obter_serie():
    serie = input('Qual série adicionar?: ')
    return serie


def cadastrar_serie(catalogo):
    lista = catalogo['lista']
    serie = obter_serie()
    lista.append(serie)
    catalogo.update({"lista":lista})
     
     
def obter_posicao_serie(catalogo):
    lista = catalogo['lista']
    try:
        serie = input('Pesquisar posição da série: ')
        index = lista.index(serie)
        return index
    except ValueError as erro:
        print(f'Erro: {erro}')
        input('\nPrescione "ENTER... "')


def remover_serie(catalogo):
    lista = catalogo['lista']
    try:
        serie_indesejada = input('Série a remover: ')
        lista.remove(serie_indesejada)
        catalogo.update({"lista":lista})
    except ValueError as erro:
        print(f'Erro: {erro}')
        input('\nPrescione "ENTER... "')
    
    
def mostrar_series(catalogo):
    series = catalogo['lista']
    return series

def main():
    catalogo = {'lista':[]}
    while True:
        limpar_console()
        print('1 - Adicionar série')
        print('2 - Pesquisar posição série')    
        print('3 - Deletar série')
        print('4 - Mostrar séries')
        print('5 - Sair')
        resposta = input('\nSeu comando: ')
        
        if resposta == '5':
            break
        
        match resposta:
            case '1': 
                limpar_console()
                cadastrar_serie(catalogo)
            case '2':
                limpar_console()
                index = obter_posicao_serie(catalogo)
                print(f'Posição: {index}')
                input('Seu comando? ')
            case '3': 
                limpar_console()
                remover_serie(catalogo)
            case '4':
                limpar_console()
                series = mostrar_series(catalogo)
                print(series)
                input('Seu comando? ')
                
            
if __name__ == "__main__":
    main()