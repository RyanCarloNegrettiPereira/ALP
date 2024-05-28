vetor=[]
for i in range(5):
    elemento=int(input(f"Digite o {i+1}º elemento: "))
    vetor.append(elemento)
maior_valor = vetor[0]
posicao_maior_valor = 0
for i in range(1, 5):
    if vetor[i]>maior_valor:
        maior_valor=vetor[i]
        posicao_maior_valor=i+1
print("Maior valor:", maior_valor)
print("Posição:", posicao_maior_valor)