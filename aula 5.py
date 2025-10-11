boas_vindas = 'Seja bem vindo'
print("seja bem vindo")
tipo = True
multi = float
divi = float
sub = float

print(f'''

1 = valor da variáver "tipo"
2 = múltiplicação de 2 números decimais
3 = múltiplicação com 4 números
4 = divisão de números decimais
5 = divisão com 2 números inteiros
6 = dobro de um número inteiro
7 = fazer registro
''')
decisao = int(input(f'''digite números de 1 a 7 para fazer sua escolha!
'''))

if decisao == 1:
    print(type(tipo))

if decisao == 2:
        n1 = float(input('digite um número: '))
        n2 = float(input('digite outro número: '))
        multi = n1 * n2
        print('o resultado da sua multiplicação é:', multi)

if decisao == 3:
    n1 = float(input('digite um número: '))
    n2 = float(input('digite outro número: '))
    n3 = float(input('digite outro número: '))
    n4 = float(input('digite outro número: '))
    multi = n1 * n2 * n3 * n4
    print('o resultado da sua multiplicação é:', multi)

if decisao == 4:
    n1 = float(input('digite um número: '))
    n2 = float(input('digite outro número: '))
    divi = n1 / n2
    print('o resultado da sua divisão é:', divi)

if decisao == 5:
    n1 = float(input('digite um número: '))
    n2 = float(input('digite outro número: '))
    divi = n1 // n552
    print('o resultado da sua divisão é:', divi)

if decisao == 6:
    n1 = float(input('digite um número: '))
    print('o seu resultado é: ', n1 * 2)

if decisao == 7:
    nome = input('digite seu nome:')
    idade = input('digite sua idade: ')
    endereco = input('digite seu endereço: ')
    print('resgistrado com sucesso!')

    print(f'''
    o seu nome é: {nome}
    a sua idade é: {idade}
    o seu endereço é: {endereco}
    ''')

exit(f'''
OBRIGADO POR USAR!!!

criado por Caio de Souza
''')
    







