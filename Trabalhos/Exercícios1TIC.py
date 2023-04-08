import os
from functools import reduce
import random
import operator
import locale
locale.setlocale( locale.LC_ALL, '' )

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_currency(i):
    return locale.currency(float(i), grouping=True)

def main():
    LoopExercise = 'y'
    while LoopExercise == 'y' or LoopExercise == 'Y':
        while True:
            try:
                Exercise = int(input('Qual exercício você deseja acessar? \n'))
                break

            except ValueError:
                print('Exercício inválido, tente novamente! \n')
        cls()
        while True:
            if Exercise == 1:
                Exercises.exercise1()
                break
            elif Exercise == 2:
                Exercises.exercise2()
                break
            elif Exercise == 3:
                Exercises.exercise3()
                break
            elif Exercise == 4:
                Exercises.exercise4()
                break
            elif Exercise == 5:
                Exercises.exercise5()
                break
            elif Exercise == 6:
                Exercises.exercise6()
                break 
            elif Exercise == 7:
                Exercises.exercise7()
                break
            elif Exercise == 8:
                Exercises.exercise8()
                break
            elif Exercise == 9:
                Exercises.exercise9()
                break
            elif Exercise == 10:
                Exercises.exercise10()
                break
            elif Exercise == 11:
                Exercises.exercise11()
                break
            elif Exercise == 12:
                Exercises.exercise12()
                break
            elif Exercise == 13:
                Exercises.exercise13()
                break
            elif Exercise == 14:
                Exercises.exercise14()
                break
            elif Exercise == 15:
                Exercises.exercise15()
                break
            else:
                break
        if Exercise < 16 and Exercise > 0: 
            LoopExercise = str(input("Deseja acessar outro exercício? (y/n) \n"))
            cls()
        else: print('Exercício inválido, tente novamente!\n')

class Exercises():
    def exercise1():
        Soma = 0.0
        for i in range (0, 2):
            while True:
                try:
                    Soma += float(input('Digite um número: '))
                    break

                except ValueError:
                    print('Digite um número válido! \n')
                
        print(f'A soma dos número é igual a {Soma}. \n')

    def exercise2():
        Area = 0.0
        while True:
            try:
                Area += float(input('Insira o valor do lado do seu Quadrado: '))
                break
            except ValueError:
                print('Utilize apenas números! \n')
        
        print(f'A área do seu quadrado é {Area * 2}')

    def exercise3():
        while True:
            try:
                Farenheit = float(input('Insira o valor da temperatura em Farenheit: \n'))
                break

            except ValueError:
                print('Insira um valor válido!!! \n')

        Celsius = 5*((Farenheit - 32)/9)
        print (f"O Valor em Celsius será de {Celsius} \n")

    def exercise4():
        while True:
            try:
                AlturaIMC = float(input('Digite a sua altura em metros Por Favor: '))
                PesoIMC = float(input('Digite o seu peso em Kgs Por Favor: '))
                break
            except ValueError:
                print('Utilize apenas números por favor.')    

        IMC = PesoIMC/(AlturaIMC*AlturaIMC)
        print(f'\n Seu índice do IMC é {IMC}')

    def exercise5():
        while True:
            try:
                Polegadas = float(input('Insira o valor em polegadas para ser convertido em cm: '))
                break
            except ValueError:
                print('Utilize apenas números por favor.')
        Centimetros = Polegadas*2.54
        print(f'O Valor em centímetros é {Centimetros}! \n')

    def exercise6():
        while True:
            try:
                BaseTriangulo = float(input('Insira o valor da base do triangulo a ser convertido: '))
                AlturaTriangulo = float(input('Agora insira a altura do triangulo :'))
                break
            except ValueError:
                print('Utilize apenas números por favor.')
        AreaTriangulo = (BaseTriangulo*AlturaTriangulo)/2
        print(f'\n O Valor da área deste triângulo é {AreaTriangulo}! \n')

    def exercise7():
        while True:
            try:
                Idade = int(input('Insira a sua idade: '))
                break
            except ValueError:
                print('Utilize apenas números cheios.')

        DiasDeVida = Idade*365
        print(f'Você tem {DiasDeVida} dias de vida! \n')

    def exercise8():
        while True:
            try:
                Dividendo = float(input('Insira o Dividendo da operação: '))
                Divisor = float(input('Insira o Divisor da operação: '))
                ResultadoDivisao = Dividendo/Divisor
                if ResultadoDivisao == 0:
                    print('Divisão indefinida')
                else: print(f'O resultado da divisão é {ResultadoDivisao}. \n')
                break
            except ZeroDivisionError: print('É impossível dividir por 0, tente novamente.\n')
            except ValueError: print('Utilize apenas números!\n')

    def exercise9():
        while True:
            try:
                Idade = int(input('Insira a sua idade: '))
                break
            except ValueError:
                print('Utilize apenas números por favor.')
        if Idade >= 18:
            print('Ta liberado a Skol e o Churras! \n')
        elif Idade > 65:
            print('O vovô vai pro hospital fazendo favor. \n')
        elif Idade <= 0:
            print('Você tá bem irmão? \n')
        else:
            print('Pode vir pro Churras, mas vai ficar só no Guaravita ein!')
            
    def exercise10():
        while True:
            try:
                ValorQuadrado = int(input('Insira o valor desejado: '))
                if ValorQuadrado == 0: break
                print(f'O valor inserido ao quadrado é {ValorQuadrado*ValorQuadrado} \n')
                break
                        
            except ValueError:
                print('Utilize apenas números por favor.')
            
    def exercise11():
        while True:
            try:
                ValorBase = float(input('Insira o valor a ser exponenciado: '))
                Exponente = int(input('Insira o exponente: '))
                ResultadoExp = ValorBase
                break

            except ValueError:
                print('Utilize apenas números por favor.')
                
        for i in range(1, Exponente):
                ResultadoExp = ResultadoExp * ValorBase

        print(f'O resultado da exponenciação é: {ResultadoExp} \n')

    def exercise12():
        RandomNumb = random.randint(0, 100)
        for i in range (1, 10):
            while True:
                try:
                    Advinha = int(input('Tente advinhar o número aleatório! '))
                    if Advinha == RandomNumb:
                        print(f'\nParabéns! O número realmente era {RandomNumb}!!!')
                        i = 11
                        break
                    elif Advinha > RandomNumb:
                        print('\nOps, o número aleatório é menor que o que vc inseriu.')
                        print(f'Você tem {10-i} de tentativas restantes. \n')
                    elif Advinha < RandomNumb:
                        print('\nOps, o número aleatório é maior que o que vc inseriu.')
                        print(f'Você tem {10-i} de tentativas restantes. \n')
                    break
                except ValueError:
                    print('Utilize apenas numeros cheios')
            if Advinha == RandomNumb: break
        if Advinha != RandomNumb:
            print('Você perdeu! :( \n')

    def exercise13():
        idadeNamorado = []
        idadeNamorada = []
        idadeNamoro = []

        for i in range(0, 2500):
            idadeNamorado.append(random.randint(18, 40))
            idadeNamorada.append(random.randint(18, 40))
            idadeNamoro.append(random.randint(1, 10))

        mediaNamorado = (reduce(operator.add, idadeNamorado))/2500
        mediaNamorada = (reduce(operator.add, idadeNamorada))/2500
        mediaNamoro = ((reduce(operator.add, idadeNamoro))/2500)
        print(f'Em média a idade do namorado da pesquisa foi {mediaNamorado},')
        print(f'a idade da namorada resultou em {mediaNamorada},')
        print(f'e o tempo de namoro em anos foi de {mediaNamoro}. \n')

    def exercise14():
        EstoqueJogos = []
        EstoqueVendidos = []
        Tempo = 0

        for i in range(0,64):
            EstoqueJogos.append(random.randint(0, 200))
            EstoqueVendidos.append(random.randint(0, EstoqueJogos[Tempo]))
            Tempo =+ 1
                
        IngressoVendido = (reduce(operator.add, EstoqueVendidos))
        IngressoDisponivel = (reduce(operator.add, EstoqueJogos))
        IngressoNaoVendido = IngressoDisponivel - IngressoVendido
        Treshold20 = 180
        Jogos90 = len([i for i in EstoqueVendidos if i > Treshold20])
        
        print(f'O numero de tickets totais é de: {IngressoDisponivel},')
        print(f'o numero de tickets que foram vendidos é: {IngressoVendido},')
        print(f'o numero de tickets que não foram vendidos é de: {IngressoNaoVendido},')
        print(f'o numero de jogos com mais de 90% de ingressos vendidos foi de: {Jogos90}.\n')
        
        while True:
            try:
                Jogos = (int(input('Qual jogo você deseja analisar? ')) -1)
                print(f'O jogo {Jogos+1} tem {EstoqueJogos[Jogos]} ingressos totais e {EstoqueVendidos[Jogos]} vendidos.')
                print(f'Este jogo tem atualmente {EstoqueJogos[Jogos] - EstoqueVendidos[Jogos]} ingressos disponíveis\n')
                xr = str(input('Deseja verificar outro jogo?(y/n) '))
                cls()
                if xr == 'y' or xr == 'Y': continue
                else: break
            except ValueError:
                cls()
                print('Utilize apenas números.\n')
            except IndexError:
                cls()
                print('Jogo inválido, tente novamente.\n')
        
    def exercise15():
        Produto1 = []
        Produto2 = []
        Produto3 = []
        MaiorVenda = []
        for i in range(0, 1000):
            Random = random.randint(1,3)
            if Random == 1:
                Produto1.append(round(random.uniform(40, 50), 2))
            elif Random == 2:
                Produto2.append(round(random.uniform(70, 80), 2))
            elif Random == 3:
                Produto3.append(round(random.uniform(100, 135), 2))
                
        Produto1 = tuple(sorted(Produto1, reverse=True))
        Produto2 = tuple(sorted(Produto2, reverse=True))
        Produto3 = tuple(sorted(Produto3, reverse=True))
        totalProduto1 = (reduce(operator.add, Produto1))
        totalProduto2 = (reduce(operator.add, Produto2))
        totalProduto3 = (reduce(operator.add, Produto3))
        MaiorVenda.append(Produto1[0])
        MaiorVenda.append(Produto2[0])
        MaiorVenda.append(Produto3[0])
        MaiorVenda = tuple(sorted(MaiorVenda, reverse=True))

        print('Registro de 1000 vendas da emprea: \n \n')
        print(f'O numero de vendas do Produto 1 foi de: {len(Produto1)}, contabilizados em {format_currency(totalProduto1)}.')
        print(f'Do Produto 2: {len(Produto2)} foram vendidos, gerando {format_currency(totalProduto1)} para a empresa.')
        print(f'E do Produto 3 foram vendidos: {len(Produto3)}, gerando assim: {format_currency(totalProduto3)}. \n')
        print(f'O valor total em vendas da loja foi de: {format_currency(totalProduto1 + totalProduto2 + totalProduto3)}.')
        print(f'A maior venda foi contabilizada em: {format_currency(MaiorVenda[0])}.')

main()