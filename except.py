try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {numero}.")
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
except ValueError:
    print("Erro: Você deve digitar apenas números.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

    
lista = [10, 20, 30, 40, 50]

try:
    indice = int(input("Digite o índice que deseja acessar (0 a 4): "))
    print(f"O valor no índice {indice} é {lista[indice]}.")
except ValueError:
    print("Erro: Digite um número inteiro válido para o índice.")
except IndexError:
    print("Erro: Índice fora do intervalo da lista.")