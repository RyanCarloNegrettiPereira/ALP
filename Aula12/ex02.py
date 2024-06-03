def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return 1
    else:
        return 0
ano=int(input("Digite um ano no formato AAAA: "))
print(bissexto(ano))