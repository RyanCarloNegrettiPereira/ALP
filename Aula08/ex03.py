frase=input("Digite uma frase: ")
contador_palavras=0
for caractere in frase:
    if caractere==' ':
        contador_palavras+=1
contador_palavras+=1
print(f"Número de palavras na frase: {contador_palavras}")