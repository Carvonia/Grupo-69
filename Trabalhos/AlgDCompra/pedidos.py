class Pedido:

    codigo = 0
    lista = []

    def __init__(self, codproduto, quantidade):
        self.codproduto = codproduto
        self.quantidade = quantidade
        self.status = False
        Pedido.codigo += 1
        self.codigo = Pedido.codigo

    def addProduct(self):
        self.lista.append(self.codproduto)


p1 = Pedido()