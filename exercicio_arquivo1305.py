# Faça um programa que receba o nome de N pessoas e armazene no arquivo nome.txt.
# Que receba o sobrenome das mesmas N pessoas e armazene no arquivo sobrenome.txt. E
# que ao final crie um terceiro arquivo com o nome completo das mesmas N pessoas.

def main():
    try:
        # Lê o número de pessoas com validação
        while True:
            try:
                n = int(input("Digite o número de pessoas: "))
                if n > 0:
                    break
                else:
                    print("Por favor, insira um número positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")

        # Abre o arquivo nome.txt para escrita
        with open('nome.txt', 'w') as nome_file:
            # Lê os nomes e escreve no arquivo
            for i in range(n):
                nome = input(f"Digite o nome da pessoa {i + 1}: ").strip()
                nome_file.write(nome + '\n')

        # Abre o arquivo sobrenome.txt para escrita
        with open('sobrenome.txt', 'w') as sobrenome_file:
            # Lê os sobrenomes e escreve no arquivo
            for i in range(n):
                sobrenome = input(f"Digite o sobrenome da pessoa {i + 1}: ").strip()
                sobrenome_file.write(sobrenome + '\n')

        # Cria um terceiro arquivo com os nomes completos
        with open('nomes_completos.txt', 'w') as completos_file:
            with open('nome.txt', 'r') as nome_file, open('sobrenome.txt', 'r') as sobrenome_file:
                for nome, sobrenome in zip(nome_file, sobrenome_file):
                    completos_file.write(nome.strip() + ' ' + sobrenome.strip() + '\n')

        print("Arquivos criados com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()