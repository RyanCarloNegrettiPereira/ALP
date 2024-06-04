from cpf import valida_cpf
from data import valida_data
from menu import exibir_menu
import random
def cadastrar():
    nome=input("Digite o nome: ")
    sobrenome=input("Digite o sobrenome: ")
    cpf=input("Digite o CPF (no formato 999.999.999-99): ")
    if not valida_cpf(cpf):
        print("CPF inválido.")
        return
    data_nascimento=input("Digite a data de nascimento (no formato dd/mm/aaaa): ")
    if not valida_data(data_nascimento):
        print("Data de nascimento inválida ou usuário menor de 18 anos.")
        return
    renda_bruta=float(input("Digite a renda bruta: "))
def exibir_mensagem():
    mensagens=[
        "A persistência realiza o impossível",
        "Seus sonhos não precisam de plateia, eles só precisam de você",
        "A persistência é o caminho do êxito",
        "No meio da dificuldade encontra-se a oportunidade"
    ]
    print(random.choice(mensagens))
while True:
    opcao=exibir_menu()
    if opcao==1:
        cadastrar()
    elif opcao==2:
        exibir_mensagem()
    elif opcao==3:
        print("Bye bye!")
        break