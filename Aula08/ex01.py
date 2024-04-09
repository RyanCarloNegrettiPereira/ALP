print(f'Digite a data.')
dia=int(input(f'Dia: '))
if dia>9:
    a=1
else:
    a=0
mes=int(input(f'Mês: '))
if mes>9:
    b=1
else:
    b=0
ano=int(input(f'Ano: '))
if a==1 and b==1:
    print(f'{ano}/{mes}/{dia}')
elif a==1 and b==0:
    print(f'{ano}/{mes}/0{dia}')
elif a==0 and b==1:
    print(f'{ano}/0{mes}/{dia}')
else:
    print(f'{ano}/0{mes}/0{dia}')