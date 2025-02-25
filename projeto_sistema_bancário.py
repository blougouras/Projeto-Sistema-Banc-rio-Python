from time import sleep

menu = """

=== SISTEMA BANCÁRIO ===

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

Opção => """

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
limiteSaques = 3

while True:

    opc = input(menu)

    if opc == "d":
        valorDeposito = float(input("Digite o valor que deseja depositar: R$ "))

        if valorDeposito > 0:
            saldo += valorDeposito
            extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
            print("Depósito realizado com sucesso.")
            
        else:
            print("Valor muito baixo ou negativo, não foi possível realizar a operação. Tente novamente!")

    elif opc == "s":
        valorSaque = float(input("Digite o valor que deseja ser sacado: R$ "))

        if valorSaque > 0 and numeroSaques < limiteSaques:
            saldo -= valorSaque
            extrato += f"Saque: R$ {valorSaque:.2f}\n"
            numeroSaques += 1
            print("Saque realizado com sucesso")

        elif valorSaque > saldo:
            print("Não foi possível realizar o saque, pois o saldo da conta é insuficiente.")

        elif valorSaque > limite:
            print("Não foi possível realizar o saque, pois o valor do saque é maior que o limite de saque da conta.")

        else:
            print("Limite diário de saques atingindo, não será possível realizar o operação.")


    elif opc == "e":
        print("\n===================== EXTRATO =====================")

        if not extrato:
            print("Não foram realizadas movimentações na conta")
        else:
            print(extrato)
    
        print(f"\nSaldo: R$ {saldo:.2f}")

        print("=====================================================")

    elif opc == "q":
        print("Obrigado por usar o sistema do banco, tenha um bom dia!")
        break

    else:
        print("Operação Inválida, por favor selecione novamente a opção desejada!")