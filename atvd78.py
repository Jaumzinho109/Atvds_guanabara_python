valor = []
maior = 0
menor = 0
for c in range (0,5):
    valor.append(int(input('Informe um número inteiro: ')))
    for n in valor:
        if n > maior:
            maior = n
        elif c == 1:
            menor = n
        elif c > 1:
            if n < menor:
                menor = n
for i, v in enumerate(valor):       
    if v == maior:
        print('A posição do maior valor foi {}'.format(i))
    elif v == menor:
        print('A posição do menor número foi {}'.format(i))
print('O maior número da lista é {}'.format(maior))
print('O menor número da lista foi {}'.format(menor))
