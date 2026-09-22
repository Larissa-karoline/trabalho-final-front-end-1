# Exercício 3 - Simulação de Caixa Eletrônico
saldo = 1000.0  # Saldo inicial 
opcao = 0

while opcao != 4:
    print("-" * 35)
    print("1 - depósito")
    print("2 - saque")
    print("3 - saldo")
    print("4 - sair")
    
    opcao = int(input("opcao : "))
    
    if opcao == 1:
        deposito = float(input("Valor do depósito: "))
        saldo += deposito
    elif opcao == 2:
        saque = float(input("Valor do saque: "))
        saldo -= saque
    elif opcao == 3:
        print(f"Saldo atual: {saldo:.2f}")
    elif opcao == 4:
        print("Fim das transações!")
    else:
        print("Opção inválida!")