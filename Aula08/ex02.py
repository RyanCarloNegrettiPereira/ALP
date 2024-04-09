frase=input(f'Digite uma frase: ').lower()
v=0
for letra in frase:
    if letra in "aáàâãeéêiíoóôõuúû":
        v=v+1
if v==1:
    print(f'Em sua frase temos {v} vogal.')
else:
    print(f'Em sua frase temos {v} vogais.')