def aumentar(v, format = False):
    nv = v + 10*v/100
    return nv if format is False else ver(v)

def diminuir(v):
    nv = v - 13 * v / 100
    return nv

def dobro(v):
    nv = v * 2
    return nv

def metade(v):
    nv = v / 2
    return nv

def moeda(v, moeda='R$'):
    return (f'{moeda}{v}'.replace('.', ','))

def ver(v):
    print(f'O valor {v} não pode ser formatado.')
