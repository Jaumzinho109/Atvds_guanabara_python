dados = dict()
total = 0
gol = []
lista = list()
pts = dict()
ptd = list()

while True:
    nome = str(input('Escreva o nome do jogador: '))
    dados['Nome'] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou?'))
    gol = []
    total = 0
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c + 1}? '))
        total += gols
        gol.append(gols)
    dados['Gols'] = gol
    dados['Total'] = total
    lista.append(dados.copy())
    dados.clear()
    while True:
        resp = str(input('Você quer continuar? [S/N]')).upper()
        if resp == 'N':
            print('-=' * 40)
            print('cod nome', ' ' * 6, 'gols', ' '* 6, 'total')
            print('_' * 40)
            for i, v in enumerate(lista):
                print(f'{i}  {v["Nome"]:<3}        {v["Gols"]}          {v["Total"]}')
            print('_' * 40)
            while True:
                esc = int(input('Mostrar dados de qual jogador?(999 para parar) '))
                if esc == 999:
                    break
                if esc >= len(lista):
                    print(f'O jogador {esc} não está na lista')
                else:
                    print(f'Levantamento do jogador {lista[esc]["Nome"]}')
                    for i, g in enumerate(lista[esc]["Gols"]):
                        print(f'No jogo {i+1} fez {g} gols')
                print()
            print('_' * 40)
            print('Finalizando o programa')
            exit()
        elif resp == 'S':
            break
        else:
            print('ERRO! Digite apenas S ou N')
