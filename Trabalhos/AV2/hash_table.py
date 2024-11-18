class Hash:
    def __init__(self, tam, hash_metodo='div'):
        self.tab = {}
        self.tam_max = tam
        self.hash_metodo = hash_metodo

    def funcaohash(self, chave):
        if self.hash_metodo == 'div':
            v = str(chave)
            return len(v) % self.tam_max
        
        if self.hash_metodo == 'normal':
            v = str(chave)
            return len(v) - 1

        if self.hash_metodo == 'multiplicacao':
            return self.hash_multi(chave)

        if self.hash_metodo == 'dobra':
            return self.hash_dobra(chave)

    def hash_dobra(self, chave):
        v = len(chave)
        str_v = str(v)
        part = 2
        total = sum(int(str_v[i:i+part]) for i in range(0, len(str_v), part))
        return total % self.tam_max

    def hash_multi(self, chave):
        v = len(chave)
        part_fracionaria = (v * 0.61803398875) % 1
        return int(part_fracionaria * self.tam_max)

    def cheia(self):
        return len(self.tab) >= self.tam_max

    def imprime(self):
        x = sorted(self.tab)
        for i in x:
            print("Hash[%d] = " % i, end="")
            print(self.tab[i])

    def apaga(self, chave):
        pos = self.busca(chave)
        nome = self.tab.get(pos)
        if pos != -1:
            del self.tab[pos]
            print(f"-> Nome <{nome}> na posicao [{pos}] apagado.")
        else:
            print("Nome nao encontrado")

    def busca(self, chave):
        pos = self.funcaohash(chave)
        return pos if self.tab.get(pos) else -1

    def inserir(self, chave, valor):
        if self.cheia():
            print("Tabela cheia")
            return False
        pos = self.funcaohash(chave)
        if self.tab.get(pos) is None:
            self.tab[pos] = valor
            return True
        else:
            print("Posição já ocupada")
            return False
