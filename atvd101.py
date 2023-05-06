from datetime import datetime

def voto(ano):
   idade = datetime.now().year - ano
   print('_' * 50)
   if (idade >= 16 and idade < 18) or idade >= 60:
      print(f'Com {idade} de idade, o seu voto é opcional!')
   elif (idade >= 18 and idade < 60):
      print(f'Com a idade de {idade}, o seu voto é obrigatório!')
   else:
      print(f'Com a idade de {idade}, você não pode votar!')

ano = int(input('Qual foi o ano do seu nascimento? '))
voto(ano)


