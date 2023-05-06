def fatorial (num, show):
    c = num - 1
    fat = num * c
    print('_' * 40)
    while True:
        if show == True:
            if c == num - 1:
                print(f'{num} x {c} x ', end='')
            elif c == 1:
                print(f'{c} ', end= '')
            else:
                print(f'{c} x ', end='')
        c -= 1
        if c == 0:
            break
        fat = fat * c
    if show == True:
        print(f'= {fat}')
    else:
        print(fat)

num = int(input('Quer saber o fatorial de qual número? '))
fatorial(num, show= True)