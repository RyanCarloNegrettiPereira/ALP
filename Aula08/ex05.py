string_numerica = input("Digite nove caracteres numéricos: ")
if len(string_numerica)!=9:
    print("A string deve conter exatamente nove caracteres numéricos.")
else:
    parte_inteira=string_numerica[:6]
    parte_decimal=string_numerica[6:]
    string_formatada=parte_inteira[:3]+'.'+parte_inteira[3:]+','+parte_decimal
    print(f"Mostrado: {string_formatada}")