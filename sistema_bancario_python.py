# Constantes para as opções do menu
OPCAO_DEPOSITAR = '1'
OPCAO_SACAR = '2'
OPCAO_EXTRATO = '3'
OPCAO_SAIR = '4'

# Mensagem do menu
menu = f"""
[{OPCAO_DEPOSITAR}] Depositar
[{OPCAO_SACAR}] Sacar
[{OPCAO_EXTRATO}] Extrato
[{OPCAO_SAIR}] Sair

=> """

# Inicialização das variáveis
saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, extrato
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"

def sacar(valor):
    global saldo, extrato, numero_saques
    if valor > saldo:
        print("Você não tem saldo suficiente.")
    elif valor > limite_saque:
        print("O valor do saque excede o limite. Tente solicitar um valor de saque menor.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Número máximo de saques excedido. Você não pode realizar mais saques até amanhã.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

def mostrar_extrato():
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============FIM DO EXTRATO================")

# Loop principal do programa
while True:
    opcao = input(menu).lower()

    if opcao == OPCAO_DEPOSITAR:
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            depositar(valor)
        else:
            print("O valor informado é inválido. Informe um valor válido.")

    elif opcao == OPCAO_SACAR:
        valor = float(input("Informe o valor a ser sacado: "))
        if valor > 0:
            sacar(valor)
        else:
            print("O valor informado é inválido. Informe um valor válido.")

    elif opcao == OPCAO_EXTRATO:
        mostrar_extrato()

    elif opcao == OPCAO_SAIR:
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida.")
