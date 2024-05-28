matriz=[]
print("Digite os elementos da matriz 10x20:")
for i in range(10):
    linha=[]
    for j in range(20):
        elemento=int(input(f"Digite o elemento {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)
somas_linhas=[]
for linha in matriz:
    soma=sum(linha)
    somas_linhas.append(soma)
matriz_resultante=[[elemento*somas_linhas[i] for elemento in linha] for i, linha in enumerate(matriz)]
print("Matriz resultante:")
for linha in matriz_resultante:
    print(linha)