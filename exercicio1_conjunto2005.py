#Faça um programa que conte a quantidade de valores diferentes em um vetor com 10 posições.#

# Solicita ao usuário que digite 10 números e armazena em uma lista
vetor = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

# Usa um conjunto (set) para encontrar os valores diferentes
valores_diferentes = set(vetor)

# Exibe a quantidade de valores diferentes
print(f"Quantidade de valores diferentes: {len(valores_diferentes)}")







