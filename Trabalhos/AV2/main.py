import os
from hash_table import Hash
from menu import Menu

def main():
    tamanhoHash = int(input("Forneca o tamanho da Tabela Hash: "))
    metodo = input("Escolha o método de hash (div, normal, multiplicacao, dobra): ")
    tab = Hash(tamanhoHash, metodo)
    menu = Menu(tab)
    sair = False

    while not sair:
        length = len(tab.tab)
        print(f"-Tabela HASH Teste- {length} de {tamanhoHash} itens\n\n")
        resposta = int(input("Você deseja:\n1 - Inserir um nome\n2 - Buscar um nome\n3 - Apagar um nome\n4 - Sair\nR: "))
        os.system('cls' if os.name == 'nt' else 'clear')

        if resposta == 1:
            while True:
                try:
                    quantidade = int(input("Quantos nomes você deseja inserir?\nR: "))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if quantidade <= 0:
                        print("ERRO: A quantidade de nomes a se inserir deve ser maior que zero!\n")
                        continue
                    menu.inserir(quantidade)
                    break
                except Exception as e:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"ERRO {e}: Tente digitar um número inteiro!\n")
        elif resposta == 2:
            item = input("\n - Forneca um nome inteiro para buscar: ").capitalize()
            os.system('cls' if os.name == 'nt' else 'clear')
            menu.buscar(item)
        elif resposta == 3:
            item = input("\n - Forneca um nome para apagar: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            menu.apagar(item)
        elif resposta == 4:
            sair = True
        else:
            print("ERRO: Opção inválida!\n")

    print("-Encerrando...")

if __name__ == "__main__":
    main()
