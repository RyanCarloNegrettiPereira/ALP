n=int(input(f'Digite um númer: '))
if n%5==0 and n%3==0:
    print(f'{n} é divisível por 5 e 3.\n'
          f'{n}/5= {n/5}\n'
          f'{n}/3= {n/3}')
else:
    if n%5==0 and n%3!=0:
        print(f'{n} não é divisível por 3.\n'
              f'{n}/5= {n/5}')
    elif n%5!=0 and n%3==0:
        print(f'{n} não é divisível por 5.\n'
              f'{n}/3= {n/3}')
    else:
        print(f'{n} não é divisível por 5 e 3.')