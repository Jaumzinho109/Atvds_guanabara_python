def LeiaInt(msg): 
   while True:
    try:
       n = int(input(msg))
    except (TypeError, ValueError):
      print('Digite um número inteiro válido')
      continue
    except (KeyboardInterrupt):
      print('O usuário preferiu não digitar nenhum número.')
      return 0
    else:
      return n
def LeiaFloat(floats):
     while True:
        try:
            n = float(input(floats))
        except (TypeError, ValueError):
            print('Digite um número inteiro válido')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar nenhum número.')
            return 0
        else:
            return n

num = LeiaInt('Escreva um número inteiro: ')
real = LeiaFloat('Agora, um número real: ')
print(f'O valor inteiro foi {num}, enquanto o real {real}')