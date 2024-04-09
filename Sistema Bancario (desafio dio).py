menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
cheque_especial=1000
saldo_cheque_especial=1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if (saldo >=0) and (saldo_cheque_especial == cheque_especial):
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        elif valor <= (cheque_especial-saldo_cheque_especial):
            saldo_cheque_especial+=valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        elif valor > (cheque_especial-saldo_cheque_especial): 
            valor-=(cheque_especial-saldo_cheque_especial)
            saldo_cheque_especial=cheque_especial
            saldo+=valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo+saldo_cheque_especial

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            if valor <= saldo:
               saldo -= valor   
            elif valor > saldo:
                saldo_cheque_especial-=(valor-saldo)
                saldo=0
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo + Cheque Especial: R$ {saldo+saldo_cheque_especial:.2f}")
        print(f"\nVoce usou: R$ {-saldo_cheque_especial+cheque_especial:.2f} do cheque especial")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")