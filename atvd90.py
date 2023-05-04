dados = dict()
dados['Nome'] = str(input('Digite o seu nome: '))
dados['Média'] = float(input('Agora, a sua média: '))

print(f'O seu nome é {dados["Nome"]}', end=' ')
print(f'e conseguiu a média {dados["Média"]}')

if dados['Média'] >= 7.0:
    print('Parabéns, você foi aprovado.')
else:
    print('Que pena!! Você está reprovado')