import time
def fibonacci1(n, table = {}):
    if n == 1 or n == 0:
        return n
    try:
        return table[n]
    except:
        table[n] = fibonacci1(n-1) + fibonacci1(n-2)
        return table[n]
        
start_time = time.time()      
print(fibonacci1(19))
execution_time = time.time() - start_time
print("--- %s segundos ---" % execution_time)

tabela =[1, 4, 13, 15, 19, 20, 26, 33, 38, 43]
lista_ = []

for i in (tabela):
    start_time = time.time()      
    print(fibonacci1(i))
    execution_time = time.time() - start_time
    lista_.append(execution_time)
    print("--- %s segundos ---" % execution_time)
print(lista_)