def ficha(nome='esquecido',gol=0):
    print(f'O jogador {nome} fez {gol} gols')

n = str(input('Qual é seu nome? '))
g = str(input('Quantos gols você fez? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)

else:
    ficha(n, g)

