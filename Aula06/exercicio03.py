larg=float(input(f"Quantos metros de largura tem seu aposento?\n"))
comp=float(input(f"Quantos metros de comprimento tem seu aposento?\n"))
print(f"Existe 3 tipos de lata de tinta.\n"
      f"1 Litro;\n"
      f"3,7 Litros;\n"
      f"18 Litros.")
pedi=2.8
porta=0.80*2.1
metros=(((larg*pedi)*2)+((comp*pedi)*2)-porta)
print(f"Seu aposento tem {metros:.2f}m.\n"
      f"1 litro de tinta pode pintar 3m².")
litros=metros/(3**2)
print(f"Você irá precisar de {litros:.2f}L de tinta.")