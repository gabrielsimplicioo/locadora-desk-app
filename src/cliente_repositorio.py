from src.cliente import Cliente


class ClienteRepositorio:
    def __init__(self, banco):
        self.conexao = banco.conexao

    def salvar(self, cliente):
        cursor = self.conexao.execute(
            "INSERT INTO clientes (nome, cpf, telefone) VALUES (?, ?, ?)",
            (cliente.nome, cliente.cpf, cliente.telefone))
        self.conexao.commit()
        cliente.id = cursor.lastrowid
        return cliente

    def listar(self):
        linhas = self.conexao.execute("SELECT * FROM clientes").fetchall()
        return [self._para_cliente(linha) for linha in linhas]

    def buscar_por_id(self, id):
        linha = self.conexao.execute(
            "SELECT * FROM clientes WHERE id = ?", (id,)).fetchone()
        return self._para_cliente(linha) if linha else None

    def _para_cliente(self, linha):
        id, nome, cpf, telefone = linha
        cliente = Cliente(nome, cpf, telefone)
        cliente.id = id
        return cliente
