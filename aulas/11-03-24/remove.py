import os

#   Comandos apresentados:
#       - .pop(remove_index)
#       - .remove(remove_element)

def Limpar():
    os.system('cls')

lista = [1, 2, 6, 67, 90]

def Remove_By_Element():
    while True:
        Limpar()
        element_remove = int(input('Elemento a remover: '))

        if element_remove in lista:
            lista.remove(element_remove)
            print('ELEMENTO REMOVIDO')
            print(lista)
            break
            
        else:
            print('ELEMENTO NÃO EXITA NA LISTA')
            
def Remove_By_Index():
    while True:
        Limpar()
        index_remove = int(input('Posição a remover: '))
        
        if (index_remove < 0) or (index_remove >= len(lista)):
            print(f'{"POSIÇÃO INVÁLIDA":=^50}')
        else:
            lista.pop(index_remove)
            print(f'{"ELEMENTO REMOVIDO PELO ÍNDEX":=^50}')
            print(f'{lista}')

