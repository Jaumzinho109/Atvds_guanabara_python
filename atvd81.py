lista = []
while True:
    valor = int(input('Informe um valor inteiro: '))
    lista.append(valor)
    resp = str(input('Você quer continuar? S/N ')).upper()
    if resp == 'N':
        break
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista')
print('Foram digitador {} números'.format(len(lista)))
lista.sort(reverse=True)
print(lista)
