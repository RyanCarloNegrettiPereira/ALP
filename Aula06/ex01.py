v=float(input(f'Quanto você gastou na compra?\n'))
if v<1001:
    print(f'Desconto de 10% no valor da compra: R${v*0.1}\n'
          f'Total= R${v-v*0.1}')
elif v<5001:
    print(f'Desconto de 20% no valor da compra: R${v*0.2}\n'
          f'Total= R${v-v*0.2}')
else:
    print(f'Desconto de 30% no valor da compra: R${v*0.3}\n'
          f'Total= R${v-v*0.3}')