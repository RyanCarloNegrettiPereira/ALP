def identificar_primo():
    if n<2:
        return False
    else:
        i=1
        for i in range(n):
            if i==0:
                i=1
            if ((n/i)==1)and((n/i)==n):
                return True
            else:
                return False
print(f'True= É primo\n'
      f'False= Não é primo')
n=int(input(f'Digite um número para vermos se ele é primo e ver quantos números primos temos até o mesmo:\n'))
print(identificar_primo())
'''Tentei.'''