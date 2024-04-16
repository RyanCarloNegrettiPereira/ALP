from random import randint
resultados=[0]*7
freq=[0]*7
print(resultados)
for i in range(6000):
    lado=randint(1,6)
    resultados[lado]=resultados[lado]+1
for i in range(1,7):
    freq[i]=resultados[i]/6000
print(resultados)
print(freq)