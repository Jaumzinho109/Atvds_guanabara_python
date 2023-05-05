from random import randint
numeros = list()
def sorteia(lst):
    for c in range (0,5,1):
        num = randint(1, 10)
        lst.append(num)
    print(lst)
def somapar(lst):
    soma = 0
    for k, v in enumerate(lst):
        if v % 2 == 0:
            soma += v
    print(soma)

sorteia(numeros)
somapar(numeros)