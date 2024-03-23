print(f"Código de origem |Procedência  |% Imposto\n"
      f"1                |Sul          |11%\n"
      f"2                |Norte        |13%\n"
      f"3                |Nordeste     |9%\n"
      f"4                |Centro-Oeste |12%\n"
      f"5                |Sudeste      |18%")
liquido=float(input("Informe o valor Líquido do seu produto: "))
categoria=float(input("Informe a categoria do produto: "))
if categoria==1:
    imposto=liquido*0.11
    valorfinal=liquido-imposto
    print(f"O produto procede do Sul.\nValor final: R${valorfinal:.2f}")
elif categoria==2:
    imposto=liquido*0.13
    valorfinal=liquido-imposto
    print(f"O produto procede do Norte.\nValor final: R${valorfinal:.2f}")
elif categoria ==3:
    imposto=liquido*0.09
    valorfinal=liquido-imposto
    print(f"O produto procede do Nordeste.\nValor final: R${valorfinal:.2f}")
elif categoria ==4:
    imposto=liquido*0.12
    valorfinal=liquido-imposto
    print(f"O produto procede do Centro-Oeste.\nValor final: R${valorfinal:.2f}")
elif categoria ==5:
    imposto=liquido*0.18
    valorfinal=liquido-imposto
    print(f"O produto procede do Sudeste.\nValor final: R${valorfinal:.2f}")
else:
    print(f"Não temos está Categoria no momento.")