valor=int(input(f'Digite um valor inteiro e positivo para "n": '))
soma=0
for i in range(1,(valor+1)):
    soma=soma+(2**i)
print(f'O valor de E=((2¹)+...+(2^{valor})) é: {soma}')