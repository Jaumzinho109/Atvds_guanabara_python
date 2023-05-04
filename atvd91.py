from random import randint
from operator import itemgetter
dados = {}
ranking = {}

for c in range (0,4):
    nome = str(input('Digite o seu nome: '))
    dados[nome] = randint(1, 6)
    print(f'O jogador {nome} teve o resultado {dados[nome]}')

ranking = sorted(dados.items(), key= itemgetter(1), reverse= True)
for i, v in enumerate(ranking):
    print(f'Em {i+1} lugar: {v[0]} com {v[1]}')