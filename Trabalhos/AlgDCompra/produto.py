class Produto:
    codigo = 0
    lista = []

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        Produto.codigo += 1
        self.codigo = Produto.codigo
        self.addProduct()

    def __str__(self):
        print(f"Nome: {self.nome} - Preço: {self.preco}")


    def addCodigo(self, codigo):
        codigo = self.codigo+1

    def addProduct(self):
        self.lista.append(self.codigo)
    
    def showProduct (self):
      for product in self.lista:
          print(product)

p1 = Produto("Mouse", "10.50")
p2 = Produto("Rato", "16.10")
p3 = Produto("Papel", "30.33")
p4 = Produto("Barril", "5.81")
print(p4.lista)