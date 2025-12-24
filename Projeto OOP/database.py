import sqlite3

def conectar_db(nome_db="hotel.db"):
    conexao = sqlite3.connect(nome_db)
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quartos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER NOT NULL UNIQUE,
            tipo TEXT NOT NULL,
            diaria REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            quarto_id INTEGER NOT NULL,
            checkin TEXT NOT NULL,
            checkout TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (quarto_id) REFERENCES quartos(id)
        )
    """)

    conexao.commit()

def inserir_cliente(conexao, nome, telefone, email):
    """Insere um cliente no banco de dados."""
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO clientes (nome, telefone, email)
        VALUES (?, ?, ?)
    """, (nome, telefone, email))
    conexao.commit()
    return cursor.lastrowid

def inserir_quarto(conexao, numero, tipo, diaria, status):
    """Insere um quarto no banco de dados."""
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO quartos (numero, tipo, diaria, status)
        VALUES (?, ?, ?, ?)
    """, (numero, tipo, diaria, status))
    conexao.commit()
    return cursor.lastrowid

def inserir_reserva(conexao, cliente_id, quarto_numero, checkin, checkout, status):
    """Insere uma reserva no banco de dados."""
    cursor = conexao.cursor()
    # Busca o quarto pelo número
    cursor.execute("SELECT id FROM quartos WHERE numero = ?", (quarto_numero,))
    quarto = cursor.fetchone()
    if not quarto:
        raise ValueError(f"Quarto {quarto_numero} não encontrado no banco de dados")
    
    quarto_id = quarto[0]
    cursor.execute("""
        INSERT INTO reservas (cliente_id, quarto_id, checkin, checkout, status)
        VALUES (?, ?, ?, ?, ?)
    """, (cliente_id, quarto_id, checkin, checkout, status))
    conexao.commit()
    return cursor.lastrowid

def buscar_todos_clientes(conexao):
    """Retorna todos os clientes do banco de dados."""
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, telefone, email FROM clientes")
    return cursor.fetchall()

def buscar_todos_quartos(conexao):
    """Retorna todos os quartos do banco de dados."""
    cursor = conexao.cursor()
    cursor.execute("SELECT id, numero, tipo, diaria, status FROM quartos")
    return cursor.fetchall()

def buscar_todas_reservas(conexao):
    """Retorna todas as reservas do banco de dados."""
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT r.id, c.nome, q.numero, r.checkin, r.checkout, r.status
        FROM reservas r
        JOIN clientes c ON r.cliente_id = c.id
        JOIN quartos q ON r.quarto_id = q.id
    """)
    return cursor.fetchall()

def atualizar_cliente(conexao, cliente_id, nome=None, telefone=None, email=None):
    """Atualiza dados de um cliente."""
    cursor = conexao.cursor()
    if nome:
        cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", (nome, cliente_id))
    if telefone:
        cursor.execute("UPDATE clientes SET telefone = ? WHERE id = ?", (telefone, cliente_id))
    if email:
        cursor.execute("UPDATE clientes SET email = ? WHERE id = ?", (email, cliente_id))
    conexao.commit()

def atualizar_quarto(conexao, quarto_numero, tipo=None, diaria=None, status=None):
    """Atualiza dados de um quarto."""
    cursor = conexao.cursor()
    if tipo:
        cursor.execute("UPDATE quartos SET tipo = ? WHERE numero = ?", (tipo, quarto_numero))
    if diaria:
        cursor.execute("UPDATE quartos SET diaria = ? WHERE numero = ?", (diaria, quarto_numero))
    if status:
        cursor.execute("UPDATE quartos SET status = ? WHERE numero = ?", (status, quarto_numero))
    conexao.commit()

def atualizar_reserva(conexao, reserva_id, checkin=None, checkout=None, status=None):
    """Atualiza dados de uma reserva."""
    cursor = conexao.cursor()
    if checkin:
        cursor.execute("UPDATE reservas SET checkin = ? WHERE id = ?", (checkin, reserva_id))
    if checkout:
        cursor.execute("UPDATE reservas SET checkout = ? WHERE id = ?", (checkout, reserva_id))
    if status:
        cursor.execute("UPDATE reservas SET status = ? WHERE id = ?", (status, reserva_id))
    conexao.commit()

def excluir_cliente(conexao, cliente_id):
    """Exclui um cliente do banco de dados."""
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
    conexao.commit()

def excluir_quarto(conexao, quarto_numero):
    """Exclui um quarto do banco de dados."""
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM quartos WHERE numero = ?", (quarto_numero,))
    conexao.commit()

def excluir_reserva(conexao, reserva_id):
    """Exclui uma reserva do banco de dados."""
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
    conexao.commit()

def testar_conexao():
    try:
        conexao = conectar_db()
        criar_tabelas(conexao)
        print("Conexão com o banco de dados estabelecida e tabelas criadas com sucesso.")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        if conexao:
            conexao.close() 

if __name__ == "__main__":
    testar_conexao()