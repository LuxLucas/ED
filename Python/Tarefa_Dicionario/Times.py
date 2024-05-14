from os import system

def limpar_console():
    system('cls')


def obter_time():
    time = input('Qual time adicionar?: ').upper()
    return time


def validar_time(time, campeonato):
    return time in campeonato['times']


def cadastrar_time(campeonato):
    times_no_campeonato = campeonato['times']
    time = obter_time()
    times_no_campeonato.append(time)
    campeonato.update({"times":times_no_campeonato})
     
     
def obter_posicao_time(campeonato):
    times_no_campeonato = campeonato['times']
    try:
        time = input('Pesquisar posição do time: ').upper()
        if validar_time(time, campeonato):
            index = times_no_campeonato.index(time)
            print(f"A posição de {time} na lista é {index}")
        else:
            print('Erro: time não encontrado')
    except ValueError as erro:
        print(f'Erro: {erro}')


def remover_time(campeonato):
    times_no_campeonato = campeonato['times']
    try:
        time_indesejado = input('Time a remover: ').upper()
        if validar_time(time_indesejado, campeonato):
            times_no_campeonato.remove(time_indesejado)
            campeonato.update({"time":times_no_campeonato})
        else:
            print('Erro: time não encontrado')
    except ValueError as erro:
        print(f'Erro: {erro}')
        input('\nPrescione "ENTER... "')
    
    
def mostrar_times(campeonato):
    if len(campeonato) != 0:
        times_no_campeonato = campeonato['times']
        print(f'{"POSIÇÃO":<5}{"TIME":>20}')
        for time in times_no_campeonato:
            print(f'{times_no_campeonato.index(time):<5}{time:>20}')
    else:
        print('Sem times cadastrados')

def main():
    campeonato = {'times':[]}
    while True:
        limpar_console()
        print('1 - Adicionar time')
        print('2 - Pesquisar posição de time')    
        print('3 - Deletar time')
        print('4 - Mostrar times')
        print('5 - Sair')
        resposta = input('\nSeu comando: ')
        
        if resposta == '5':
            break
        
        match resposta:
            case '1': 
                limpar_console()
                cadastrar_time(campeonato)
                input('\nCadastro completo... ')
            case '2':
                limpar_console()
                obter_posicao_time(campeonato)
                input('\nTentativa de pesquisa encerrada... ')
            case '3': 
                limpar_console()
                remover_time(campeonato)
                input('\nTentativa de remoção encerrada... ')
            case '4':
                limpar_console()
                mostrar_times(campeonato)
                input('\n Seu comando...')
                
                
            
if __name__ == "__main__":
    main()