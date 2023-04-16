menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[m] Menu

=> """

info_menu = """

Você possui até 3 saques diários, para consultar quantos ainda restam por favor verifique o seu extrato.
Você pode sacar até R$ 500 por saque.

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_DINHEIRO_SAQUE = 500

while True:

    opcao = input(menu)


    if opcao == "d":
        deposito = float(input("Qual valor será depositado? "))
        if deposito > 0:
            saldo += float(deposito)
            extrato = extrato + "\n" + f"Deposito de R$ {deposito} realizado com sucesso!"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação não realizada, por favor confirme o valor informado!")


    elif opcao == "s":
        saque = float(input("Qual valor será sacado? "))
        if saldo > 0 and saque <= LIMITE_DINHEIRO_SAQUE and saque <= saldo:
            if numero_saques < LIMITE_SAQUES:
                extrato = extrato + "\n" + f"Saque de R$ {saque} realizado com sucesso!"
                print("Saque realizado com sucesso!")
                numero_saques += 1
                saldo = saldo - saque
            else:
                print("Seu limite de saque diário foi excedido, em casos de dúvidas por favor consultar a opção 'm' no menu.")
        else:
            print("Operação não realizada, por favor, tente novamente, em casos de dúvidas por favor consultar a opção 'm' no menu.")


    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações.")

        if LIMITE_SAQUES - numero_saques > 0:
            print(f"Sua movimentação bancária foi: {extrato} \nVoce ainda possui {LIMITE_SAQUES - numero_saques} saques.\nSeu saldo é de R$ {saldo}")
        else:
            print(f"Sua movimentação bancária foi: {extrato}\nVocê não possui mais saques diários.\nSeu saldo é de R$ {saldo}")

    elif opcao == "q":
        print("Saindo do programa... Obrigado por usar o nosso sistema")
        break
    
    elif opcao == "m":
        print(info_menu)

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")