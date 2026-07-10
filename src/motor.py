class Motor:
    def __init__(self, potencia_cv: float, combustivel: str):
        self.potencia_cv = potencia_cv
        self.combustivel = combustivel

    def __str__(self):
        return f"Motor({self.potencia_cv}cv, {self.combustivel})"
