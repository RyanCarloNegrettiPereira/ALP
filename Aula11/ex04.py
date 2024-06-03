lista1=[]
lista2=[]
print("Digite 5 números inteiros para a primeira lista:")
for _ in range(5):
    numero=int(input("Digite um número inteiro: "))
    lista1.append(numero)
print("Digite 5 números inteiros para a segunda lista:")
for _ in range(5):
    numero=int(input("Digite um número inteiro: "))
    lista2.append(numero)
conjunto_uniao=set(lista1).union(set(lista2))
print("O conjunto resultante da união das duas listas é:")
print(conjunto_uniao)