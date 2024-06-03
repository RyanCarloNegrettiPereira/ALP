pessoas={}
for _ in range(10):
    sobrenome=input("Digite o sobrenome: ")
    idade=int(input("Digite a idade: "))
    pessoas[sobrenome]=idade
sobrenome_mais_velho=max(pessoas, key=pessoas.get)
print(f'O sobrenome da pessoa com a maior idade é: {sobrenome_mais_velho}')