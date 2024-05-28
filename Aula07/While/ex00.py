n=int(input("Digite um valor inteiro e positivo para N: "))
E=0
i=1
while i <= n:
    E += 2 ** i
    i += 1
print(f"O valor de E segundo a formula 'E=(2**1)+...+(2**N)' é: {E}")