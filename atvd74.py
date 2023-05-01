from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
ordenado = sorted(n)
print('Aqui está a listagem dos números{}'.format(n))
print('O menor número sorteado foi {}'.format((min(ordenado))))
print('O maior número sorteado foi {}'.format(max(ordenado)))