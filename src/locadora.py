from src.veiculo import Carro, Moto, Caminhao, Veiculo
from src.cliente import Cliente
from src.aluguel import Aluguel
from src.servico_multa import ServicoConsultaMulta


class Locadora:
    def __init__(self):
        self.veiculos: list[Veiculo] = []
        self.clientes: list[Cliente] = []
        self.alugueis: list[Aluguel] = []
        self.servico_multa = ServicoConsultaMulta()

    def cadastrar_carro(self, placa, marca, modelo, ano, valor_diaria,
                         potencia_cv, combustivel, num_portas) -> Carro:
        carro = Carro(placa, marca, modelo, ano, valor_diaria,
                       potencia_cv, combustivel, num_portas)
        self.veiculos.append(carro)
        return carro

    def cadastrar_moto(self, placa, marca, modelo, ano, valor_diaria,
                        potencia_cv, combustivel, cilindrada) -> Moto:
        moto = Moto(placa, marca, modelo, ano, valor_diaria,
                     potencia_cv, combustivel, cilindrada)
        self.veiculos.append(moto)
        return moto

    def cadastrar_caminhao(self, placa, marca, modelo, ano, valor_diaria,
                            potencia_cv, combustivel,
                            capacidade_carga_toneladas) -> Caminhao:
        caminhao = Caminhao(placa, marca, modelo, ano, valor_diaria,
                             potencia_cv, combustivel,
                             capacidade_carga_toneladas)
        self.veiculos.append(caminhao)
        return caminhao

    def cadastrar_cliente(self, nome, cpf, telefone) -> Cliente:
        cliente = Cliente(nome, cpf, telefone)
        self.clientes.append(cliente)
        return cliente

    def registrar_aluguel(self, cliente: Cliente, veiculo: Veiculo,
                           dias: int) -> Aluguel:
        aluguel = Aluguel(cliente, veiculo, dias)
        self.alugueis.append(aluguel)
        return aluguel

    def consultar_multas(self, veiculo: Veiculo) -> list[str]:
        return self.servico_multa.consultar_multas(veiculo)
