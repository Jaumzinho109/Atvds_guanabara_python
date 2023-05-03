dlista = list()
tlista = list()
leves = list()
pesados = list()

for c in range(0,4):
    nome = str(input('Escreva o seu nome: '))
    dlista.append(nome)
    peso = float(input('Informe o seu peso em kg: '))
    dlista.append(peso)
    tlista.append(dlista[:])
    if peso <= 70:
        leves.append(nome)
    elif peso >= 100:
        pesados.append(nome)
    dlista.clear()

print('Ao todo, você cadastrou {} pessoas'.format(len(tlista)))
print('Sendo que os maiores pesos são dos seguintes nomes: {}'.format(pesados))
print('E os mais leves são: {}'.format(leves))