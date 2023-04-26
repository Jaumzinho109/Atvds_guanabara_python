soma = 0
tot_mais_1000 = 0
nome_prodb = ''
cont = 0
while True:
    nome = str(input('Qual é o nome do produto? '))
    preco = float(input('Quanto custa esse produto em reais? '))
    cont += 1
    if cont == 1:
        prod_barato = preco
    soma += preco
    if preco > 1000:
        tot_mais_1000 += 1
    if preco < prod_barato:
        prod_barato = preco
        nome_prodb = nome
    resposta = str(input('Você quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break
print('O valor total dos produtos é igual a {}'.format(soma))
print('{} produto(s) custa(m) mais que 1000 reais'.format(tot_mais_1000))
print('O produto mais barato é {}'.format(nome_prodb))