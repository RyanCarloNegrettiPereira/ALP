soma_pares=0
contador_pares=0
for _ in range(1, 1000000):
    numero = int(input("Digite um número (0 para finalizar): "))
    if numero == 0:
        break
    if numero%2==0:
        soma_pares+=numero
        contador_pares+=1
if contador_pares>0:
    media_pares=soma_pares/contador_pares
    print(f"Média aritmética dos números pares: {media_pares:.2f}")
else:
    print("Nenhum número par foi fornecido.")