from Cardapio import Cardapio

# Tipo: 0 a 2
# Identificador: tipo:0 - de 0 a 4 | tipo 1: - de 0 a 2 | tipo 2: - de 0 a 1
class Pedido:
    def __init__(self, tipo, identificador):
        cardapio_de_pedidos = Cardapio()
        if cardapio_de_pedidos.validar_identificador(identificador, tipo):
            self.identificador_pedido = identificador
            self.nome_tipo_pedido = cardapio_de_pedidos.procurar_nome_do_tipo_de_pedido(tipo)
            self.nome_pedido = cardapio_de_pedidos.procurar_nome_pedido(identificador, tipo)
            self.preco_pedido = cardapio_de_pedidos.procurar_preco_pedido(identificador, tipo)
    