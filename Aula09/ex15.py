m=[]
l=[]
soma0=0
soma1=0
for y in range(5):
    for x in range(5):
        a=int(input(f"Digite um valor: "))
        l.append(a)
        a=0
    m.append(l)
    l=[]
for i in range(5):
    soma0=soma0+m[1][i]
    soma1=soma1+m[3][i]
for i in range(5):
    print(m)
print(f"A soma das linhas pares são: {soma0} e {soma1}")
print(f"A média da somas é: {(soma0+soma1)/5}")