palavra=input(f'Digite uma palavra: ')
arvalap=palavra[::-1]
if palavra==arvalap:
    print(f'Sua palavra é um palíndromo.')
else:
    print(f'Sua palavra não é um palíndromo.')