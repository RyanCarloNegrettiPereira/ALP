palavras=[]
for i in range(20):
    palavra = input(f"Digite a {i+1}ª palavra (no máximo 10 caracteres): ")
    if len(palavra)>10:
        print("A palavra deve ter no máximo 10 caracteres. Por favor, tente novamente.")
        continue
    palavras.append(palavra)
for i in range(len(palavras)):
    palavras[i]=palavras[i][::-1]
print("\nPalavras invertidas:")
for palavra in palavras:
    print(palavra)