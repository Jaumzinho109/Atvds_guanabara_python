matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somac = 0
maior = 0

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l}][{c}]'))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            somac += matriz[l][c]
        if l == 1 and maior <= matriz[l][c]:
            maior = matriz[l][c]

for l in range (0,3):
    for c in range (0,3):
        print(f'{matriz[l][c]:^5}', end='')
    print()

print('E a soma de todos os pares é: {}'.format(soma))
print('A soma dos valores da terceira coluna é {}'.format(somac))
print('Por fim, o maior valor da segunda linha é {}'.format(maior))