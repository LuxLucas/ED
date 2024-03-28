import os

#    Comandos apresentados:
#       - .append(elemento_inserido)

def Limpar():
    os.system('cls')

#   Mostra as "pessoas" da lista
def Mostrar_Lista(Lista):
    for Pessoa in Lista:
         print(f'Nome: {Pessoa['nome']}\nIdade: {Pessoa['idade']}\nCidade: {Pessoa['cidade']}\n')

lista_pessoa = []

while True:
    print(f'{"CADASTRO PESSOA":=^50}')
    nome = (input('Digite seu nome (ou "0" para sair): ')).upper()
    
    if nome == '0':
        break
    
    print(f'\n{"CONTINUAR CADASTRO":=^50}')
    idade = int(input('Sua idade: '))
    cidade = (input('Sua cidade: ')).upper()
    
    pessoa = {'nome': nome, 'idade': idade, 'cidade': cidade}
    
    lista_pessoa.append(pessoa)

Limpar()

Mostrar_Lista(lista_pessoa)
