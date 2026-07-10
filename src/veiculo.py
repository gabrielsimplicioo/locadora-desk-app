from abc import ABC, abstractmethod

from src.motor import Motor


class Veiculo(ABC):
    """Classe base. A composição com Motor vive aqui: o Motor é criado
    dentro do próprio Veiculo e não existe fora dele (se o Veiculo for
    destruído, o Motor vai junto)."""

    def __init__(self, placa: str, marca: str, modelo: str, ano: int,
                 valor_diaria: float, potencia_cv: float, combustivel: str):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.motor = Motor(potencia_cv, combustivel)

    @abstractmethod
    def calcular_aluguel(self, dias: int) -> float:
        """Cada subclasse define sua própria regra de cobrança (polimorfismo)."""
        raise NotImplementedError

    def __str__(self):
        return (f"{self.__class__.__name__} {self.marca} {self.modelo} "
                f"({self.ano}) - placa {self.placa} - {self.motor}")


class Carro(Veiculo):
    def __init__(self, placa, marca, modelo, ano, valor_diaria,
                 potencia_cv, combustivel, num_portas: int):
        super().__init__(placa, marca, modelo, ano, valor_diaria,
                          potencia_cv, combustivel)
        self.num_portas = num_portas

    def calcular_aluguel(self, dias: int) -> float:
        return self.valor_diaria * dias


class Moto(Veiculo):
    def __init__(self, placa, marca, modelo, ano, valor_diaria,
                 potencia_cv, combustivel, cilindrada: int):
        super().__init__(placa, marca, modelo, ano, valor_diaria,
                          potencia_cv, combustivel)
        self.cilindrada = cilindrada

    def calcular_aluguel(self, dias: int) -> float:
        return self.valor_diaria * dias * 0.8


class Caminhao(Veiculo):
    TAXA_POR_TONELADA = 15.0

    def __init__(self, placa, marca, modelo, ano, valor_diaria,
                 potencia_cv, combustivel, capacidade_carga_toneladas: float):
        super().__init__(placa, marca, modelo, ano, valor_diaria,
                          potencia_cv, combustivel)
        self.capacidade_carga_toneladas = capacidade_carga_toneladas

    def calcular_aluguel(self, dias: int) -> float:
        taxa_carga = self.capacidade_carga_toneladas * self.TAXA_POR_TONELADA
        return (self.valor_diaria * dias) + taxa_carga
