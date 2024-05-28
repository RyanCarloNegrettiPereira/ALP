print(f"Categoria:  |Idade:")
print(f"Infantil    |5 à 7\n"
      f"Juvenil     |8 à 10\n"
      f"Adolescente |11 à 15\n"
      f"Adulto      |16 à 30\n"
      f"Sênior      |Acima de 30")
idade=int(input("Informe sua idade: "))
if idade>=5 and idade<=7:
    print(f"Sua categoria é Infantil.")
elif idade>=8 and idade<=10:
    print(f"Sua categoria é Juvenil.")
elif idade>=11 and idade<=15:
    print(f"Sua categoria é Adolescente.")
elif idade>=16 and idade<=30:
    print(f"Sua categoria é Adulto.")
elif idade>30:
    print(f"Sua categoria é Sênior.")
else:
    print(f"Você ainda não pode participar por não ter a idade mínima!")