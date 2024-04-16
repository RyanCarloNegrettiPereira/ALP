lista=[]
for i in range(5):
    v=int(input(f"Digite o {i}º valor: "))
    lista.append(v)
print(f"O maior item da lista é: {max(lista)}")
print(f"Sua posição é: {lista.index(max(lista))}")