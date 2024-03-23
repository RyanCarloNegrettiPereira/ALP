altura_degrau=float(input(f"Quantos centímetros tem cada degrau da escada?\n"))
altura=float(input(f"Quantos metros você deseja subir?\n"))
degraus=(altura*100)/altura_degrau
print(f"Você deverá subir {degraus} degraus.")