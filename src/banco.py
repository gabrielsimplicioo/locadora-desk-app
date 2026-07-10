import sqlite3

CAMINHO_BANCO = "locadora.db"


class Banco:
    def __init__(self, caminho: str = CAMINHO_BANCO):
        self.conexao = sqlite3.connect(caminho)
        self.conexao.execute("PRAGMA foreign_keys = ON")
        self._criar_tabelas()

    def _criar_tabelas(self):
        self.conexao.execute("""
            CREATE TABLE IF NOT EXISTS veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                placa TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                ano INTEGER NOT NULL,
                valor_diaria REAL NOT NULL,
                potencia_cv REAL NOT NULL,
                combustivel TEXT NOT NULL,
                num_portas INTEGER,
                cilindrada INTEGER,
                capacidade_carga_toneladas REAL
            )
        """)
        self.conexao.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """)
        self.conexao.execute("""
            CREATE TABLE IF NOT EXISTS alugueis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                veiculo_id INTEGER NOT NULL,
                dias INTEGER NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
            )
        """)
        self.conexao.commit()
