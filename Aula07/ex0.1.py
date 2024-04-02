valor=int(input(f'Digite um valor inteiro e positivo para "n": '))
n=1
soma=0
while n<=valor:
    soma=soma+(2**n)
    n=n+1
print(f'O valor de E=((2¹)+...+(2^{valor}) é: {soma}')