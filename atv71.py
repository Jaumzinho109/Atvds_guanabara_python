valor = int(input('Quantos reais você quer sacar? '))
total = valor
ced = 50
c50 = c20 = c10 = c1 = 0
while True:
    if total >= 50:
        c50 += 1
        total -= 50
    elif total < 50 and total >= 20:
        c20 +=1
        total -= 20
    elif total < 20 and total >= 10:
        c10 += 1
        total -= 10
    elif total < 10 and total >= 1:
        c1 += 1
        total -= 1
    elif total < 1:
        break
print('Total de {} notas de 50'.format(c50))
print('Total de {} notas de 20'.format(c20))
print('Total de {} notas de 10'.format(c10))
print('Total de {} notas de 1'.format(c1))

