salario=float(input(f"Qual é o salário do funcionario?\n"))
percentual=float(input(f"Qual é o percentual de aumento?\n"))
aumento=(salario*percentual/100)
novo_salario=salario+aumento
print(f"O salario do funcionario erá de R${salario} e teve um aumento de {percentual}% igula a R${aumento}.")
print(f"O salario atual do funcionario é de R${novo_salario}.")