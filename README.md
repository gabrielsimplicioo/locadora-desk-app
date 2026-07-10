# Locadora de Veículos — Desk App (Nível 1)

Modelagem em Python orientada a objetos para o Nível 1 da macro tarefa,
cobrindo as cinco relações pedidas:

- **Herança**: `Carro`, `Moto` e `Caminhao` herdam de `Veiculo` (`src/veiculo.py`).
- **Polimorfismo**: cada subclasse sobrescreve `calcular_aluguel(dias)` com
  sua própria regra de cobrança.
- **Composição**: todo `Veiculo` cria seu próprio `Motor` (`src/motor.py`)
  dentro do construtor — o Motor não existe fora do Veiculo.
- **Associação**: `Aluguel` (`src/aluguel.py`) referencia um `Cliente` e um
  `Veiculo` que existem de forma independente dele.
- **Dependência**: `ServicoConsultaMulta` (`src/servico_multa.py`) recebe um
  `Veiculo` só como parâmetro de método, sem guardar referência.

## Rodando

```bash
python3 main.py
```

O `main.py` instancia as três subclasses de `Veiculo`, demonstra o
polimorfismo, cria clientes e aluguéis (associação) e chama o serviço de
consulta de multas (dependência) — cobrindo todas as funcionalidades para
o vídeo de apresentação.

## Diagrama UML

Fonte em `docs/diagrama.mmd` (sintaxe Mermaid). Para visualizar/exportar
como imagem: cole o conteúdo em https://mermaid.live ou use a extensão
Mermaid do VS Code.

## Nível 2 — Menu no terminal

`main.py` inicia um menu (`src/menu.py`) que dá acesso a todos os modelos
do Nível 1 através da classe `Locadora` (`src/locadora.py`).

## Nível 3 — Persistência em banco de dados

A `Locadora` agora salva e carrega tudo de um banco SQLite
(`locadora.db`, criado automaticamente na primeira execução) através de
`src/banco.py` e dos repositórios `src/veiculo_repositorio.py`,
`src/cliente_repositorio.py` e `src/aluguel_repositorio.py`. Cada
cadastro feito pelo menu é gravado no banco na hora, e ao abrir o
programa de novo os dados da sessão anterior continuam lá.
