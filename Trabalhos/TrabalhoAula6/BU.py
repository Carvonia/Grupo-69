import time
def fibonacciBottomUp(n, table = {}):
    table[0] = 0
    table[1] = 1
    for cont in range(2, n + 1):
        table[cont] = table[cont - 1] +  table[cont - 2]
    return table[n]
    
start_time = time.time()      
print(fibonacciBottomUp(19))
execution_time = time.time() - start_time
print("--- %s segundos ---" % execution_time)  

tabela =[1, 4, 13, 15, 19, 20, 26, 33, 38, 43]
lista_ = []

for i in (tabela):
    start_time = time.time()      
    print(fibonacciBottomUp(i))
    execution_time = time.time() - start_time
    lista_.append(execution_time)
    print("--- %s segundos ---" % execution_time)
print(lista_)