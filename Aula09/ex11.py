matriz=[]
print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha=[]
    for j in range(3):
        elemento=float(input(f"Digite o elemento {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)
transposta=[[matriz[j][i] for j in range(3)] for i in range(3)]
print("Matriz transposta:")
for linha in transposta:
    print(linha)