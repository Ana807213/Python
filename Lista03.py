#1.Faça um programa para verificar se um numero é triangular. Um numero é triangular se for o produto de tres numeros inteiros consecutivos.

numero = int (input ("Digite um numero:"))
i = 1
while i * (i+1) * (i+2) < numero:
    i = i+1
if i * (i + 1) * (i + 2) == numero:
    print ("O numero é triangular")
else:
    print ("O numero nao é triangular")

# 2. Faça um programa que leia n valores fornecidos pelo usuario e calcule a soma de seus quadrados 
n = int (input ("Digite a quantidade de valores:"))
soma = 0
for i in range (n):
    valor = float (input ("Digite um valor:"))
    soma = soma + valor ** 2
    print ("A soma dos quadrados é:", soma)

#3. Calcule o quociente e o resto da divisao de A por B, utilizando apenas soma e subtração
a = int (input ("Digite o dividendo:"))
b = int (input ("Digite o divisor:"))
quociente = 0
while a > b:
    a = a - b 
    quociente = quociente + 1
    print ("O quociente é:", quociente)
    print ("O resto é:", a)

#4.Faça um programa que calcule a quantidade de dias corridos entre duas datas 
dial = int (input ("Digite o dia da data: "))
mesl = int (input ("Digite o mes da data:"))
anol = int (input ("Digite o ano da data:"))
dia2 = int (input ("Digite o dia da data:"))
mes2 = int (input ("Digite o mes da data:"))
ano2 = int (input ("Digite o ano da data:"))
dias = 0
for i in range (anol, ano2):
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        dias = dias + 366
    else:
        dias = dias + 365
for i in range (1, mesl):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        dias = dias + 31
    elif i == 4 or i == 6 or i == 9 or i == 11:
        dias = dias + 30
    else:
        if anol % 4 == 0 and (anol % 100 != 0 or anol % 400 == 0):
            dias = dias + 29
        else:
            dias = dias + 28
            dias = dias + dial
for i in range (1, mes2):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        dias = dias + 31
    elif i == 4 or i == 6 or i == 9 or i == 11:
        dias = dias + 30
    else:
        if ano2 % 4 == 0 and (ano2 % 100 != 0 or ano2 % 400 == 0):
            dias = dias + 29
        else:
            dias = dias + 28
            dias = dias + dia2
print ("A quantidade de dias corridos é:", dias)

#5. Faça um programa que contenha um menu para 4 operaçoes basicas ( soma, subtração, Produto e divisao) mais a opção Sair.
# O programa deve simular uma calculadora e resolver a operação entre os 2 operandos.
opcao = 0
while opcao != 5:
    print ("1 - Soma")
    print ("2 - Subtração")
    print ("3 - Produto")
    print ("4 - Divisão")
    print ("5 - Sair")
    opcao = int (input ("Digite a opção desejada:"))
    if opcao != 5:
        operando1 = float (input ("Digite o primeiro operando:"))
        operando2 = float (input ("Digite o segundo operando:"))
        if opcao == 1:
            resultado = operando1 + operando2
        elif opcao == 2:
            resultado = operando1 - operando2
        elif opcao == 3:
            resultado = operando1 * operando2
        elif opcao == 4:
            resultado = operando1 / operando2
        print ("O resultado é:", resultado)
print ("Fim do programa")

