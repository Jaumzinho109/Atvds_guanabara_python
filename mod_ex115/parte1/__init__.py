def opcoes():
    while True:
        n = input('Sua opção: ')
        if n.isnumeric():
            opcao = float(n)
            if opcao == 1:
                print('_' * 30)
                print()
                print('Opção 1')
                print('_' * 30)
                return opcao
                continue
            elif opcao == 2:
                print('_' * 30)
                print()
                print('Opção 2')
                print('_' * 30)
                return opcao
                continue
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
