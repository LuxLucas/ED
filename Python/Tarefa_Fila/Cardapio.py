class Cardapio:
    def __init__(self):
        self.nome_tipo = self.iniciar_nome_tipo()
        self.nome_lanche = self.iniciar_nome_lanche()
        self.preco_lanche = self.iniciar_preco_lanche()
        self.nome_bebida = self.iniciar_nome_bebida()
        self.preco_bebida = self.iniciar_preco_bebida()
        self.nome_sobremesa = self.iniciar_nome_sobremesa()
        self.preco_sobremesa = self.iniciar_preco_sobremesa()


    def iniciar_nome_tipo(self):
        nome_tipo = ['Lanche', 
                    'Bebida', 
                    'Sobremesa']
        return nome_tipo


    def iniciar_nome_lanche(self):
        nome_lanche = ['Chicken Bacon Catupiry',
                      'Whopper Bacon Catupiry',
                      'Chicken Júnior',
                      'BK Original',
                      'Rodeio']
                      
        return nome_lanche
    

    def iniciar_preco_lanche(self):
        preco_lanche = [25.67, 24.45, 18.30, 20.87, 22.58]
        return preco_lanche
    

    def iniciar_nome_bebida(self):
        nome_bebida = ['Refrigerante',
                      'Suco Natural',
                      'Água']
        return nome_bebida
    

    def iniciar_preco_bebida(self):
        preco_bebida = [2.5, 3, 2]
        return preco_bebida
    

    def iniciar_nome_sobremesa(self):
        nome_sobremesa = ['Sorvete',
                         'Bolo']
        return nome_sobremesa
    
    def iniciar_preco_sobremesa(self):
        preco_sobremesa = [5, 7]
        return preco_sobremesa
    

    def encontrar_identificador_em_lanche(self, identificador):
        identificador_encontrado = identificador >= 0 and identificador <= len(self.nome_lanche)-1
        return identificador_encontrado
    

    def encontrar_identificador_em_bebida(self, identificador):
        identificador_encontrado = identificador >= 0 and identificador <= len(self.nome_bebida)-1
        return identificador_encontrado
    

    def encontrar_identificador_em_sobremesa(self, identificador):
        identificador_encontrado = identificador >= 0 and identificador<=len(self.nome_sobremesa)-1
        return identificador_encontrado
        

    def validar_identificador(self, identificador, tipo):
        match tipo:
            case 0: return self.encontrar_identificador_em_lanche(identificador)
            case 1: return self.encontrar_identificador_em_bebida(identificador)
            case 2: return self.encontrar_identificador_em_sobremesa(identificador)
            case _: return False


    def procurar_nome_do_tipo_de_pedido(self, tipo):
        match tipo:
            case 0: return self.nome_tipo[0]
            case 1: return self.nome_tipo[1]
            case 2: return self.nome_tipo[2]
            case _: return None


    def procurar_nome_de_lanche_por_identificador(self, identificador):
        nome_do_lanche = self.nome_lanche[identificador]
        return nome_do_lanche


    def procurar_nome_de_bebida_por_identificador(self, identificador):
        nome_da_bebida = self.nome_bebida[identificador]
        return nome_da_bebida
    

    def procurar_nome_de_sobremesa_por_identificador(self, identificador):
        nome_da_sobremesa = self.nome_sobremesa[identificador]
        return nome_da_sobremesa


    def procurar_nome_pedido(self, identificador, tipo):
        match tipo:
            case 0: return self.procurar_nome_de_lanche_por_identificador(identificador)
            case 1: return self.procurar_nome_de_bebida_por_identificador(identificador)
            case 2: return self.procurar_nome_de_sobremesa_por_identificador(identificador)
            case _: None


    def procurar_preco_lanche(self, identificador):
        preco_do_lanche = self.preco_lanche[identificador]
        return preco_do_lanche


    def procurar_preco_bebida(self, identificador):
        preco_da_bebida = self.preco_bebida[identificador]
        return preco_da_bebida
    

    def procurar_preco_sobremesa(self, identificador):
        preco_da_sobremesa = self.preco_sobremesa[identificador]
        return preco_da_sobremesa


    def procurar_preco_pedido(self, identificador, tipo):
        match tipo:
            case 0: return self.procurar_preco_lanche(identificador)
            case 1: return self.procurar_preco_bebida(identificador)
            case 2: return self.procurar_preco_sobremesa(identificador)
            case _: None


    def mostrar_cardapio(self):
        nomes_no_cardapio = [self.nome_lanche, self.nome_bebida, self.nome_sobremesa]
        precos_no_cardapio = [self.preco_lanche, self.preco_bebida, self.preco_sobremesa]

        print(f'{" CARDÁPIO ":=^70}')

        for tipo in range(len(self.nome_tipo)):
            print(f'\nTipo:{tipo} - Nome:{self.nome_tipo[tipo].upper()}')
            for index in range(len(nomes_no_cardapio[tipo])):
                print(f'|--- Identificador: {index:2,}| Nome: {nomes_no_cardapio[tipo][index]:<25}| Preço: R${precos_no_cardapio[tipo][index]:4,.2f}')
