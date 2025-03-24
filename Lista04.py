# 1. Faça um programa que receba um vetor com 20 posições e rotacione esse vetor para a direira (novo vetor) e para a esquerda (novo vetor)

vetor = []
for i in range (20):
    vetor.append (int (input ("Digite um valor:")))
    n = int (input ("Digite o numero de posições a serem rotacionadas:"))
    novo = []
    for i in range (20):
        novo.append (0)
        for i in range (20):
            novo [(i + n) % 20] = vetor [i]
            print ("Vetor rotacionado para a direita:", novo)
            novo = []
            for i in range (20):
                novo.append (0)
                for i in range (20):
                    novo [(i - n) % 20] = vetor [i]
                    print ("Vetor rotacionado para a esquerda:", novo)

# 2. Faça um programa que sorteie 10 numero aleatorios e mostre a quantidade de numeros maiores que a media e menores que a media 
import random
vetor = []
for i in range (10):
    vetor.append (random.randint (1, 100))
    soma = 0
    for i in range (10):
        soma = soma + vetor [i]
        media = soma / 10
        maior = 0
        menor = 0
        for i in range (10):
            if vetor [i] > media:
                maior = maior + 1
            else:
                menor = menor + 1
                print ("Quantidade de numeros maiores que a media:", maior)
                print ("Quantidade de numeros menores que a media:", menor)

# 3. Faça um programa que inverta uma lista com 5 posições em utlizar variaveis auxialiares (utiliza apenas a propria lista)
lista = []
for i in range (5):
    lista.append (int (input ("Digite um valor:")))
    for i in range (3):
        lista [i], lista [4 - i] = lista [4 - i], lista [i]
        print ("Lista invertida:", lista)
