a=float(input(f"Quanto você gastou no produto?\n"))
if a<=1000.00:
    desconto=a*0.1
    print(f"Você gastou R${a} na compra do produto. Portanto teve um desconto de 10%.\n"
          f"Valor final: R${(a-desconto):.2f}")
elif a>=1001.00 and a<5000.00:
    desconto=a*0.2
    print(f"Você gastou R${a} na compra do produto. Portanto teve um desconto de 20%.\n"
          f"Valor final: R${(a-desconto):.2f}")
else:
    desconto=a*0.3
    print(f"Você gastou R${a} na compra do produto. Portanto teve um desconto de 30%.\n"
          f"Valor final: R${(a-desconto):.2f}")