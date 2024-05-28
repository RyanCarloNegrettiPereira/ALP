from math import sqrt
print(f"Solucionador da Equação do 2º Grau.")
a=float(input(f"Digite o valor de a: "))
if a!=0:
    b = float(input(f"Digite o valor de b: "))
    c = float(input(f"Digite o valor de c: "))
    delta=(b**2)-4*(a*c)
    if delta<0:
        print(f"O valor de Delta é menor que Zero, não temos raizes reais.")
    elif delta==0:
        print(f"O valor de Delta é igual a Zero, só temos uma raiz real.")
        x1=-b/2*a
        print(f"A raiz é: {x1}")
    else:
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        print(f"O valor de Delta é maior que Zero, temos duas raizes reais.")
        print(f"1º raiz: {x1}\n2º raiz: {x2}")
else:
    print(f"Não é possivel fazer está equação pois a é igual a zero.")