print(f'Calculador de IMC')
soma_altura=0
soma_peso=0
maior_imc=0
menor_imc=100
for i in range(0,5):
    altura=float(input(f'Digite sua altura em m: '))
    peso=float(input(f'Digite seu peso em Kg: '))
    imc=peso/(altura**2)
    print(f'Su IMC é: {imc:.2f}')
    soma_altura=soma_altura+altura
    soma_peso=soma_peso+peso
    if imc>=maior_imc:
        maior_imc=imc
    if imc<=menor_imc:
        menor_imc=imc
media_peso=soma_peso/5
media_altura=soma_altura/5
print(f'A média das alturas é: {media_altura:.2f}m.\n'
      f'A média dos pesos é: {media_peso:.2f}Kg.\n'
      f'O maior IMC é: {maior_imc:.2f}Kg/m².\n'
      f'O menor IMC é: {menor_imc:.2f}Kg/m².')