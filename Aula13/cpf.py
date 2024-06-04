# valida_cpf.py

def valida_cpf(cpf):
    cpf=[int(digito) for digito in cpf if digito.isdigit()]
    if len(cpf)!=11:
        return False
    soma=sum([cpf[i] * (10 - i) for i in range(9)])
    resto=soma%11
    if resto<2:
        digito1=0
    else:
        digito1=11-resto
    if cpf[9]!=digito1:
        return False
    soma=sum([cpf[i]*(11-i) for i in range(10)])
    resto=soma%11
    if resto<2:
        digito2=0
    else:
        digito2=11-resto
    if cpf[10] != digito2:
        return False
    return True