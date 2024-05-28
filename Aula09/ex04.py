from random import randint
frequencia={1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for _ in range(6000):
    resultado=randint(1, 6)
    frequencia[resultado]+=1
for face, freq in frequencia.items():
    print(f"Face {face}: {freq} vezes")