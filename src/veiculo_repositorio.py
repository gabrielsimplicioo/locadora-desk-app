from src.veiculo import Carro, Moto, Caminhao


class VeiculoRepositorio:
    def __init__(self, banco):
        self.conexao = banco.conexao

    def salvar(self, veiculo):
        num_portas = getattr(veiculo, "num_portas", None)
        cilindrada = getattr(veiculo, "cilindrada", None)
        capacidade_carga_toneladas = getattr(
            veiculo, "capacidade_carga_toneladas", None)

        cursor = self.conexao.execute(
            """INSERT INTO veiculos
               (tipo, placa, marca, modelo, ano, valor_diaria, potencia_cv,
                combustivel, num_portas, cilindrada, capacidade_carga_toneladas)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (veiculo.__class__.__name__, veiculo.placa, veiculo.marca,
             veiculo.modelo, veiculo.ano, veiculo.valor_diaria,
             veiculo.motor.potencia_cv, veiculo.motor.combustivel,
             num_portas, cilindrada, capacidade_carga_toneladas))
        self.conexao.commit()
        veiculo.id = cursor.lastrowid
        return veiculo

    def listar(self):
        linhas = self.conexao.execute("SELECT * FROM veiculos").fetchall()
        return [self._para_veiculo(linha) for linha in linhas]

    def buscar_por_id(self, id):
        linha = self.conexao.execute(
            "SELECT * FROM veiculos WHERE id = ?", (id,)).fetchone()
        return self._para_veiculo(linha) if linha else None

    def _para_veiculo(self, linha):
        (id, tipo, placa, marca, modelo, ano, valor_diaria, potencia_cv,
         combustivel, num_portas, cilindrada, capacidade_carga_toneladas) = linha

        if tipo == "Carro":
            veiculo = Carro(placa, marca, modelo, ano, valor_diaria,
                             potencia_cv, combustivel, num_portas)
        elif tipo == "Moto":
            veiculo = Moto(placa, marca, modelo, ano, valor_diaria,
                            potencia_cv, combustivel, cilindrada)
        else:
            veiculo = Caminhao(placa, marca, modelo, ano, valor_diaria,
                                potencia_cv, combustivel,
                                capacidade_carga_toneladas)
        veiculo.id = id
        return veiculo
