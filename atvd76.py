lista = ("Caderno universitário", 15.00,
"Lápis preto nº 2", 1.00,
"Caneta esferográfica azul ou preta", 2.00,
"Borracha branca", 1.50,
"Apontador", 3.00,
"Régua de 30cm", 2.50,
"Cola branca", 5.00,
"Tesoura sem ponta", 10.00,
"Marcador de texto", 2.50,
"Pasta catálogo com 50 plásticos", 25.00,)
print('-'*30)
print('Lista de compras escolares')
print('-'*30)
for pos in range (0,len(lista)):
    if pos % 2 == 0:
        print(' {} custa'.format(lista[pos]), end=' ')
    else:
        print('R$ {}'.format(lista[pos]))
