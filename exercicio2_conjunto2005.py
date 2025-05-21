#Faça um programa que receba vários números do usuários (menores que 30) e determine quais números são primos.

def eh_primo(n): # def define uma função. Indica o inicio de um bloco de codifo que pode ser usado em outras partes do programa 
    # Função que verifica se um número é primo
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numeros = []
while True:
    try:
        # Solicita ao usuário um número menor que 30
        valor = int(input("Digite um número menor que 30 (ou um número negativo para sair): "))
        if valor < 0:
            # Sai do loop se o número for negativo
            break
        if valor >= 30:
            # Garante que o número seja menor que 30
            print("Por favor, digite apenas números menores que 30.")
            continue
        numeros.append(valor)
    except ValueError:
        # Trata entradas inválidas
        print("Digite um número válido.")

# Cria uma lista apenas com os números primos digitados
primos = [num for num in numeros if eh_primo(num)]

# Exibe os números primos encontrados
print("Números primos digitados:", primos)