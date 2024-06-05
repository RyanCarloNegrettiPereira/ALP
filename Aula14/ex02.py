numero_string=input("Digite um número positivo: ")
soma_digitos=0
multiplicacao_digitos=1
for char in numero_string:
    digito=int(char)
    soma_digitos+=digito
    multiplicacao_digitos*=digito
print(f"A soma dos dígitos é: {soma_digitos}")
print(f"A multiplicação dos dígitos é: {multiplicacao_digitos}")