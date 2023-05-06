def LeiaInt(num):
    ver = False
    v = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            v = int(n)
            ver = True
        else:
            print(f'Digite um número inteiro')
        if ver:
            break
    return v
n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

