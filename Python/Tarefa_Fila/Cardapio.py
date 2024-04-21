class Cardapio:
    def __init__(self):
        self.NomeTipo = self.iniciarNomeTipo()
        self.NomeLanche = self.iniciarNomeLanche()
        self.PrecoLanche = self.iniciarPrecoLanche()
        self.NomeBebida = self.iniciarNomeBebida()
        self.PrecoBebida = self.iniciarPrecoBebida()
        self.NomeSobremesa = self.iniciarNomeSobremesa()
        self.PrecoSobremesa = self.iniciarPrecoSobremesa()


    def iniciarNomeTipo(self):
        NomeTipo = ['Lanche', 
                    'Bebida', 
                    'Sobremesa']
        return NomeTipo


    def iniciarNomeLanche(self):
        NomePedido = ['Chicken Bacon Catupiry',
                      'Whopper Bacon Catupiry',
                      'Chicken Júnior',
                      'BK Original',
                      'Rodeio']
                      
        return NomePedido
    

    def iniciarPrecoLanche(self):
        PrecoLanche = [25.67, 24.45, 18.30, 20.87, 22.58]
        return PrecoLanche
    

    def iniciarNomeBebida(self):
        NomeBebida = ['Refrigerante',
                      'Suco Natural',
                      'Água']
        return NomeBebida
    

    def iniciarPrecoBebida(self):
        PrecoBebida = [2.5, 3, 2]
        return PrecoBebida
    

    def iniciarNomeSobremesa(self):
        NomeSobremesa = ['Sorvete',
                         'Bolo']
        return NomeSobremesa
    
    def iniciarPrecoSobremesa(self):
        PrecoSobremesa = [5, 7]
        return PrecoSobremesa
    

    def identificadorInLanche(self, identificador):
        IdentificadorEncontrado = identificador >= 0 and identificador <= len(self.NomeLanche)-1
        return IdentificadorEncontrado
    

    def identificadorInBebida(self, identificador):
        IdentificadorEncontrado = identificador >= 0 and identificador <= len(self.NomeBebida)-1
        return IdentificadorEncontrado
    

    def identificadorInSobremesa(self, identificador):
        IdentificadorEncontrado = identificador >= 0 and identificador<=len(self.NomeSobremesa)-1
        return IdentificadorEncontrado
        

    def validarIdentificador(self, identificador, tipo):
        match tipo:
            case 0: return self.identificadorInLanche(identificador)
            case 1: return self.identificadorInBebida(identificador)
            case 2: return self.identificadorInSobremesa(identificador)
            case _: return False


    def procurarNomeTipoPedido(self, tipo):
        match tipo:
            case 0: return self.NomeTipo[0]
            case 1: return self.NomeTipo[1]
            case 2: return self.NomeTipo[2]
            case _: return None


    def procurarNomeLanche(self, identificador):
        NomeDoLanche = self.NomeLanche[identificador]
        return NomeDoLanche


    def procurarNomeBebida(self, identificador):
        NomeDaBebida = self.NomeBebida[identificador]
        return NomeDaBebida
    

    def procurarNomeSobremesa(self, identificador):
        NomeDaSobremesa = self.NomeSobremesa[identificador]
        return NomeDaSobremesa


    def procurarNomePedido(self, identificador, tipo):
        match tipo:
            case 0: return self.procurarNomeLanche(identificador)
            case 1: return self.procurarNomeBebida(identificador)
            case 2: return self.procurarNomeSobremesa(identificador)
            case _: None


    def procurarPrecoLanche(self, identificador):
        PrecoDoLanche = self.PrecoLanche[identificador]
        return PrecoDoLanche


    def procurarPrecoBebida(self, identificador):
        PrecoDaBebida = self.PrecoBebida[identificador]
        return PrecoDaBebida
    

    def procurarPrecoSobremesa(self, identificador):
        PrecoDaSobremesa = self.PrecoSobremesa[identificador]
        return PrecoDaSobremesa


    def procurarPrecoPedido(self, identificador, tipo):
        match tipo:
            case 0: return self.procurarPrecoLanche(identificador)
            case 1: return self.procurarPrecoBebida(identificador)
            case 2: return self.procurarPrecoSobremesa(identificador)
            case _: None


    def mostarCardapio(self):
        NomeCardapio = [self.NomeLanche, self.NomeBebida, self.NomeSobremesa]
        PrecoCardapio = [self.PrecoLanche, self.PrecoBebida, self.PrecoSobremesa]

        print(f'{" CARDÁPIO ":=^70}')

        for tipo in range(len(self.NomeTipo)):
            print(f'\nTipo:{tipo} - Nome:{self.NomeTipo[tipo].upper()}')
            for index in range(len(NomeCardapio[tipo])):
                print(f'|--- Identificador: {index:2,}| Nome: {NomeCardapio[tipo][index]:<25}| Preço: R${PrecoCardapio[tipo][index]:4,.2f}')
