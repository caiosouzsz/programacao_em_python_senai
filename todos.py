import random

def jogo_ppt():
    ppt_maquina = ['🧻','🪨','✂️']
    ppt_jogador = ['🧻','🪨','✂️']

    aleatorio = random.choice(ppt_maquina)
    escolha = int(input('''
0 - 🧻 (Papel)
1 - 🪨 (Pedra)
2 - ✂️ (Tesoura)

Escolha: '''))

    print(f'Você escolheu: {ppt_jogador[escolha]}')
    print(f'A máquina escolheu: {aleatorio}')

    if aleatorio == ppt_jogador[escolha]:
        print('EMPATE!')
    elif (aleatorio == '🧻' and ppt_jogador[escolha] == '✂️') or \
         (aleatorio == '🪨' and ppt_jogador[escolha] == '🧻') or \
         (aleatorio == '✂️' and ppt_jogador[escolha] == '🪨'):
        print('VOCÊ GANHOU! 🎉')
    else:
        print('A MÁQUINA GANHOU! 😢')

def jogo_perguntas():
    perguntas = [
        'O que é o que é? Quanto mais se tira, maior fica?',
        'Por que o livro foi ao médico?',
        'O que é o que é que tem dentes, mas não morde?',
        'Por que o computador foi preso?',
        'O que é o que é que cai em pé e corre deitado?',
        'O que é um pontinho vermelho no jardim?',
        'O que o tomate foi fazer no banco?',
        'O que é o que é que tem asa, mas não voa, e canta sem ter boca?',
        'Por que o lápis se deu mal na prova?',
        'O que é o que é que quanto mais quente fica, mais frio deixa o ambiente?',
    ]

    respostas = [
        'Um buraco!',
        'Histórias pra contar!',
        'O pente!',
        'Porque ele executou um programa!',
        'A chuva!',
        'Uma formiga com batom!',
        'Tirar extrato!',
        'O ventilador!',
        'Porque estava sem ponta!',
        'O ar-condicionado!'
    ]

    indice = random.randrange(len(perguntas))
    print(perguntas[indice])
    escolha = int(input(f'''
0 - {respostas[0]}
1 - {respostas[1]}
2 - {respostas[2]}
3 - {respostas[3]}
4 - {respostas[4]}
5 - {respostas[5]}
6 - {respostas[6]}
7 - {respostas[7]}
8 - {respostas[8]}
9 - {respostas[9]}

Escolha a resposta correta: '''))

    if indice == escolha:
        print('Acertou em cheio! 🥳')
    else:
        print(f'ERROU! 😵 A resposta certa era: {respostas[indice]}')

def jogo_adivinhacao():
    numero = random.randint(1, 10)
    escolha = int(input('Escolha um número de 1 a 10: '))
    print(f'O número aleatório era: {numero}')
    if escolha == numero:
        print('Você ganhou o jogo! 🎉')
    else:
        print('Errou feio! ☠️')

def menu():
    while True:
        print('''
=== SISTEMA DE JOGOS ===
1 - Pedra, Papel e Tesoura
2 - Perguntas e Respostas
3 - Adivinhação de Números
0 - Sair
''')
        opcao = input('Escolha um jogo: ').strip()

        if opcao == '1':
            jogo_ppt()
        elif opcao == '2':
            jogo_perguntas()
        elif opcao == '3':
            jogo_adivinhacao()
        elif opcao == '0':
            print('Saindo do sistema de jogos...')
            break
        else:
            print('Opção inválida! Digite 0, 1, 2 ou 3.')

# Executa o menu
menu()