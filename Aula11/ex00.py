lista=[]
for i in range(10):
    numero=int(input(f'Digite um número: '))
    lista.append(numero)
tupla=tuple(lista)
print(tupla[::-1])