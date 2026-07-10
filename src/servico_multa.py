from src.veiculo import Veiculo


class ServicoConsultaMulta:
    """Dependência: recebe o Veiculo apenas como parâmetro de método, usa e
    descarta. Não guarda referência nenhuma a ele como atributo."""

    def consultar_multas(self, veiculo: Veiculo) -> list[str]:
        print(f"Consultando multas da placa {veiculo.placa}...")
        return []
