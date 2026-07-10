from src.cliente import Cliente
from src.veiculo import Veiculo


class Aluguel:
    """Associação: o Aluguel referencia um Cliente e um Veiculo, mas nenhum
    dos dois pertence a ele nem depende dele para existir."""

    def __init__(self, cliente: Cliente, veiculo: Veiculo, dias: int):
        self.id = None
        self.cliente = cliente
        self.veiculo = veiculo
        self.dias = dias

    def calcular_valor_total(self) -> float:
        return self.veiculo.calcular_aluguel(self.dias)

    def __str__(self):
        total = self.calcular_valor_total()
        return (f"Aluguel: {self.cliente} alugou {self.veiculo} por "
                f"{self.dias} dia(s) - Total: R$ {total:.2f}")
