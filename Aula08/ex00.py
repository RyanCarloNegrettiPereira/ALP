nome1=input(f'Digite seu 1º nome: ')
id=input(f'Tem 2º nome?\n').upper()
if id=='SIM' or id=='S':
    nome2=input(f'Digite seu 2º nome: ')
    sobrenome=input(f'Digite seu sobrenome: ')
    nome_completo=nome1+' '+nome2+' '+sobrenome
    print(nome_completo)
else:
    sobrenome=input(f'Digite seu sobrenome: ')
    nome_completo=nome1+' '+' '+sobrenome
    print(nome_completo)