from random import randint

lista_dos_palpites = list()
lista = list()

c = int(input('Quantos jogos serão gerados? '))
while c > 0:
    lista = [randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60)]
    lista_dos_palpites.append(lista[:])
    lista.clear()
    c -= 1

for i, l in enumerate(lista_dos_palpites):
    print(f'Jogo {i+1}: {l}')