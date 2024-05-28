ano_de_nascimento=int(input(f"Em que ano você nasceu?\n"))
ano_atual=int(input(f"Em que ano estamos?\n"))
idade_anos=ano_atual-ano_de_nascimento
idade_meses=idade_anos*12
idade_semanas=idade_anos*52
idade_dia=idade_anos*365
print(f"Você nasceu em {ano_de_nascimento}.\nVocê tem {idade_anos} anos de vida;")
print(f"Você tem {idade_meses} meses de vida;\nVocê tem {idade_semanas} semanas de vida;")
print(f"Você tem {idade_dia} dias de vida.\nData atual: {ano_atual}")