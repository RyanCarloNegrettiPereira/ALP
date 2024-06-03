from math import pi
def volume():
    v=(4/3)*pi*(r**3)
    return v
r=int(input(f'Qual é o raio da esfera?\n'))
print(volume())