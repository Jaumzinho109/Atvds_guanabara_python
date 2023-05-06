def notas(*nota, sit=False):
    r = dict()
    r['Total'] = len(nota)
    r['maior'] = max(nota)
    r['Menor'] = min(nota)
    r['Média'] = sum(nota)/len(nota)
    if sit:
        if r['Média'] >= 8.0:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 6:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'

    return r

r = notas(4.7, 10, 10, sit= True)
print(r)

