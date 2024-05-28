frase=input("Digite uma frase: ")
contador_vogais=0
vogais=['a', 'e', 'i', 'o', 'u']
for caractere in frase:
    caractere=caractere.lower()
    if caractere in vogais:
        contador_vogais+=1
print(f"Número de vogais na frase: {contador_vogais}")