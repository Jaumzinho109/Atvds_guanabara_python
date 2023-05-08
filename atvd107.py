import atvd107_mod
preco = float(input('Informe o valor do produto: '))
valor_final = atvd107_mod.aumentar(v=preco)
print(f'Diminuindo {preco} em 13%, teremos {atvd107_mod.diminuir(preco)} ')
print(f'Aumento em 10%, o preço final será: {valor_final}')
print(f'O dobro de {preco} é igual a {atvd107_mod.dobro(preco)}')
print(f'A metade de {preco} é igual a {atvd107_mod.metade(preco)}')