lista = []
resp = ''
while True:
    valor = int(input('Digite os números do seu cadastro: '))
    if valor not in lista: 
        lista.append(valor)
    resp = str(input('Você quer continuar? [S/N]')).upper()
    if resp == 'N':
        break
print(sorted(lista))