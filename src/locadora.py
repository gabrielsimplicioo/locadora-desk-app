from src.veiculo import Carro, Moto, Caminhao, Veiculo
from src.cliente import Cliente
from src.aluguel import Aluguel
from src.servico_multa import ServicoConsultaMulta
from src.banco import Banco
from src.veiculo_repositorio import VeiculoRepositorio
from src.cliente_repositorio import ClienteRepositorio
from src.aluguel_repositorio import AluguelRepositorio


class Locadora:
    def __init__(self):
        banco = Banco()
        self.veiculo_repositorio = VeiculoRepositorio(banco)
        self.cliente_repositorio = ClienteRepositorio(banco)
        self.aluguel_repositorio = AluguelRepositorio(
            banco, self.veiculo_repositorio, self.cliente_repositorio)
        self.servico_multa = ServicoConsultaMulta()

        self.veiculos: list[Veiculo] = self.veiculo_repositorio.listar()
        self.clientes: list[Cliente] = self.cliente_repositorio.listar()
        self.alugueis: list[Aluguel] = self.aluguel_repositorio.listar()

    def cadastrar_carro(self, placa, marca, modelo, ano, valor_diaria,
                         potencia_cv, combustivel, num_portas) -> Carro:
        carro = Carro(placa, marca, modelo, ano, valor_diaria,
                       potencia_cv, combustivel, num_portas)
        self.veiculo_repositorio.salvar(carro)
        self.veiculos.append(carro)
        return carro

    def cadastrar_moto(self, placa, marca, modelo, ano, valor_diaria,
                        potencia_cv, combustivel, cilindrada) -> Moto:
        moto = Moto(placa, marca, modelo, ano, valor_diaria,
                     potencia_cv, combustivel, cilindrada)
        self.veiculo_repositorio.salvar(moto)
        self.veiculos.append(moto)
        return moto

    def cadastrar_caminhao(self, placa, marca, modelo, ano, valor_diaria,
                            potencia_cv, combustivel,
                            capacidade_carga_toneladas) -> Caminhao:
        caminhao = Caminhao(placa, marca, modelo, ano, valor_diaria,
                             potencia_cv, combustivel,
                             capacidade_carga_toneladas)
        self.veiculo_repositorio.salvar(caminhao)
        self.veiculos.append(caminhao)
        return caminhao

    def cadastrar_cliente(self, nome, cpf, telefone) -> Cliente:
        cliente = Cliente(nome, cpf, telefone)
        self.cliente_repositorio.salvar(cliente)
        self.clientes.append(cliente)
        return cliente

    def registrar_aluguel(self, cliente: Cliente, veiculo: Veiculo,
                           dias: int) -> Aluguel:
        aluguel = Aluguel(cliente, veiculo, dias)
        self.aluguel_repositorio.salvar(aluguel)
        self.alugueis.append(aluguel)
        return aluguel

    def consultar_multas(self, veiculo: Veiculo) -> list[str]:
        return self.servico_multa.consultar_multas(veiculo)
