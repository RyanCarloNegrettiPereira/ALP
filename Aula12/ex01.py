def verificador():
    if n<1:
        return False
    else:
        for i in range(2, n):
            if n%i==0:
                return False
            else:
                return True
n=int(input("Digite um número inteiro maior que 1: "))
print(verificador())