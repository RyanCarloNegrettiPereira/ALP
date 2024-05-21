ra=input('Digite seu RA: ')
soma=0
multiplicador=1
for i in range(len(ra)):
    soma+=int(ra[i])
    multiplicador*=int(ra[i])
print(f'A soma é: {soma}\n'
      f'A multiplicação é: {multiplicador}')