primos=[]
num=101
while len(primos)<10:
    eh_primo=True
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            eh_primo=False
            break
    if eh_primo:
        primos.append(num)
    num+=1
tupla=tuple(primos)
print(f'Os 10 primeiros números primos acima de 100 são:\n{tupla}')