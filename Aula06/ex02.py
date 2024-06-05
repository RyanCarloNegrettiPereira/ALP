largura=float(input("Digite a largura do aposento em metros: "))
comprimento=float(input("Digite o comprimento do aposento em metros: "))
litros_por_lata=float(input("Digite a quantidade de litros por lata de tinta: "))
altura=2.8
largura_porta=0.8
altura_porta=2.1
area_porta=largura_porta*altura_porta
rendimento_tinta=3
area_paredes=2*altura*(largura+comprimento)-area_porta
litros_necessarios=area_paredes/rendimento_tinta
latas_necessarias=litros_necessarios/litros_por_lata
if latas_necessarias.is_integer():
    latas_necessarias=int(latas_necessarias)
else:
    latas_necessarias=int(latas_necessarias)+1
print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")