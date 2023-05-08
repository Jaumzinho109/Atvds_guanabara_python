import atvd108_mod
prec = str(input('Informe o valor do produto: '))
preco = float(prec)
print(f'Diminuindo {atvd108_mod.moeda(preco)} em 13%, teremos {atvd108_mod.moeda(atvd108_mod.diminuir(preco))} ')
print(f'Aumento em 10%, o preço final será: {atvd108_mod.moeda(atvd108_mod.aumentar(preco))}')
print(f'O dobro de {preco} é igual a {atvd108_mod.moeda(atvd108_mod.dobro(preco))}')
print(f'A metade de {preco} é igual a {atvd108_mod.moeda(atvd108_mod.metade(preco))}')
