soma_pesos=0
soma_alturas=0
maior_imc=0
menor_imc=1
i=0
while i<5:
    peso=float(input("Digite o peso (em kg): "))
    altura=float(input("Digite a altura (em metros): "))
    soma_pesos+=peso
    soma_alturas+=altura
    imc=peso/(altura**2)
    print(f"IMC da pessoa {i+1} é: {imc:.2f}")
    if imc>maior_imc:
        maior_imc=imc
    if imc<menor_imc:
        menor_imc=imc
    i+=1
peso_medio=soma_pesos/5
altura_medio=soma_alturas/5
print(f"Peso médio: {peso_medio:.2f} kg\n"
      f"Altura média: {altura_medio:.2f} m\n"
      f"Maior IMC: {maior_imc:.2f}\n"
      f"Menor IMC: {menor_imc:.2f}")