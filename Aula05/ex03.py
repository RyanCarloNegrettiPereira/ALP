print(f"Identificador de Triângulos.")
a=float(input(f"Digite o valor do 1º lado: "))
b=float(input(f"Digite o valor do 2º lado: "))
c=float(input(f"Digite o valor do 3º lado: "))
if a+b>c and a+c>b and b+c>a:
    print(f"Temos um Triângulo.")
    if a==b and b==c and c==a:
        print(f"Temos um Triângulo Equilátero.")
    elif a==b or b==c or a==c:
        print(f"Temos um Triângulo Isosceles.")
    else:
        print(f"Temos um Triângulo Escaleno.")
else:
    print(f"Não é possivel formar um Triângulo.")