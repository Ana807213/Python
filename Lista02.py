#1.Faça um programa que calcule IMC de uma pessoa e informe a classificação segundo os intervalos:
# Abaixo do peso : abaixo de 18.5
# Peso normal : 18.5 e 25
# Acima do peso : entre 25 e 30
# Obeso : acima de 30
peso = float (input("Digite o peso:"))
altura = float (input ("Digite a altura:"))
imc = peso / (altura ** 2)
if imc < 18.5:
    print ("Abaixo do peso")
elif imc <25:
    print ("Peso normal")
elif imc <30:
    print ("Acima do peso")
else : 
    print ("Obeso")

#2. Faça um programa que leia 3 lados de um triangulo e verifique se os 3 lados formam ou nao um triangulo.

lado1 = float (input ("Digite o primeiro lado:"))
lado2 = float (input ("Digite o segundo lado:"))
lado3 = float (input ("Digite o terceiro lado:"))
if lado1 < lado2 + lado3 and lado2< lado1 + lado3 and lado3 < lado1 + lado2:
    print (" É um triangulo")
else:
        print ("Nao é um triangulo")

#3. Faça um programa que receba as coordenadas de um ponto e retorne qual quadrante esse ponto esta localizado
x = float (input ("Digite a coordenada x do ponto:"))
y = float (input ("Digite a coordenada y do ponto:"))
if x > 0 and y > 0:
     print ("Primeiro quadrante")
elif x < 0 and y >0:
     print ("Segundo quadrante")
elif x < 0 and y <0 :
     print ("Terceiro quadrante")
else:
     print ("Quarto quadrante")

#4. Faça um programa que receba a data de nascimento de uma pessoa e fale qual o signo dessa pessoa 
dia = int (input ("Digite o dia do nascimento:"))
mes = int (input ("Digite o mes do nascimento:"))
if (dia >= 21 and mes == 3) or (dia <= 20 and mes ==4):
    print ("Aries")
elif (dia >= 21 and mes == 4) or (dia <= 20 and mes ==5):
    print ("Touro")
elif (dia >= 21 and mes == 5) or (dia <= 20 and mes ==6):
    print ("Gemeos")
elif (dia >= 21 and mes == 6) or (dia <= 20 and mes ==7):                   
    print ("Cancer")
elif (dia >= 21 and mes == 7) or (dia <= 20 and mes ==8):
    print ("Leao")
elif (dia >= 21 and mes == 8) or (dia <= 20 and mes ==9):  
    print ("Virgem")
elif (dia >= 21 and mes == 9) or (dia <= 20 and mes ==10):
    print ("Libra")
elif (dia >= 21 and mes == 10) or (dia <= 20 and mes ==11):
    print ("Escorpiao")
elif (dia >= 21 and mes == 11) or (dia <= 20 and mes ==12):
    print ("Sagitario")
elif (dia >= 21 and mes == 12) or (dia <= 20 and mes ==1):
    print ("Capricornio")
elif (dia >= 21 and mes == 1) or (dia <= 20 and mes ==2):
    print ("Aquario")
else:
    print ("Peixes")   


#5. Faça um programa que receba um numero o salario de um vendedor e total de vendas de um mes.
# Acrescentar ao salario um premrio de acordo com os intervalos a seguir.
# Mostrar o salario do vendedor com a premiação.
# Vendas de 1000 a 5000: Premiação de 500,00
# Vendas de 5000 a 7500: Premiação de 750,00
# Vendas maiores que  7500 : Premiação de 1.000,00
numero = int (input ("Digite o numero do venededor:"))
salario = float (input ("Digite o salario do vendendor:"))
vendas = float (input ("Digite o total de vendas:"))
if vendas < 5000:
    salario = salario + 500
elif vendas < 7500:
    salario = salario + 750
else:
    salario = salario + 1000
    print ("O salaario do vendedor é:", salario)

