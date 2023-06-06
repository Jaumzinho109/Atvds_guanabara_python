import arquivotext
lista = [
        {"nome:João", "idade:24"},
        {"nome:Marcelo", "idade:18"},
        {"nome:Luciano", "idade:19"},
        {"nome:Maria", "idade:28"}
        ]
dic = dict()
def opcoes():
    while True:
        n = input('Sua opção: ')
        if n.isnumeric():
            opcao = float(n)
            if opcao == 1:
                print('_' * 30)
                print()
                print('Pessoas Cadastradas')
                print('_' * 30)
                for k, v in enumerate(lista):
                    print(f'{v}')
                return opcao
            elif opcao == 2:
                print('_' * 30)
                print()
                print('Novo cadastro')
                print('_' * 30)
                dic["nome"] = str(input('Qual o nome? '))
                dic["idade"] = int(input('Qual a idade? '))
                print(dic)
                lista.append(dic.copy())
                dic.clear()
                return opcao
            elif opcao == 3:
                print('_' * 30)
                print()
                print('SAINDO DO SISTEMA....')
                print('_' * 30)
                exit()
            else:
                print('Digite um dos números citados, por favor.')
        else:
            print('Não aceitamos textos, por favor digite um dos números citados.')

