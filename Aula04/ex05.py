deposito=float(input(f"Quanto você deseja depositar no Depósito?\n"))
juros=float(input(f"Qual é o valor da Taxa de Juros?\n"))
rendimento=(deposito*juros)/100
valor_total=deposito+rendimento
print(f"O valor depositado foi R${deposito} com um juros de {juros}%."
      f"\nO rendimento foi de R${rendimento}. O rendimento total foi de R${valor_total}.")