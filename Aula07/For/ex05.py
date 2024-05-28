a=0
b=1
print(a)
print(b)
for _ in range(8):
    proximo=a+b
    print(proximo)
    a_antigo=a
    a=b
    b=proximo