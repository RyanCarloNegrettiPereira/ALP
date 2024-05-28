x=int(input("Digite um número inteiro para calcular o fatorial: "))
fatorial=1
for i in range(1, x+1):
    fatorial*=i
print(f"O fatorial de {x} é: {fatorial}")