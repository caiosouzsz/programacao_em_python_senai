import random
import time

# =====================================================
# 1 - Número aleatório de 5 a 10
# =====================================================
def numero_aleatorio_5_10():
    return random.randint(5, 10)

# =====================================================
# 2 - Três números aleatórios
# =====================================================
def tres_numeros_aleatorios():
    return [random.randint(1, 100) for _ in range(3)]

# =====================================================
# 3 - Número aleatório entre 10 e 30 usando range()
# =====================================================
def numero_aleatorio_10_30():
    valores = list(range(10, 31))
    return random.choice(valores)

# =====================================================
# 4 - Contagem regressiva simples (for)
# =====================================================
def contagem_regressiva():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(0.3)  # pausa opcional; remova se não quiser
    print("Fogo!")

# =====================================================
# 5 - Soma de números pares até o número inserido
# =====================================================
def soma_pares(numero):
    soma = 0
    for i in range(2, numero + 1, 2):
        soma += i
    return soma

# =====================================================
# 6 - Tabuada de multiplicação
# =====================================================
def tabuada(numero):
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# =====================================================
# 7 - Números ímpares reversos (for)
# =====================================================
def impares_reversos():
    print("\nNúmeros ímpares de 99 a 1:")
    for i in range(99, 0, -2):
        print(i, end=" ")
    print("\nFim!")

# =====================================================
# Função principal
# =====================================================
def main():
    print("1 - Número aleatório de 5 a 10:", numero_aleatorio_5_10())
    print("2 - Três números aleatórios:", tres_numeros_aleatorios())
    print("3 - Número aleatório entre 10 e 30:", numero_aleatorio_10_30())

    print("\n4 - Contagem regressiva:")
    contagem_regressiva()

    print("\n5 - Soma de números pares até o número inserido:")
    while True:
        try:
            n = int(input("Digite um número inteiro positivo: "))
            if n >= 1:
                break
            print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    print(f"A soma dos números pares até {n} é:", soma_pares(n))

    print("\n6 - Tabuada de multiplicação:")
    while True:
        try:
            num_tabuada = int(input("Digite um número para ver a tabuada: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    tabuada(num_tabuada)

    print("\n7 - Números ímpares reversos:")
    impares_reversos()

# =====================================================
# Execução do programa
# =====================================================
if __name__ == "__main__":
    main()