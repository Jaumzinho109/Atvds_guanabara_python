tot_mais_18 = 0
tot_mulher_menos_20 = 0
tot_man = 0
while True:
    sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
    idade = int(input('Informe a sua idade: '))
    if idade > 18:
        tot_mais_18 += 1
    if sexo == 'M':
        tot_man += 1
    if sexo == 'F' and idade < 20:
        tot_mulher_menos_20 += 1
    opcao = int(input('Digite 1 para o programa parar ou qualquer outra coisa para continuar: '))
    if opcao == 1:
        break
print('O total de pessoas com mais de 18 anos é {}'.format(tot_mais_18))
print('{} mulhere(s) possuem menos de 20 anos'.format(tot_mulher_menos_20))
print('O total de homens é {}'.format(tot_man))