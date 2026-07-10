from src.aluguel import Aluguel


class AluguelRepositorio:
    def __init__(self, banco, veiculo_repositorio, cliente_repositorio):
        self.conexao = banco.conexao
        self.veiculo_repositorio = veiculo_repositorio
        self.cliente_repositorio = cliente_repositorio

    def salvar(self, aluguel):
        cursor = self.conexao.execute(
            "INSERT INTO alugueis (cliente_id, veiculo_id, dias) VALUES (?, ?, ?)",
            (aluguel.cliente.id, aluguel.veiculo.id, aluguel.dias))
        self.conexao.commit()
        aluguel.id = cursor.lastrowid
        return aluguel

    def listar(self):
        linhas = self.conexao.execute("SELECT * FROM alugueis").fetchall()
        return [self._para_aluguel(linha) for linha in linhas]

    def _para_aluguel(self, linha):
        id, cliente_id, veiculo_id, dias = linha
        cliente = self.cliente_repositorio.buscar_por_id(cliente_id)
        veiculo = self.veiculo_repositorio.buscar_por_id(veiculo_id)
        aluguel = Aluguel(cliente, veiculo, dias)
        aluguel.id = id
        return aluguel
