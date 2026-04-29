from db import get_connection
from datetime import datetime

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
            preco_compra = float(input("Digite o valor da compra: "))
            data_compra = datetime.strptime(input("Digite a data (dd/mm/aaaa): "), "%d/%m/%Y").date().isoformat()
            categoria_compra = input("Digite a categoria da compra: ")
            conn = get_connection() 
            cursor = conn.cursor()
            query = "INSERT INTO cadastro_gastos (nome_compra, preco_compra, data_compra, categoria_compra) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nome_compra, preco_compra, data_compra, categoria_compra))
            conn.commit()
            print("Gasto adicionado com sucesso!")

        elif opc == 2:
            print("Exibindo gastos...")
            query = "SELECT * FROM cadastro_gastos"
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            gastos = cursor.fetchall()
            for gasto in gastos:
                print(f"ID: {gasto[0]}, Nome da Compra: {gasto[1]}, Valor: {gasto[2]}, Data: {gasto[3]}, Categoria: {gasto[4]}")
        elif opc == 3:
            print("Exibindo total de gastos...")
            query = "SELECT SUM(preco_compra) FROM cadastro_gastos"
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            total = cursor.fetchone()[0]
            print(f"Total de gastos: {total}")

        elif opc == 4:
            print("Saindo do programa...")

        if opc != 1 and opc != 2 and opc != 3 and opc != 4:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()
