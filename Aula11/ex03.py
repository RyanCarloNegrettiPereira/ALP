pessoas={}
num_pessoas=int(input("Quantas pessoas você deseja inserir (pelo menos 5)? "))
while num_pessoas<5:
    print("Por favor, insira pelo menos 5 pessoas.")
    num_pessoas=int(input("Quantas pessoas você deseja inserir (pelo menos 5)? "))
for _ in range(num_pessoas):
    nome=input("Digite o nome: ")
    idade=int(input("Digite a idade: "))
    pessoas[nome]=idade
media_idades=sum(pessoas.values())/len(pessoas)
nomes_acima_media=[nome for nome, idade in pessoas.items() if idade > media_idades]
print(f"Nomes com idade maior que a média ({media_idades:.2f} anos):")
for nome in nomes_acima_media:
    print(nome)