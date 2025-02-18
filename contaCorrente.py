class ContaCorrente:
    def __init__(self, nome, cpf, numeroDaConta, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numeroDaConta = numeroDaConta
        self.saldo = saldo

saldo = 0

def cadastrarCliente():
   nome = input("Nome do cliente: ")
   cpf = input("CPF: ")
   numeroDaConta = input("Digite o número da conta")
   saldo = 0
   return nome, cpf, numeroDaConta, saldo


def depositarConta(saldo):
    valor = float(input("Digite o valor a ser depositado: "))
    saldo += valor
    return f"Deposito concluído com sucesso! saldo atual:R${saldo}"

def sacarConta(saldo):
    valor = float(input("Digite o valor a ser sacado: "))
    if saldo >= valor:
       saldo -= valor
       print(f"Saque no valor de R${valor} foi concluído com sucesso!")
       print(f"O seu saldo atual é R${saldo}")
    else:
        print(f"Você não tem saldo o suficiente para sacar. O seu saldo atual é de R${saldo}")




