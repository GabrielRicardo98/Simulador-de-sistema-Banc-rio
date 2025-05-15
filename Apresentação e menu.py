saldo = 0.0  # Saldo inicial (você pode alterar este valor)
opcao = 0

print("Olá! Bem-vindo ao seu banco virtual.")
print("--------------------------------------")
print("1 - Consultar Saldo")
print("2 - Depositar")
print("3 - Sacar")
print("4 - Sair")
print("--------------------------------------")

opcao_str = input("Digite a opção desejada: ")

while not opcao_str.isdigit() or not (1 <= int(opcao_str) <= 4):
    print("Opção inválida. Por favor, digite um número entre 1 e 4.")
    opcao_str = input("Digite a opção desejada: ")

opcao = int(opcao_str)

if opcao == 1:
    print(f"Seu saldo atual é: R$ {saldo:.2f}")
elif opcao == 2:
    valor_deposito = float(input("Digite o valor a depositar: R$ "))
    saldo += valor_deposito
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    print(f"Seu novo saldo é: R$ {saldo:.2f}")
elif opcao == 3:
    valor_saque = float(input("Digite o valor a sacar: R$ "))
    if valor_saque <= saldo:
        saldo -= valor_saque
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        print(f"Seu novo saldo é: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente.")
elif opcao == 4:
    print("Obrigado por utilizar nosso banco virtual!")