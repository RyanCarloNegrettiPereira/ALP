n=int(input("Digite um valor inteiro e positivo para N: "))
E=0
for i in range(1, n + 1):
    E+=2**i
print(f"O valor de E segundo a formula 'E=(2**1)+...+(2**N)' é: {E}")