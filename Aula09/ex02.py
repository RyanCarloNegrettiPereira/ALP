vetor1 = []
vetor2 = []
print("Digite os elementos do primeiro vetor:")
for i in range(5):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    vetor1.append(elemento)
print("\nDigite os elementos do segundo vetor:")
for i in range(5):
    elemento=int(input(f"Digite o {i+1}º elemento: "))
    vetor2.append(elemento)
vetor_resultante=[]
for i in range(5):
    vetor_resultante.append(vetor1[i])
    vetor_resultante.append(vetor2[i])
print("\nVetor resultante da intercalação:")
print(vetor_resultante)