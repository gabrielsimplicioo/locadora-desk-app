import tkinter as tk
from tkinter import ttk, messagebox

from src.locadora import Locadora

COR_FUNDO = "#1f2933"
COR_PAINEL = "#243b53"
COR_TEXTO = "#f0f4f8"
FONTE_TITULO = ("Segoe UI", 16, "bold")
FONTE_TEXTO = ("Segoe UI", 11)


def aplicar_estilo(raiz: tk.Tk) -> ttk.Style:
    raiz.configure(bg=COR_FUNDO)
    estilo = ttk.Style(raiz)
    estilo.theme_use("clam")
    estilo.configure("TFrame", background=COR_FUNDO)
    estilo.configure("Painel.TFrame", background=COR_PAINEL)
    estilo.configure("TLabel", background=COR_FUNDO, foreground=COR_TEXTO,
                      font=FONTE_TEXTO)
    estilo.configure("Titulo.TLabel", background=COR_FUNDO,
                      foreground=COR_TEXTO, font=FONTE_TITULO)
    estilo.configure("TButton", font=FONTE_TEXTO, padding=8)
    estilo.configure("Treeview", font=FONTE_TEXTO, rowheight=26,
                      background="white", fieldbackground="white")
    estilo.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))
    return estilo


class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.locadora = Locadora()

        self.title("Locadora de Veículos")
        self.geometry("420x480")
        self.minsize(320, 240)
        aplicar_estilo(self)

        ttk.Label(self, text="Locadora de Veículos",
                  style="Titulo.TLabel").pack(pady=(24, 16))

        area = tk.Canvas(self, bg=COR_FUNDO, highlightthickness=0)
        barra = ttk.Scrollbar(self, orient="vertical", command=area.yview)
        area.configure(yscrollcommand=barra.set)
        area.pack(side="left", padx=(24, 0), pady=8, fill="both", expand=True)
        barra.pack(side="right", padx=(0, 24), pady=8, fill="y")

        painel = ttk.Frame(area, style="Painel.TFrame", padding=20)
        janela_painel = area.create_window((0, 0), window=painel, anchor="nw")

        def ajustar_scrollregion(evento):
            area.configure(scrollregion=area.bbox("all"))

        def ajustar_largura(evento):
            area.itemconfigure(janela_painel, width=evento.width)

        painel.bind("<Configure>", ajustar_scrollregion)
        area.bind("<Configure>", ajustar_largura)

        def rolar(evento):
            area.yview_scroll(int(-evento.delta / 120), "units")

        area.bind_all("<MouseWheel>", rolar)
        area.bind_all("<Button-4>", lambda evento: area.yview_scroll(-1, "units"))
        area.bind_all("<Button-5>", lambda evento: area.yview_scroll(1, "units"))

        botoes = [
            ("Cadastrar veículo", self.abrir_cadastro_veiculo),
            ("Listar veículos", self.abrir_listagem_veiculos),
            ("Cadastrar cliente", self.abrir_cadastro_cliente),
            ("Listar clientes", self.abrir_listagem_clientes),
            ("Registrar aluguel", self.abrir_registro_aluguel),
            ("Listar aluguéis", self.abrir_listagem_alugueis),
            ("Consultar multas", self.abrir_consulta_multa),
        ]
        for texto, comando in botoes:
            ttk.Button(painel, text=texto, command=comando).pack(
                fill="x", pady=6)

    def abrir_cadastro_veiculo(self):
        JanelaCadastroVeiculo(self, self.locadora)

    def abrir_cadastro_cliente(self):
        JanelaCadastroCliente(self, self.locadora)

    def abrir_registro_aluguel(self):
        JanelaRegistrarAluguel(self, self.locadora)

    def abrir_consulta_multa(self):
        JanelaConsultaMulta(self, self.locadora)

    def abrir_listagem_veiculos(self):
        JanelaListagem(self, "Veículos cadastrados",
                        [str(v) for v in self.locadora.veiculos])

    def abrir_listagem_clientes(self):
        JanelaListagem(self, "Clientes cadastrados",
                        [str(c) for c in self.locadora.clientes])

    def abrir_listagem_alugueis(self):
        JanelaListagem(self, "Aluguéis registrados",
                        [str(a) for a in self.locadora.alugueis])


class JanelaCadastroVeiculo(tk.Toplevel):
    CAMPOS_EXTRA = {
        "Carro": ("Número de portas", int),
        "Moto": ("Cilindrada", int),
        "Caminhão": ("Capacidade de carga (t)", float),
    }

    def __init__(self, pai: tk.Widget, locadora: Locadora):
        super().__init__(pai)
        self.locadora = locadora
        self.title("Cadastrar veículo")
        self.configure(bg=COR_FUNDO)
        self.resizable(False, False)

        campo = ttk.Frame(self, padding=20)
        campo.pack()

        self.tipo = tk.StringVar(value="Carro")
        ttk.Label(campo, text="Tipo").grid(row=0, column=0, sticky="w", pady=4)
        combo = ttk.Combobox(campo, textvariable=self.tipo, state="readonly",
                              values=list(self.CAMPOS_EXTRA))
        combo.grid(row=0, column=1, pady=4)
        combo.bind("<<ComboboxSelected>>",
                   lambda evento: self._atualizar_rotulo_extra())

        self.entradas = {}
        rotulos = ["Placa", "Marca", "Modelo", "Ano", "Valor da diária",
                   "Potência (cv)", "Combustível"]
        for i, rotulo in enumerate(rotulos, start=1):
            ttk.Label(campo, text=rotulo).grid(row=i, column=0, sticky="w", pady=4)
            entrada = ttk.Entry(campo)
            entrada.grid(row=i, column=1, pady=4)
            self.entradas[rotulo] = entrada

        linha_extra = len(rotulos) + 1
        self.rotulo_extra = ttk.Label(campo, text="")
        self.rotulo_extra.grid(row=linha_extra, column=0, sticky="w", pady=4)
        self.entrada_extra = ttk.Entry(campo)
        self.entrada_extra.grid(row=linha_extra, column=1, pady=4)
        self._atualizar_rotulo_extra()

        ttk.Button(campo, text="Cadastrar", command=self._cadastrar).grid(
            row=linha_extra + 1, column=0, columnspan=2, pady=(16, 0), sticky="ew")

    def _atualizar_rotulo_extra(self):
        texto, _ = self.CAMPOS_EXTRA[self.tipo.get()]
        self.rotulo_extra.configure(text=texto)

    def _cadastrar(self):
        try:
            placa = self.entradas["Placa"].get()
            marca = self.entradas["Marca"].get()
            modelo = self.entradas["Modelo"].get()
            ano = int(self.entradas["Ano"].get())
            valor_diaria = float(self.entradas["Valor da diária"].get())
            potencia_cv = float(self.entradas["Potência (cv)"].get())
            combustivel = self.entradas["Combustível"].get()
            _, conversor = self.CAMPOS_EXTRA[self.tipo.get()]
            valor_extra = conversor(self.entrada_extra.get())
        except ValueError:
            messagebox.showerror("Erro", "Verifique os campos numéricos.")
            return

        if self.tipo.get() == "Carro":
            veiculo = self.locadora.cadastrar_carro(
                placa, marca, modelo, ano, valor_diaria, potencia_cv,
                combustivel, valor_extra)
        elif self.tipo.get() == "Moto":
            veiculo = self.locadora.cadastrar_moto(
                placa, marca, modelo, ano, valor_diaria, potencia_cv,
                combustivel, valor_extra)
        else:
            veiculo = self.locadora.cadastrar_caminhao(
                placa, marca, modelo, ano, valor_diaria, potencia_cv,
                combustivel, valor_extra)

        messagebox.showinfo("Sucesso", f"Cadastrado: {veiculo}")
        self.destroy()


class JanelaCadastroCliente(tk.Toplevel):
    def __init__(self, pai: tk.Widget, locadora: Locadora):
        super().__init__(pai)
        self.locadora = locadora
        self.title("Cadastrar cliente")
        self.configure(bg=COR_FUNDO)
        self.resizable(False, False)

        campo = ttk.Frame(self, padding=20)
        campo.pack()

        self.entradas = {}
        for i, rotulo in enumerate(["Nome", "CPF", "Telefone"]):
            ttk.Label(campo, text=rotulo).grid(row=i, column=0, sticky="w", pady=4)
            entrada = ttk.Entry(campo)
            entrada.grid(row=i, column=1, pady=4)
            self.entradas[rotulo] = entrada

        ttk.Button(campo, text="Cadastrar", command=self._cadastrar).grid(
            row=3, column=0, columnspan=2, pady=(16, 0), sticky="ew")

    def _cadastrar(self):
        nome = self.entradas["Nome"].get()
        cpf = self.entradas["CPF"].get()
        telefone = self.entradas["Telefone"].get()
        if not nome or not cpf:
            messagebox.showerror("Erro", "Nome e CPF são obrigatórios.")
            return
        cliente = self.locadora.cadastrar_cliente(nome, cpf, telefone)
        messagebox.showinfo("Sucesso", f"Cadastrado: {cliente}")
        self.destroy()


class JanelaRegistrarAluguel(tk.Toplevel):
    def __init__(self, pai: tk.Widget, locadora: Locadora):
        super().__init__(pai)
        self.locadora = locadora

        if not locadora.clientes or not locadora.veiculos:
            messagebox.showwarning(
                "Aviso", "Cadastre ao menos um cliente e um veículo antes.")
            self.destroy()
            return

        self.title("Registrar aluguel")
        self.configure(bg=COR_FUNDO)
        self.resizable(False, False)

        campo = ttk.Frame(self, padding=20)
        campo.pack()

        ttk.Label(campo, text="Cliente").grid(row=0, column=0, sticky="w", pady=4)
        self.cliente_var = tk.StringVar(value=str(locadora.clientes[0]))
        ttk.Combobox(campo, textvariable=self.cliente_var, state="readonly",
                     values=[str(c) for c in locadora.clientes]).grid(
                         row=0, column=1, pady=4)

        ttk.Label(campo, text="Veículo").grid(row=1, column=0, sticky="w", pady=4)
        self.veiculo_var = tk.StringVar(value=str(locadora.veiculos[0]))
        ttk.Combobox(campo, textvariable=self.veiculo_var, state="readonly",
                     values=[str(v) for v in locadora.veiculos]).grid(
                         row=1, column=1, pady=4)

        ttk.Label(campo, text="Dias").grid(row=2, column=0, sticky="w", pady=4)
        self.entrada_dias = ttk.Entry(campo)
        self.entrada_dias.grid(row=2, column=1, pady=4)

        ttk.Button(campo, text="Registrar", command=self._registrar).grid(
            row=3, column=0, columnspan=2, pady=(16, 0), sticky="ew")

    def _registrar(self):
        try:
            dias = int(self.entrada_dias.get())
        except ValueError:
            messagebox.showerror("Erro", "Dias deve ser um número inteiro.")
            return

        clientes_str = [str(c) for c in self.locadora.clientes]
        veiculos_str = [str(v) for v in self.locadora.veiculos]
        cliente = self.locadora.clientes[clientes_str.index(self.cliente_var.get())]
        veiculo = self.locadora.veiculos[veiculos_str.index(self.veiculo_var.get())]

        aluguel = self.locadora.registrar_aluguel(cliente, veiculo, dias)
        messagebox.showinfo("Sucesso", str(aluguel))
        self.destroy()


class JanelaConsultaMulta(tk.Toplevel):
    def __init__(self, pai: tk.Widget, locadora: Locadora):
        super().__init__(pai)
        self.locadora = locadora

        if not locadora.veiculos:
            messagebox.showwarning("Aviso", "Cadastre um veículo antes.")
            self.destroy()
            return

        self.title("Consultar multas")
        self.configure(bg=COR_FUNDO)
        self.resizable(False, False)

        campo = ttk.Frame(self, padding=20)
        campo.pack()

        ttk.Label(campo, text="Veículo").grid(row=0, column=0, sticky="w", pady=4)
        self.veiculo_var = tk.StringVar(value=str(locadora.veiculos[0]))
        ttk.Combobox(campo, textvariable=self.veiculo_var, state="readonly",
                     values=[str(v) for v in locadora.veiculos]).grid(
                         row=0, column=1, pady=4)

        ttk.Button(campo, text="Consultar", command=self._consultar).grid(
            row=1, column=0, columnspan=2, pady=(16, 0), sticky="ew")

    def _consultar(self):
        veiculos_str = [str(v) for v in self.locadora.veiculos]
        veiculo = self.locadora.veiculos[veiculos_str.index(self.veiculo_var.get())]
        multas = self.locadora.consultar_multas(veiculo)
        texto = "\n".join(multas) if multas else "Nenhuma multa encontrada."
        messagebox.showinfo("Resultado", texto)


class JanelaListagem(tk.Toplevel):
    def __init__(self, pai: tk.Widget, titulo: str, itens: list[str]):
        super().__init__(pai)
        self.title(titulo)
        self.configure(bg=COR_FUNDO)
        self.geometry("420x320")

        ttk.Label(self, text=titulo, style="Titulo.TLabel").pack(pady=12)

        lista = tk.Listbox(self, font=FONTE_TEXTO, bg="white", fg=COR_FUNDO,
                            relief="flat", highlightthickness=0)
        lista.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        if itens:
            for item in itens:
                lista.insert("end", item)
        else:
            lista.insert("end", "Nenhum registro encontrado.")
            lista.configure(state="disabled")
