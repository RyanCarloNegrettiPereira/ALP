matriz = []
print("Digite os elementos da matriz 2x2:")
for i in range(2):
    linha=[]
    for j in range(2):
        elemento=int(input(f"Digite o elemento {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)
maior_elemento=max(max(matriz))
matriz_resultante=[[elemento*maior_elemento for elemento in linha] for linha in matriz]
print(f"Matriz resultante (original multiplicada pelo maior elemento):")
for linha in matriz_resultante:
    print(linha)