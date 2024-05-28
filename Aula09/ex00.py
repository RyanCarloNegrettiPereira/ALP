vetor=[]
for i in range(10):
    elemento=int(input(f"Digite o {i+1}º elemento: "))
    vetor.append(elemento)
print("Vetor na ordem inversa de entrada:")
for i in range(9, -1, -1):
    print(vetor[i])