def total_de_segundos():
    total_segundos=(h*3600)+(m*60)+s
    return total_segundos
h=int(input("Digite o número de horas: "))
m=int(input("Digite o número de minutos: "))
s=int(input("Digite o número de segundos: "))
print(f"{h} horas, {m} minutos e {s} segundos correspondem a {total_de_segundos()} segundos.")