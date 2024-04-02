n=0
soma=0
qtd=0
while 1:
    n=n+1
    if (n%2)==0:
        soma=soma+n
        qtd=qtd+1
    if qtd==50:
        break
print(f'A soma dos {qtd} primeiros números pares é: {soma}')