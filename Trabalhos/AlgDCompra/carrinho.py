from produto import Produto
class Carrinho:

    def __init__(self, codigo):
        self.lista = []
        self.addProduct()

    def __str__(self):
        print(f"Nome: {self.nome} - Preço: {self.preco}")

    def addProduct(self, codigo):
        self.lista.append(self.codigo)

    def removerItem(self, item):
        self.lista.remove(item)

    def showProducts (self):
        print(Produto.showProduct())