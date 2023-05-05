def contador1():
    c = 1
    while True:
        print(c, '...', end=' ')
        c += 1
        if c == 11:
            break
def contador2():
    c = 10
    while True:
        print(c, '...', end='')
        c -= 2
        if c < 0:
            break
def contador3():
    inc = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if fim > 0:
        for c in range(inc, fim + 1, passo):
            print(c, end='... ')
    else:
        for c in range(inc, fim - 1, passo):
            print(c, end='... ')



contador1()
print()
contador2()
print()
contador3()
