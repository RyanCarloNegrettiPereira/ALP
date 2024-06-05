cabeças=int(input(f'Digite a quantidade de cabeças no cercado: '))
total_pes=cabeças*3+3
coelhos=(total_pes/2)-28
patos=cabeças-coelhos
print(f'Total de coelhos: {coelhos}\n'
      f'Total de patos: {patos}')