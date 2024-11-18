import time
def fibonacci1(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)
        
tabela =[1, 4, 13, 15, 19, 20, 26, 33, 38]
lista_ = []

for i in (tabela):
    start_time = time.time()      
    print(fibonacci1(i))
    execution_time = time.time() - start_time
    lista_.append(execution_time)
    print("--- %s segundos ---" % execution_time)
print(lista_)    
