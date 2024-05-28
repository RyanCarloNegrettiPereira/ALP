matriz = []
print("Digite os elementos da matriz 5x5:")
for i in range(5):
    linha=[]
    for j in range(5):
        elemento=float(input(f"Digite o elemento {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)
soma_elementos=0
num_elementos=0
for i in range(5):
    if i%2==1:
        for j in range(5):
            soma_elementos+=matriz[i][j]
            num_elementos+=1
if num_elementos!=0:
    media=soma_elementos/num_elementos
    print(f"A média dos elementos nas linhas pares da matriz é: {media}")
else:
    print("Não há elementos suficientes nas linhas pares para calcular a média.")