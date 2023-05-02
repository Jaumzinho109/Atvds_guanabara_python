lista = ("Abacaxi", "Cadeira", "Telefone", "Cachorro", "Amor", "Mesa", "Computador", "Felicidade", "Chocolate", "Carro")
for p in lista:
    print('\nNa palavra {} temos as vogais: '.format(p))
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')
