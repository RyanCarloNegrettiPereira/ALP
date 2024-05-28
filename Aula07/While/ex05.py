a=0
b=1
print(a)
print(b)
contador=2
while contador<10:
    proximo=a+b
    print(proximo)
    a_antigo=a
    a=b
    b=proximo
    contador+=1