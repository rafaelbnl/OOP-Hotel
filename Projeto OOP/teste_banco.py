"""
Script de teste para verificar integração com banco de dados.
Mostra os dados salvos nas tabelas do hotel.db
"""
import database as db

def exibir_dados():
    print("\n" + "="*60)
    print("DADOS ARMAZENADOS NO BANCO DE DADOS hotel.db")
    print("="*60)
    
    conexao = db.conectar_db()
    
    # Exibir clientes
    print("\n📋 CLIENTES:")
    print("-" * 60)
    clientes = db.buscar_todos_clientes(conexao)
    if clientes:
        for cliente in clientes:
            id_cli, nome, telefone, email = cliente
            print(f"ID: {id_cli} | Nome: {nome} | Tel: {telefone} | Email: {email}")
    else:
        print("Nenhum cliente cadastrado no banco de dados.")
    
    # Exibir quartos
    print("\n🏨 QUARTOS:")
    print("-" * 60)
    quartos = db.buscar_todos_quartos(conexao)
    if quartos:
        for quarto in quartos:
            id_q, numero, tipo, diaria, status = quarto
            print(f"ID: {id_q} | Nº: {numero} | Tipo: {tipo} | Diária: R${diaria:.2f} | Status: {status}")
    else:
        print("Nenhum quarto cadastrado no banco de dados.")
    
    # Exibir reservas
    print("\n📅 RESERVAS:")
    print("-" * 60)
    reservas = db.buscar_todas_reservas(conexao)
    if reservas:
        for reserva in reservas:
            id_r, nome_cliente, numero_quarto, checkin, checkout, status = reserva
            print(f"ID: {id_r} | Cliente: {nome_cliente} | Quarto: {numero_quarto}")
            print(f"   Check-in: {checkin} | Check-out: {checkout} | Status: {status}")
    else:
        print("Nenhuma reserva cadastrada no banco de dados.")
    
    conexao.close()
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    exibir_dados()
