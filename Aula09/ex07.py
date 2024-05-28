a=[]
b=[]
print("Digite 10 números inteiros:")
for i in range(10):
    numero=int(input(f"Digite o {i+1}º número: "))
    a.append(numero)
b=sorted(a)
print(f"Vetor A (números digitados): {a}")
print(f"Vetor B (números ordenados): {b}")