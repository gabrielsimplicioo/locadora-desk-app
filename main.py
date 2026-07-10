from src.veiculo import Carro, Moto, Caminhao
from src.cliente import Cliente
from src.aluguel import Aluguel
from src.servico_multa import ServicoConsultaMulta


def main():
    print("=== Locadora de Veículos - Nível 1 (modelagem POO) ===\n")

    carro = Carro("ABC1D23", "Fiat", "Argo", 2023, 120.0,
                   95, "Flex", num_portas=4)
    moto = Moto("XYZ9E87", "Honda", "CG 160", 2022, 60.0,
                16, "Flex", cilindrada=160)
    caminhao = Caminhao("QWE4F56", "Volvo", "FH 540", 2021, 400.0,
                         540, "Diesel", capacidade_carga_toneladas=10)

    veiculos = [carro, moto, caminhao]

    print("-- Herança e Composição --")
    for v in veiculos:
        print(v)  # cada Veiculo mostra seu Motor (composição) no __str__
    print()

    print("-- Polimorfismo: calcular_aluguel(dias) muda por tipo --")
    for v in veiculos:
        print(f"{v.__class__.__name__}: R$ {v.calcular_aluguel(dias=5):.2f} por 5 dias")
    print()

    print("-- Associação: Cliente x Veiculo via Aluguel --")
    cliente1 = Cliente("Gabriel Simplicio", "111.222.333-44", "(11) 91234-5678")
    cliente2 = Cliente("Maria Souza", "555.666.777-88", "(11) 98765-4321")

    aluguel1 = Aluguel(cliente1, carro, dias=3)
    aluguel2 = Aluguel(cliente2, caminhao, dias=7)
    for aluguel in (aluguel1, aluguel2):
        print(aluguel)
    print()

    print("-- Dependência: ServicoConsultaMulta usa Veiculo sem possuí-lo --")
    servico = ServicoConsultaMulta()
    for v in veiculos:
        servico.consultar_multas(v)


if __name__ == "__main__":
    main()
