from db import get_connection

def menu():
    opc = 0
    while opc != 1 and opc != 2 and opc != 3 and opc != 4:

        print(''''
          1-Adicionar gasto
          2-Ver gastos
          3-Ver total de gastos 
          4-Sair 
          
          
          '''
                )
        opc = int(input('Digite a opção desejada: '))
        if opc == 1:
            nome_compra = input("Digite o nome da compra: ")
            gasto = float(input("Digite o valor da compra: "))
            data = input("Digite a data da compra (dd/mm/aaaa): ")
            categoria = input("Digite a categoria da compra: ")
            print("Gasto adicionado com sucesso!")

        elif opc == 2:
            print("Exibindo gastos...")

        elif opc == 3:
            print("Exibindo total de gastos...")

        elif opc == 4:
            print("Saindo do programa...")

        if opc != 1 and opc != 2 and opc != 3 and opc != 4:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()
