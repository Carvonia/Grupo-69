import os
from hash_table import Hash

class Menu:
    def __init__(self, tab):
        self.tab = tab

    def inserir(self, quantidade):
        for _ in range(quantidade):
            nome = input("Forneca o nome a ser inserido: ").capitalize()
            if not self.tab.inserir(nome, nome):
                break
        self.printcontent()

    def buscar(self, item):
        pos = self.tab.busca(item)
        if pos == -1:
            print("Nome não encontrado / Valor Inválido\n")
        else:
            print(f"Nome <{item}> encontrado na posicao: {pos}!\n")
        input("Pressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.printcontent()

    def apagar(self, item):
        self.tab.apaga(item)
        input("Pressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.printcontent()

    def printcontent(self):
        self.tab.imprime()
