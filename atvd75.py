num = (int(input('Informe um número inteiro entre 1 e 10: ')), int(input('Informe um número inteiro entre 1 e 10: ')),
        int(input('Informe um número inteiro entre 1 e 10: ')), int(input('Informe um número inteiro entre 1 e 10: ')))
print(num.count(9))
if 3 in num:
    print(num.index(3)+1)
else:
    print('O valor 3 não foi digitado.')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')