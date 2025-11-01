# Cadastro de clientes
clientes = []

# Cliente 1
nome1 = input("Digite o nome do Cliente 1: ")
idade1 = int(input("Digite a idade do Cliente 1: "))
clientes.append(nome1)

# Cliente 2
nome2 = input("Digite o nome do Cliente 2: ")
idade2 = int(input("Digite a idade do Cliente 2: "))
clientes.append(nome2)

# Cliente 3
nome3 = input("Digite o nome do Cliente 3: ")
idade3 = int(input("Digite a idade do Cliente 3: "))
clientes.append(nome3)

# Tipos de quartos e preços
quartos = ["Simples", "Duplo", "Luxo"]
preco_simples = 100
preco_duplo = 150
preco_luxo = 250

# Reserva do Cliente 1
quarto1 = input(f"{nome1}, escolha seu quarto (Simples/Duplo/Luxo): ").strip().capitalize()
dias1 = int(input(f"{nome1}, quantos dias ficará no hotel? "))

if quarto1 == "Simples":
    total1 = preco_simples * dias1
elif quarto1 == "Duplo":
    total1 = preco_duplo * dias1
elif quarto1 == "Luxo":
    total1 = preco_luxo * dias1
else:
    total1 = 0
    print("Quarto inválido para Cliente 1!")

# Reserva do Cliente 2
quarto2 = input(f"{nome2}, escolha seu quarto (Simples/Duplo/Luxo): ").strip().capitalize()
dias2 = int(input(f"{nome2}, quantos dias ficará no hotel? "))

if quarto2 == "Simples":
    total2 = preco_simples * dias2
elif quarto2 == "Duplo":
    total2 = preco_duplo * dias2
elif quarto2 == "Luxo":
    total2 = preco_luxo * dias2
else:
    total2 = 0
    print("Quarto inválido para Cliente 2!")

# Reserva do Cliente 3
quarto3 = input(f"{nome3}, escolha seu quarto (Simples/Duplo/Luxo): ").strip().capitalize()
dias3 = int(input(f"{nome3}, quantos dias ficará no hotel? "))

if quarto3 == "Simples":
    total3 = preco_simples * dias3
elif quarto3 == "Duplo":
    total3 = preco_duplo * dias3
elif quarto3 == "Luxo":
    total3 = preco_luxo * dias3
else:
    total3 = 0
    print("Quarto inválido para Cliente 3!")

# Exibir valores a pagar
print("\n=== RESUMO DAS RESERVAS ===")
print(f"{nome1}: Quarto {quarto1}, {dias1} dias, Total a pagar: R$ {total1},00")
print(f"{nome2}: Quarto {quarto2}, {dias2} dias, Total a pagar: R$ {total2},00")
print(f"{nome3}: Quarto {quarto3}, {dias3} dias, Total a pagar: R$ {total3},00")