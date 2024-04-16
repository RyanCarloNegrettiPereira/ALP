lista0=[]
for i in range(5):
    v0=int(input(f"Digite o {i}º valor: "))
    lista0.append(v0)
lista1=[]
for i in range(5):
    v1=int(input(f"Digite o {i}º valor: "))
    lista1.append(v1)
lista2=[]
for i in range(10):
    lista2.insert(lista0[i])
    lista2.insert(lista1[i])
print(lista2)