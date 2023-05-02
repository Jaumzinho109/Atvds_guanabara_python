lista = []
lista_imp = []
lista_par = []
while True:
    n = int(input('Digite um valor inteiro: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_imp.append(n)
    resp = str(input('Você quer continuar? S/N ')).lower()
    if resp == 'n':
        break
print('A lista completa é a seguinte: {}'.format(lista))
print('Essa é a lista dos pares: {}'.format(lista_par))
print('E essa a dos ímpares: {}'.format(lista_imp))