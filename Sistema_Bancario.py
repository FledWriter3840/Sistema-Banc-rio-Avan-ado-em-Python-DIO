def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Saldo
    [5] Criar Conta Bancaria
    [6] Criar Cliente
    [7] Contas Cadastradas
    [8] Sair

    => """

    return input(menu).strip()
    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito realizado com sucesso no valor de R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!"
              f"\nValor sacado: R$ {valor:.2f}"
              f"\nSaldo atual: R$ {saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def saldo(saldo):
    if saldo > 0:
        print(f"\nSaldo: R$ {saldo:.2f} ")
    else:
        print("Você não possui saldo em sua conta bancária.")
    
    return saldo

def exibir_extrato(saldo,/,*, extrato,):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastro_cliente(cliente):  
    cpf = input("Informe o CPF (somente numeros): ")

    for cliente in cliente: 
        if cliente["cpf"] == cpf:
            print("Operação falhou! Ja existe um cliente com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (logradouro, nro - bairro - cidade/sigla estado): ")

    if len(cpf) != 11:
        print("Operação falhou! O CPF informado é inválido.")
        return

    cliente.append ({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Cliente cadastrado com sucesso!")

def filtrar_cliente(cpf, cliente):
    clientes_filtrados = [cliente for cliente in cliente if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def conta_bancaria(AGENCIA, numero_conta, cliente):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, cliente)
    if cliente:
        print("Conta bancária criada com sucesso!")
    return {"agencia": "0001", "numero_conta": numero_conta, "usuario": cliente }    

    print("Operação falhou! Cliente nao encontrado, utilize o comando 6 para cadastrar um novo cliente.")

    return conta

def contas_cadastradas(contas):
    for conta in contas:
        print(conta)

def main():
   
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    cliente = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == "3":
            extrato = exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            saldo = saldo(saldo)
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = conta_bancaria(AGENCIA, numero_conta, cliente)
            if conta:
                contas.append(conta)
        elif opcao == "6":
            cadastro_cliente(cliente)
        elif opcao == "7":
            contas_cadastradas(contas)
        elif opcao == "8":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()