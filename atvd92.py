from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Qual é o seu nome? '))
nascimento = int(input('Em que ano você nasceu? '))
dados['Idade'] = datetime().now().year - nascimento
carteira = int(input('Digite o valor da sua carteira de trabalho: '))
if carteira != 0:
    dados['ctps'] = carteira
    salario = int(input('Qual é o seu salário? '))
    dados['Salário'] = salario
    ano_cont = int(input('Em que ano você foi contratado? '))
    dados['Ano de contratação'] = ano_cont
    ano_apos = ano_cont + 35
    idade_apos = ano_apos - nascimento
    dados['Idade da aposentadoria'] = idade_apos
else:
    dados['ctps'] = carteira
print(f'O nome tem o valor {dados["Nome"]}')
print(f'A idade tem o valor {dados["Idade"]}')
if dados['ctps'] == 0:
    print('O ctps tem o valor 0')
else:
    print(f'ctps tem o valor {dados["ctps"]}')
    print(f'O salário tem valor {dados["Salário"]}')
    print(f'A contratação tem valor {dados["Ano de contratação"]}')
    print(f'A aposentadoria tem valor {dados["Idade da aposentadoria"]}')