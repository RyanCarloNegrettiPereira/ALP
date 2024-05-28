from random import randint
frequencia={i: 0 for i in range(2, 13)}
for _ in range(30000):
    dado1=randint(1, 6)
    dado2=randint(1, 6)
    soma=dado1+dado2
    frequencia[soma]+=1
for soma, freq in frequencia.items():
    print(f"Soma {soma}: {freq} vezes")
total_jogadas=sum(frequencia.values())
freq_7=frequencia[7]
print(f"Verificação da frequência do valor 7:\n"
      f"Frequência do valor 7: {freq_7} vezes\n"
      f"Porcentagem do valor 7: {freq_7 / total_jogadas * 100:.2f}%\n"
      f"Porcentagem esperada para o valor 7: {(1/6) * 100:.2f}%")