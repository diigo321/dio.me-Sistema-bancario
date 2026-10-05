"""Desafio DIO: sistema bancário de uma conta, com dados em memória."""
from decimal import Decimal, InvalidOperation


def ler_valor(mensagem):
    try:
        valor = Decimal(input(mensagem).strip().replace(",", "."))
        if not valor.is_finite() or valor <= 0 or valor != valor.quantize(Decimal("0.01")):
            raise ValueError
        return valor
    except (InvalidOperation, ValueError):
        print("Valor inválido. Informe um número positivo com até duas casas decimais.")
        return None


def main():
    saldo = Decimal("0.00")
    limite = Decimal("500.00")
    limite_saques = 3
    numero_saques = 0
    extrato = []
    menu = "\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> "

    while True:
        opcao = input(menu).strip().lower()
        if opcao == "d":
            valor = ler_valor("Valor do depósito: R$ ")
            if valor is not None:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print("Depósito realizado.")
        elif opcao == "s":
            valor = ler_valor("Valor do saque: R$ ")
            if valor is None:
                continue
            if valor > saldo:
                print("Saldo insuficiente.")
            elif valor > limite:
                print("O limite por saque é R$ 500.00.")
            elif numero_saques >= limite_saques:
                print("Limite de 3 saques atingido.")
            else:
                saldo -= valor
                numero_saques += 1
                extrato.append(f"Saque: R$ {valor:.2f}")
                print("Saque realizado.")
        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("\n".join(extrato) if extrato else "Não foram realizadas movimentações.")
            print(f"Saldo: R$ {saldo:.2f}")
            print("=========================================")
        elif opcao == "q":
            print("Até logo!")
            break
        else:
            print("Operação inválida. Escolha d, s, e ou q.")


if __name__ == "__main__":
    main()
