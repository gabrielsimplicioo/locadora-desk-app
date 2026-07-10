class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str):
        self.id = None
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} (CPF {self.cpf})"
