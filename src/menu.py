from src.locadora import Locadora


class Menu:
    def __init__(self):
        self.locadora = Locadora()

    def executar(self):
        acoes = {
            "1": self.cadastrar_veiculo,
            "2": self.listar_veiculos,
            "3": self.cadastrar_cliente,
            "4": self.listar_clientes,
            "5": self.registrar_aluguel,
            "6": self.listar_alugueis,
            "7": self.consultar_multas,
        }

        while True:
            self._imprimir_opcoes()
            escolha = input("Escolha uma opção: ").strip()
            if escolha == "0":
                print("Encerrando...")
                break
            acao = acoes.get(escolha)
            if acao is None:
                print("Opção inválida.\n")
                continue
            acao()
            print()

    def _imprimir_opcoes(self):
        print("=== Locadora de Veículos ===")
        print("1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Cadastrar cliente")
        print("4 - Listar clientes")
        print("5 - Registrar aluguel")
        print("6 - Listar aluguéis")
        print("7 - Consultar multas de um veículo")
        print("0 - Sair")

    def cadastrar_veiculo(self):
        print("Tipo: 1-Carro  2-Moto  3-Caminhão")
        tipo = input("Escolha o tipo: ").strip()

        placa = input("Placa: ").strip()
        marca = input("Marca: ").strip()
        modelo = input("Modelo: ").strip()
        ano = self._pedir_int("Ano: ")
        valor_diaria = self._pedir_float("Valor da diária: ")
        potencia_cv = self._pedir_float("Potência (cv): ")
        combustivel = input("Combustível: ").strip()

        if tipo == "1":
            num_portas = self._pedir_int("Número de portas: ")
            veiculo = self.locadora.cadastrar_carro(
                placa, marca, modelo, ano, valor_diaria,
                potencia_cv, combustivel, num_portas)
        elif tipo == "2":
            cilindrada = self._pedir_int("Cilindrada: ")
            veiculo = self.locadora.cadastrar_moto(
                placa, marca, modelo, ano, valor_diaria,
                potencia_cv, combustivel, cilindrada)
        elif tipo == "3":
            capacidade = self._pedir_float("Capacidade de carga (toneladas): ")
            veiculo = self.locadora.cadastrar_caminhao(
                placa, marca, modelo, ano, valor_diaria,
                potencia_cv, combustivel, capacidade)
        else:
            print("Tipo inválido.")
            return

        print(f"Cadastrado: {veiculo}")

    def listar_veiculos(self):
        if not self.locadora.veiculos:
            print("Nenhum veículo cadastrado.")
            return
        for i, veiculo in enumerate(self.locadora.veiculos, start=1):
            print(f"{i}. {veiculo}")

    def cadastrar_cliente(self):
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        telefone = input("Telefone: ").strip()
        cliente = self.locadora.cadastrar_cliente(nome, cpf, telefone)
        print(f"Cadastrado: {cliente}")

    def listar_clientes(self):
        if not self.locadora.clientes:
            print("Nenhum cliente cadastrado.")
            return
        for i, cliente in enumerate(self.locadora.clientes, start=1):
            print(f"{i}. {cliente}")

    def registrar_aluguel(self):
        cliente = self._escolher_cliente()
        if cliente is None:
            return
        veiculo = self._escolher_veiculo()
        if veiculo is None:
            return
        dias = self._pedir_int("Quantidade de dias: ")

        aluguel = self.locadora.registrar_aluguel(cliente, veiculo, dias)
        print(aluguel)

    def listar_alugueis(self):
        if not self.locadora.alugueis:
            print("Nenhum aluguel registrado.")
            return
        for i, aluguel in enumerate(self.locadora.alugueis, start=1):
            print(f"{i}. {aluguel}")

    def consultar_multas(self):
        veiculo = self._escolher_veiculo()
        if veiculo is None:
            return
        multas = self.locadora.consultar_multas(veiculo)
        if not multas:
            print("Nenhuma multa encontrada.")

    def _escolher_cliente(self):
        if not self.locadora.clientes:
            print("Nenhum cliente cadastrado ainda.")
            return None
        self.listar_clientes()
        indice = self._pedir_int("Número do cliente: ") - 1
        if 0 <= indice < len(self.locadora.clientes):
            return self.locadora.clientes[indice]
        print("Cliente inválido.")
        return None

    def _escolher_veiculo(self):
        if not self.locadora.veiculos:
            print("Nenhum veículo cadastrado ainda.")
            return None
        self.listar_veiculos()
        indice = self._pedir_int("Número do veículo: ") - 1
        if 0 <= indice < len(self.locadora.veiculos):
            return self.locadora.veiculos[indice]
        print("Veículo inválido.")
        return None

    @staticmethod
    def _pedir_int(mensagem: str) -> int:
        while True:
            try:
                return int(input(mensagem))
            except ValueError:
                print("Digite um número inteiro válido.")

    @staticmethod
    def _pedir_float(mensagem: str) -> float:
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Digite um número válido.")
