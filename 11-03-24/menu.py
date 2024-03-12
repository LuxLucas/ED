import os

def Limpar():
    os.system('cls')
    
def Inserir_Na_Lista(Elemento, Lista):
    Lista.append(Elemento)
    print(f'{"Elemento {Elemento} inserido na lista":-^50}')
    
def Mostrar_Lista(Lista):
    Index = 0
    for Elemento in Lista:
        print(f'Elemento {Index+1}: {Elemento}\n')
        
    
# Funcção prinpal
def main():
    
    Lista = []
    
    while True:
        print(f'\nOpção 1: Inserir Elemento')
        print('Opção 2: Encerrar programa')
        
        opcao = input('\nEscolha sua opção: ')
        
        if opcao == '1':
            Limpar()
            Elemento = input('Elemento para adicionar:')
            Inserir_Na_Lista(Elemento, Lista)
            
        elif opcao == '2':
            print(f'{"PROGRAMA ENCERRADO":=^50}')
            break
        
        else:
            print(f'{"OPÇÃO INVÁLIDA":=^50}')
            
    Limpar()
    print(f'{"MOSTRANDO RESULTADO":=^50}')
    Mostrar_Lista(Lista)
           
if __name__ == "__main__":
    main()  
    