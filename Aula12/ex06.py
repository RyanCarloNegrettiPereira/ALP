def eh_primo(numero):
    if numero<=1:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero%i==0:
            return False
    return True
def contar_primos(n):
    if n<=0:
        print("O número deve ser maior que zero.")
        return
    if n>=1:
        contagem_primos=1
    else:
        contagem_primos=0
    for numero in range(2, n + 1):
        if eh_primo(numero):
            contagem_primos += 1
    print(f"A quantidade de números primos entre 1 e {n} é: {contagem_primos}")
n=int(input("Digite um número inteiro positivo maior que zero: "))
contar_primos(n)
