from db import get_connection
from datetime import datetime
    
def menu():
    opc = 0
    while opc != 1 and opc != 2 and opc != 3 and opc != 4:

        print(''''
          1-Adicionar gasto
          2-Ver gastos
          3-Ver total de gastos 
          4-Apagar gastos
          5-Atualizar gastos
          6-Sair
          
          
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
            print("Pressione ENTER para voltar ao menu...")
            enter = input()
            if enter == "":
                menu()

        elif opc == 2:
            print("Exibindo gastos...")
            query = "SELECT * FROM cadastro_gastos"
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            gastos = cursor.fetchall()
            for gasto in gastos:
                print(f"ID: {gasto[0]}, Nome da Compra: {gasto[1]}, Valor: {gasto[2]}, Data: {gasto[3]}, Categoria: {gasto[4]}")
            print("Pressione ENTER para voltar ao menu...")
            enter = input()
            if enter == "":
                menu()


        elif opc == 3:
            limite = float(input("Qual é o seu limite de gastos para esse mês? : "))
            print("Exibindo total de gastos...")
            query = "SELECT SUM(preco_compra) FROM cadastro_gastos"
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            total = cursor.fetchone()[0]
            print(f"Total de gastos: {total}")
            restante = limite - float(total)
            if restante > 0:
                print(f"Você ainda pode gastar R${restante:.2f} para atingir o seu limite.")
            elif restante < 0:
                print(f"Você ultrapassou seu limite em R${-restante:.2f}.")
            print("Pressione ENTER para voltar ao menu...")
            enter = input()
            if enter == "":
                menu()

        elif opc == 4:
            query = "SELECT * FROM cadastro_gastos"
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            gastos = cursor.fetchall()
            for gasto in gastos:
                print(f"ID: {gasto[0]}, Nome da Compra: {gasto[1]}, Valor: {gasto[2]}, Data: {gasto[3]}, Categoria: {gasto[4]}")
            print("Digite o ID do gasto que deseja apagar: ")
            id_compra = int(input())
            query = "DELETE FROM cadastro_gastos WHERE id_compra = %s"
            cursor.execute(query, (id_compra,))
            conn.commit()
            print("Gasto apagado com sucesso!")
            print("Pressione ENTER para voltar ao menu...")
            enter = input()
            if enter == "":
                menu()
            
        elif opc == 5:
            query = "SELECT * FROM cadastro_gastos"
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            gastos = cursor.fetchall()
            for gasto in gastos:
                print(f"ID: {gasto[0]}, Nome da Compra: {gasto[1]}, Valor: {gasto[2]}, Data: {gasto[3]}, Categoria: {gasto[4]}")
            print("Digite o ID do gasto que deseja atualizar: ")
            id_compra = int(input())
            nome_compra = input("Digite o novo nome da compra: ")
            preco_compra = float(input("Digite o novo valor da compra: "))
            data_compra = datetime.strptime(input("Digite a nova data (dd/mm/aaaa): "), "%d/%m/%Y").date().isoformat()
            categoria_compra = input("Digite a nova categoria da compra: ")
            query = "UPDATE cadastro_gastos SET nome_compra = %s, preco_compra = %s, data_compra = %s, categoria_compra = %s WHERE id_compra = %s"
            cursor.execute(query, (nome_compra, preco_compra, data_compra, categoria_compra, id_compra))
            conn.commit()
            print("Gasto atualizado com sucesso!")
            print("Pressione ENTER para voltar ao menu...")
            enter = input()
            if enter == "":
                menu()

        elif opc == 6:
            print("Saindo do programa...")

        if opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5 and opc != 6:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()
