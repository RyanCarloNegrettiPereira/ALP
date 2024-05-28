matriz=[]
print("Digite os elementos da matriz 4x4:")
for i in range(4):
    linha=[]
    for j in range(4):
        elemento=float(input(f"Digite o elemento {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)
soma_diagonal_principal=sum(matriz[i][i] for i in range(4))
print(f"A soma dos elementos da diagonal principal é: {soma_diagonal_principal}")