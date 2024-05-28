numero=int(input("Digite um número inteiro maior que 1: "))
primo=True
if numero<=1:
    primo=False
else:
    for i in range(2, numero):
        if numero%i==0:
            primo=False
            break
if primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")