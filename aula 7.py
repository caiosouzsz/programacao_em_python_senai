# ## EXERCÍCIOS:

#**Exercício 0:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

#**Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.

#**Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.

#**Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.

#**Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.

#**Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.

i = list(range(0, 22, 2))
carros = [input('digite um nome de carro: '), input('agora outro: '), input('agora outro: ')]
numeros = [1,2,3,4,5,6,7,8,9,10]

print(i)

print(numeros)

print(numeros[3])

numeros.append(9)
print(numeros)

del(numeros[4])
print(numeros)

print(numeros + carros)