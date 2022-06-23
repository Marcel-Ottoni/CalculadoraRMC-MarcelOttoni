import math
import cmath
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from sympy.plotting import *

def escolher_funcao_2grau(pergunta):
    while pergunta == 1:
        print("Você selecionou a Funcao do segundo grau")
        print("O que voce quer calcular?\n"
              "1 - Calcular raizes\n"
              "2 - Calcular função em x pedido\n"
              "3 - Calcular o vertice\n"
              "4 - Gerar gráfico\n"
              "5 - Voltar ao menu principal")
        escolha = int(input('Digite aqui: '))
        if escolha == 5:
            break
        elif escolha > 5 or escolha < 1:
            print('Voce colocou um numero invalido!')
            continue
        escolha_a = int(input("Insira o valor desejado para A: "))
        escolha_b = int(input("Insira o valor desejado para B: "))
        escolha_c = int(input("Insira o valor desejado para C: "))
        if escolha == 1:
            calcular_raizes(escolha_a, escolha_b, escolha_c)
        elif escolha == 2:
            calcular_funcao_x(escolha_a, escolha_b, escolha_c)
        elif escolha == 3:
            calcular_vertice(escolha_a, escolha_b, escolha_c)
        elif escolha == 4:
            gerar_grafico(escolha_b,escolha_c)


def calcular_raizes(escolha_a, escolha_b, escolha_c):
    delta = escolha_b * escolha_b - 4 * escolha_a * escolha_c
    if delta > 0:
        raiz = math.sqrt(delta)
        valor_x1 = (-escolha_b - raiz) / (2 * escolha_a)
        valor_x2 = (-escolha_b + raiz) / (2 * escolha_a)
        print("Valor de x1: ",valor_x1)
        print("Valor de x2: ",valor_x2)
    elif delta < 0:
        raiz = cmath.sqrt(delta)
        valor_x1 = (-escolha_b - raiz) / (2 * escolha_a)
        valor_x2 = (-escolha_b + raiz) / (2 * escolha_a)
        print('valor de x1: ', valor_x1)
        print('valor de x2: ', valor_x2)


def calcular_funcao_x(escolha_a, escolha_b, escolha_c):
    escolha_x = int(input('Digite o valor de X: '))
    valor_FX = (escolha_a * escolha_x ** 2) + (escolha_b * escolha_x) + escolha_c
    print('O valor de f(x) é: ', valor_FX)


def calcular_vertice(escolha_a, escolha_b, escolha_c):
    delta = escolha_b * escolha_b - 4 * escolha_a * escolha_c
    vertice_x = -(escolha_b) / (2 * escolha_a)
    vertice_y = -(delta) / (4 * escolha_a)
    print(delta)
    print('O vertice de x eh: ', vertice_x)
    print('O vertice de y eh: ', vertice_y)


def gerar_grafico(escolha_b, escolha_c):
    x = Symbol('x')
    y = x**2 - escolha_b*x + escolha_c
    y1 = diff(y, x)
    x_vertice = solve(y1, x)
    y_vertice = y.subs(x, escolha_b/2)
    print("O ponto do vertice eh: ", (x_vertice[0], y_vertice))
    plot(y, xlim=[0, 10], ylim=[-5, 5])

#Função exponencial
def escolher_exponencial(pergunta):
    while pergunta == 2:
        print("Voce selecionou Funcao exponencial")
        print("O que voce quer calcular?\n"
              "1 - Verificar se é crescente ou decrescente\n"
              "2 - Calcular função em X pedido\n"
              "3 - Gerar grafico\n"
              "4 - Voltar para menu principal")
        escolha = int(input("Digite aqui: "))
        if escolha == 4:
            break
        elif escolha > 4 or escolha < 1:
            print("Voce colocou um numero invalido!")
            continue
        escolha_a = float(input("Insira o valor desejado para A: "))
        escolha_b = float(input("Insira o valor desejado para B: "))
        if escolha == 1:
            verificar_crescente_decrescente(escolha_a)
        elif escolha == 2:
            calcular_xpedido(escolha_a, escolha_b)
        elif escolha == 3:
            gerar_grafico_exp(escolha_a)
def verificar_crescente_decrescente(escolha_a):
    if 0 < escolha_a < 1:
        print("O seu gráfico eh decrescente, pois o A eh menor que 1 e maior que 0!")
    elif escolha_a > 1:
        print("O seu gráfico eh crescente, pois o A eh maior que 1!")
    else:
        print("A sua reta eh horizontal ")
def calcular_xpedido(escolha_a,escolha_b):
    escolha_x = int(input("Digite o valor de X: "))
    valor_FX = escolha_a * (escolha_b ** escolha_x)
    print("O valor de f(x) eh: ",valor_FX)
def gerar_grafico_exp(escolha_a):
    def funcao_exponencial(escolha_a,x):
        return(escolha_a**x)
    vetorX = np.arange(-7, 7, 0.1)
    vetorY = []
    for x in vetorX:
        vetorY.append(funcao_exponencial(escolha_a, x))

    fig = plt.figure(figsize=(5, 5))

    plt.plot(vetorX, vetorY, label = 'Funcao Exponencial', color = 'g')
    plt.title("f(x) = a^x")
    plt.xlabel("eixo x")
    plt.ylabel("eixo y")
    plt.legend()
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
    fig.savefig("FExp.png")
    print(funcao_exponencial(escolha_a, x))
def escolher_matriz(pergunta):
    while pergunta == 3:
        print("Voce selecionou Matriz")
        print("O que voce quer calcular?\n"
              "1 - Determinante da matriz\n"
              "2 - Multiplicar matriz\n"
              "3 - Matriz transposta\n"
              "4 - Voltar pro menu principal")
        escolha = int(input('Digite aqui: '))
        if escolha == 4:
            break
        elif escolha > 4 or escolha < 1:
            print("Voce colocou um numero invalido!")
        nlinhas = int(input("Digite a quantidade de linhas: "))
        ncolunas = int(input("Digite a quantidade de colunas: "))
        matriz = [0] * nlinhas
        for linha in range(nlinhas):
            matriz[linha] = [0] * ncolunas
        for linha in range(nlinhas):
            for coluna in range(ncolunas):
                matriz[linha][coluna] = int(input(("Digite os elementos da matriz: ")))
        for i in matriz:
            print(i)
        if nlinhas < 1 or ncolunas < 1:
            print("A sua quantidade de linhas ou colunas estao menores do que 1! coloque novamente")
            continue
        if escolha == 1:
            calcular_determinante(matriz,nlinhas,ncolunas)
        elif escolha == 2:
            multiplicar_matrizes(matriz,nlinhas,ncolunas)
        elif escolha == 3:
            fazer_matriz_transposta(matriz,nlinhas,ncolunas)

def calcular_determinante(matriz,nlinhas,ncolunas):
                print("Voce escolheu calcular a determinante da matriz!")
                if nlinhas != ncolunas:
                    print("Sua matriz nao eh quadrada!")
                elif nlinhas == 3 and ncolunas == 3:
                    diagonal1 = matriz[0][0] * matriz[1][1] * matriz[2][2] + \
                                matriz[0][1] * matriz[1][2] * matriz[2][0] + \
                                matriz[0][2] * matriz[1][0] * matriz[2][1]
                    diagonal2 = matriz[2][0] * matriz[1][1] * matriz[0][2] + \
                                matriz[2][1] * matriz[1][2] * matriz[0][0] + \
                                matriz[2][2] * matriz[1][0] * matriz[0][1]
                    print("Soma Diagonal Principal = ", diagonal1)
                    print("Soma Diagonal Secundaria", diagonal2)
                    total = diagonal1 - diagonal2
                    print("\nDeterminante da matriz = ",total)
                elif nlinhas == 2 and ncolunas == 2:
                    diagonal1 = matriz[0][0] * matriz[1][1]
                    diagonal2 = matriz[0][1] * matriz[1][0]
                    print("Soma Diagonal Principal = ",diagonal1)
                    print("Soma Diagonal Secundaria = ",diagonal2)
                    total = diagonal1 - diagonal2
                    print("\nDeterminante da matriz = ",total)
                else:
                    print("Sua matriz nao eh 2x2 ou 3x3")

def multiplicar_matrizes(matriz,nlinhas,ncolunas):
            print("Voce escolheu multiplicar 2 matrizes!")
            nlinhas2 = int(input("Digite a quantidade de linhas da segunda matriz: "))
            ncolunas2 = int(input("Digite a quantidade de colunas da segunda matriz: "))
            matriz2 = [0] * nlinhas2
            matriz3 = [0] * nlinhas
            for linha in range(nlinhas):
                matriz3[linha] = [0] * ncolunas2

            for linha in range(nlinhas2):
                matriz2[linha] = [0] * ncolunas2
            if ncolunas != nlinhas2:
                print("Nao eh possivel realizar a multiplicacao, pois o numero de colunas da matriz 1 esta diferente do numero de linhas da matriz \n")
            for linha in range(nlinhas2):
                for coluna in range(ncolunas2):
                    matriz2[linha][coluna] = int(input(("Digite os elementos da segunda matriz: ")))

            for cont in range(nlinhas):
                for cont2 in range(ncolunas2):
                    acumula = 0
                    for i in range(ncolunas):
                        acumula += matriz[cont][i] * matriz2[i][cont2]
                        matriz3[cont][cont2] = acumula
            print("{0} X {1} = {2}".format(matriz,matriz2,matriz3))
def fazer_matriz_transposta(matriz,nlinhas,ncolunas):
    transposta = []
    for linha in range(ncolunas):
        linhaT = []
        for coluna in range(nlinhas):
            linhaT.append(0)
        transposta.append(linhaT)
    for linha in range(nlinhas):
        for coluna in range(ncolunas):
            transposta[coluna][linha] = matriz[linha][coluna]
    print("Matriz transposta {}x{}".format(ncolunas, nlinhas))
    for i in transposta:
        print(i)

while True:

    print("Selecione a calculadora desejada: \n"
          "1 - Função do segundo grau\n" 
           "2- Função exponencial \n"
          "3 - Matriz \n"
          "4 - Sair")
    pergunta = int(input("Digite aqui: "))
    if pergunta == 1:
        escolher_funcao_2grau(pergunta)
    elif pergunta == 2:
        escolher_exponencial(pergunta)
    elif pergunta == 3:
        escolher_matriz(pergunta)
    elif pergunta == 4:
        break
    else:
        print("Voce colocou um numero invalido")