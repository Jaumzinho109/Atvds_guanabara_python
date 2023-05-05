def vmaior(* valores):
    cont = maior = 0
    for valor in valores: 
        print(f'{valor}',end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'O maior valor é {maior}')


vmaior(2, 4, 5 ,7, 9, 0)