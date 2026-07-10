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
