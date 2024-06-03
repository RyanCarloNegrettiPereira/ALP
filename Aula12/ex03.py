def mdc(a, b):
    while b!=0:
        a, b=b, a%b
    return a
a=int(input("Digite o primeiro número inteiro: "))
b=int(input("Digite o segundo número inteiro: "))
print(f"O MDC de {a} e {b} é: {mdc(a, b)}")