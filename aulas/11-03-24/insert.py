import os

#   Comando apresentados:
#       - .insert(index, elemento)

def Resposta_User():
    resposta = int(input('Deseja continuar ? (1:Sim || 2:NÃO): '))
       
    if resposta == 1:
        return True
    else:
        return False

def Limpar():
    os.system('cls')

def Mostrar_Lista(lista):
    indice = 0
    for elemento in lista:
        print(f'Elemento {indice + 1}: {elemento}')

lista = []
Resposta = True

while True:
    
    posicao = int(input('POSIÇÃO DO ELEMENTO: '))
    elemento = input('ELEMENTO: ')

    if posicao > len(lista):
        print(f'{"POSIÇÃO INVÁLIDA":=^50}')
        Limpar()
    else:
        lista.insert(posicao, elemento)

    Limpar()   
    Resposta = Resposta_User()
 
print(f'{"RESULTADO":=^50}')
Mostrar_Lista(lista)
