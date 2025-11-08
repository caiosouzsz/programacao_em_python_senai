# 1) Função para comparar dois números (par ou ímpar)
def compara_par_impar(num1, num2):
    def tipo(n):
        return "par" if n % 2 == 0 else "ímpar"

    print(f"{num1} é {tipo(num1)}")
    print(f"{num2} é {tipo(num2)}")


# 2) Função para multiplicar 3 números
def multiplicar3(a, b, c):
    return a * b * c


# 3) Função para descobrir valor elevado
def elevado(numero, expoente):
    return numero ** expoente


# 4) Mensagem personalizada para 18 anos
def verifica_idade(idade):
    if idade == 18:
        print("Você tem 18 anos! Seja bem-vindo!")
    else:
        print("Você NÃO tem 18 anos.")


# 5) Função para descobrir idade
def calcula_idade(ano_nasc, ano_atual):
    return ano_atual - ano_nasc


# 6) Função para ver se Brasil ganhou Copa de 1999
def brasil_ganhou_1999():
    return False


# 7.1) Função - Cumprimentar
def cumprimenta():
    print("\nOlá! Bem-vindo ao restaurante!")


# 7.2) Função - Restaurante
def restaurante():
    cardapio = ["Salada", "Macarronada", "Sanduíche", "Sorvete"]

    print("\nMENU:")
    for i, comida in enumerate(cardapio, start=1):
        print(f"{i} - {comida}")

    opcao = int(input("\nEscolha uma opção: "))

    if 1 <= opcao <= len(cardapio):
        print(f"Você escolheu: {cardapio[opcao - 1]}")
    else:
        print("Opção inválida!")


# MENU PRINCIPAL
def main():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Comparar par/ímpar")
        print("2 - Multiplicar 3 números")
        print("3 - Elevar número")
        print("4 - Verificar idade = 18")
        print("5 - Descobrir idade")
        print("6 - Brasil ganhou a copa de 1999?")
        print("7 - Restaurante")
        print("0 - Sair")

        op = int(input("Escolha uma opção: "))

        if op == 1:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            compara_par_impar(n1, n2)

        elif op == 2:
            a = int(input("Digite A: "))
            b = int(input("Digite B: "))
            c = int(input("Digite C: "))
            print("Resultado =", multiplicar3(a, b, c))

        elif op == 3:
            num = int(input("Digite o número: "))
            exp = int(input("Digite o expoente: "))
            print("Resultado =", elevado(num, exp))

        elif op == 4:
            idade = int(input("Digite sua idade: "))
            verifica_idade(idade)

        elif op == 5:
            nasc = int(input("Ano de nascimento: "))
            atual = int(input("Ano atual: "))
            print("Sua idade é:", calcula_idade(nasc, atual))

        elif op == 6:
            if brasil_ganhou_1999():
                print("Sim!")
            else:
                print("Não! Brasil NÃO ganhou em 1999!")

        elif op == 7:
            cumprimenta()
            restaurante()

        elif op == 0:
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


# Programa inicia aqui
main()