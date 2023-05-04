dados_dict = dict()
dados_list = list()
dict_mulher = dict()
lista_mulheres = list()
soma = 0

while True:
    nome = str(input('Qual é o seu nome? '))
    dados_dict['Nome'] = nome

    while True:
        sexo = str(input('Qual é o seu sexo? [M/F] ')).upper()
        if sexo == "M" or sexo == "F":
            dados_dict['Sexo'] = sexo
            if sexo == "F":
                dict_mulher['Nome das mulheres'] = nome
                lista_mulheres.append(dict_mulher.copy())
                dict_mulher.clear()

            break
        print('ERRO! Digite apenas M ou F.')

    idade = int(input('Qual é a sua idade? '))
    dados_dict['Idade'] = idade
    soma += idade
    dados_list.append(dados_dict.copy())
    dados_dict.clear()

    while True:
        resp = str(input('Você quer continuar? [S/N] ')).upper()
        if resp == "S":
            break
        elif resp == "N" :
            print('-=' * 30)
            print(f'Ao todo temos {len(dados_list)} pessoa(s) cadastrada(s).')
            print(f'A média de idade é {soma/len(dados_list)}')
            print(f'O(s) nome(s) da(s) mulhere(s) cadastrada(s): ', end='')
            for k, v in enumerate (lista_mulheres):
                for i, q in v.items():
                    print(q, end=' ')
            print('    ')
            print('\nPessoas acima da média de idade: ')
            for p in dados_list:
                if p['Idade'] > soma/len(dados_list):
                    print('    ')
                    for k, v in p.items():
                        print(f'{k} = {v};', end=' ')
                    print()
            print('-=' * 30)
            exit_msg = 'Programa encerrado. Volte sempre!'
            print(exit_msg.center(60, ' '))
            exit()
        print('ERRO! Digite apenas S ou N')
    print('-' * 60)
