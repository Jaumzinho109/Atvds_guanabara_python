not_t = list()
nota = list()
while True:
    nome = str(input('Escreva o seu nome: '))
    nota.append(nome)
    nota1 = float(input('Informe a sua primeira nota: '))
    nota2 = float(input('Agora a segunda nota: '))
    nota.append([nota1, nota2])
    media = (nota1+nota2)/2
    nota.append(media)
    not_t.append(nota[:])
    nota.clear()
    resp = str(input('Você quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
for n, v in enumerate (not_t):
    print(f'O/A aluno(a) com o número {n} e nome {v[0]} obteve a média {v[2]}')

while True:
    resp = int(input('Você quer saber as notas de qual aluno? (Digitar 999 interrompe)'))
    if resp == 999:
        break
    if resp == len(not_t) - 1:
        print(f'Notas de {not_t[resp][0]} são {not_t[resp][1]}')