dados = {}
gol = []
total = 0

nome = str(input('Escreva o nome do jogador: '))
dados['Nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou?'))

for c in range (0, partidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    total += gols
    gol.append(gols)

dados['Gols'] = gol
dados['Total'] = total

print('-=' * 30)
print(dados)
print('-=' * 30)

for i, v in dados.items():
    print(f'O campo {i} tem valor {v}')
print('-=' * 30)

print(f'O jogador {dados["Nome"]} jogou {partidas} partidas')
for k, v in enumerate (dados['Gols']):
    print(f'Na partida {k} fez {v} gols')
print(f'Um total de {dados["Total"]} gols')
print('-=' * 30)