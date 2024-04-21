<<<<<<< HEAD
from Cardapio import Cardapio

# Tipo: 0 a 2
# Identificador: tipo:0 - de 0 a 4 | tipo 1: - de 0 a 2 | tipo 2: - de 0 a 1
class Pedido:
    def __init__(self, tipo, identificador):
        CardapioPedido = Cardapio()
        if CardapioPedido.validarIdentificador(identificador, tipo):
            self.IdentificadorPedido = identificador
            self.NomeTipoPedido = CardapioPedido.procurarNomeTipoPedido(tipo)
            self.NomePedido = CardapioPedido.procurarNomePedido(identificador, tipo)
            self.PrecoPedido = CardapioPedido.procurarPrecoPedido(identificador, tipo)
=======
from Cardapio import Cardapio

# Tipo: 0 a 2
# Identificador: tipo:0 - de 0 a 4 | tipo 1: - de 0 a 2 | tipo 2: - de 0 a 1
class Pedido:
    def __init__(self, tipo, identificador):
        CardapioPedido = Cardapio()
        if CardapioPedido.validarIdentificador(identificador, tipo):
            self.IdentificadorPedido = identificador
            self.NomeTipoPedido = CardapioPedido.procurarNomeTipoPedido(tipo)
            self.NomePedido = CardapioPedido.procurarNomePedido(identificador, tipo)
            self.PrecoPedido = CardapioPedido.procurarPrecoPedido(identificador, tipo)
>>>>>>> fbe8aacedfd0e9bde2aaf0c26a699d9fa5cbf0ca
    