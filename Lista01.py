#1.Faça um programa que transforme uma temperatura em Celsius para Farenheit 
celsius = float(input("Digite a temperatura em Celsius: "))
farenheit = (celsius * 9/5) + 32
print("A temperatura em Farenheit é: ", farenheit)

#2.Faça um programa que leia 3 valores e mostre a soma dos seus inversos 
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input ("Digite o segundo valor:"))
n3 = float (input("Digite o terceiro valor: "))
soma = 1/n1 + 1/n2 + 1/n3
print("A soma dos inversos é:", soma)

#3.Faça um programa que leia o nome de um produto, a quantidade comprada, o valor unitario e o percentual de desconto a ser aplicado
#para o pagamento. Mostre o nome do produto e o valor total da venda 
nome = input("Digite o nome do produto:")
quantidade = float(input("Digite a quantidade comprada:"))
valor_unitario = float(input("Digite o valor unitario:"))
desconto = float(input("Digite o percentual de desconto:"))
valor_total = quantidade * valor_unitario * (1 - desconto / 100)
print("O nome do produto é:", nome)
print("O valor total da venda é:", valor_total)


#4.Faça um programa que converta reais em dolares. O usuario deve informar o valor em reais e o valor cotação
reais = float (input ("Digite o valor em reais:"))
cotacao = float (input ("Digite a cotação do dolar:"))
dolares = reais / cotacao
print ("O valor em dolares é:", dolares)

#5.Faça a conversao de um tempo expresso em horas, minutos e segundos para somente em segundos 
horas = int (input("Digite as horas:"))
minutos = int (input ("Digite os minutos:"))
segundos = int (input ("Digite os segundos:"))
tempo = horas * 3600 + minutos * 60 + segundos
print ("O tempo em segundos é:", tempo)



