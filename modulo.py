# arquivo modulo.py
import statistics

def imc(peso, altura):
    return peso/altura**2


def calcular_soma(x,y):
    return x + y


def verificar_idade(idade):
    if idade >= 18:
        return 'maior de idade'
    else:
        return 'Menor de idade'