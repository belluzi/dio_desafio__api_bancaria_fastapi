# Desafio: API Bancaria Assincrona com FastAPI

Projeto desenvolvido como parte de um curso, com o objetivo de construir uma API RESTful assincrona para gerenciar operacoes bancarias simples, como depositos, saques e exibicao de extrato.

O desafio propoe o uso do FastAPI para criar uma aplicacao backend moderna, eficiente e documentada, aplicando boas praticas de design de APIs, validacao de dados e, em uma etapa posterior, autenticacao com JWT.

## Objetivos do desafio

- Cadastrar transacoes bancarias, como depositos e saques.
- Exibir o extrato de uma conta, listando as transacoes realizadas.
- Relacionar transacoes a contas correntes.
- Validar regras de negocio, como impedir valores negativos e saques sem saldo suficiente.
- Proteger endpoints sensiveis com autenticacao JWT.
- Documentar a API automaticamente com OpenAPI/Swagger.

## Requisitos tecnicos extraidos do enunciado

- **FastAPI:** framework principal para criacao da API.
- **Operacoes assincronas:** uso de recursos `async` para lidar melhor com operacoes de I/O.
- **Modelagem de dados:** representacao de contas correntes e transacoes.
- **Validacao das operacoes:** regras para depositos, saques e saldo disponivel.
- **Seguranca:** autenticacao com JWT para endpoints que exigirem usuario autenticado.
- **Documentacao OpenAPI:** descricao de endpoints, parametros e modelos de dados.

## Modelagem de entidades

Para atender aos requisitos do desafio, a API precisa de tres conceitos principais:

### Conta Bancaria

Entidade que representa a conta corrente e concentra o saldo atual.

| Campo | Descricao |
| --- | --- |
| `id` | Identificador interno da conta |
| `agency` | Agencia bancaria |
| `number` | Numero da conta |
| `digit` | Digito da conta |
| `owner_name` | Nome do titular |
| `owner_document` | Documento do titular |
| `balance_cents` | Saldo atual da conta armazenado em centavos |
| `is_active` | Indica se a conta esta ativa |
| `created_at` | Data de criacao |
| `updated_at` | Data da ultima atualizacao |

### Transacao

Entidade que representa uma movimentacao bancaria vinculada a uma conta.

| Campo | Descricao |
| --- | --- |
| `id` | Identificador interno da transacao |
| `account_id` | Conta bancaria relacionada |
| `type` | Tipo da transacao: `deposit` ou `withdraw` |
| `amount_cents` | Valor da transacao armazenado em centavos, sempre positivo |
| `description` | Descricao opcional da movimentacao |
| `occurred_at` | Data em que a transacao ocorreu |
| `balance_after_cents` | Saldo da conta apos a transacao, armazenado em centavos |
| `created_at` | Data de registro da transacao |

### Extrato

O extrato nao precisa ser uma tabela propria no banco. Ele pode ser uma visao montada a partir da conta bancaria e de suas transacoes.

| Campo | Descricao |
| --- | --- |
| `account_id` | Conta consultada |
| `agency` | Agencia bancaria |
| `account_number` | Numero da conta |
| `account_digit` | Digito da conta |
| `owner_name` | Nome do titular |
| `current_balance_cents` | Saldo atual armazenado em centavos |
| `issued_at` | Data de emissao do extrato |
| `transactions` | Lista de transacoes realizadas |

### Valor monetario

Os valores monetarios sao representados no dominio pelo objeto de valor `Money`.

Esse objeto centraliza as regras de dinheiro:

- nao permite valores negativos;
- garante no maximo duas casas decimais;
- converte valores decimais para centavos;
- realiza soma e subtracao sem usar `float`;
- impede que uma subtracao gere saldo negativo.

Na API, valores podem ser recebidos e exibidos como decimal, por exemplo `100.50`. Internamente, o armazenamento usa inteiros em centavos, por exemplo `10050`. Essa abordagem evita problemas de precisao e deixa as regras de dinheiro concentradas em um unico lugar.

## Estado atual do projeto

O projeto esta em desenvolvimento. A estrutura inicial da API ja foi criada, com separacao em camadas para controllers, services, schemas, models e views.

Atualmente existem arquivos para o fluxo de transacoes, incluindo:

- schema de entrada e atualizacao de transacoes;
- view/modelo de saida de transacoes;
- controller com rotas de criacao, listagem, atualizacao e remocao;
- service ainda pendente de implementacao das regras de negocio.

O arquivo `main.py` ainda contem as rotas padrao de exemplo do FastAPI e ainda precisa registrar os routers da aplicacao bancaria.

## Estrutura do projeto

```text
.
+-- banking_API/
|   +-- main.py
|   +-- controllers/
|   |   +-- statement.py
|   |   +-- transaction.py
|   +-- models/
|   |   +-- statement.py
|   |   +-- transaction.py
|   +-- schemas/
|   |   +-- transaction.py
|   +-- services/
|   |   +-- transaction.py
|   +-- views/
|       +-- transaction.py
+-- requirements.txt
+-- README.md
```

## Tecnologias

- Python
- FastAPI
- Pydantic
- OpenAPI/Swagger
- JWT, previsto no desafio

## Como executar localmente

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale as dependencias principais:

```bash
pip install fastapi "uvicorn[standard]"
```

Execute a aplicacao:

```bash
uvicorn banking_API.main:app --reload
```

Acesse a documentacao interativa:

```text
http://127.0.0.1:8000/docs
```

## Endpoints planejados

| Metodo | Rota | Descricao |
| --- | --- | --- |
| `POST` | `/transactions/` | Cria uma transacao bancaria |
| `GET` | `/transactions/` | Lista as transacoes cadastradas |
| `PATCH` | `/transactions/{transaction_id}` | Atualiza uma transacao |
| `DELETE` | `/transactions/{transaction_id}` | Remove uma transacao |
| `GET` | `/statement/` | Exibe o extrato da conta |

## Proximos passos

- Registrar os routers no `main.py`.
- Implementar a camada de service para transacoes.
- Criar modelos de conta corrente e extrato.
- Definir regras para deposito, saque e saldo.
- Persistir os dados em banco ou armazenamento escolhido.
- Implementar autenticacao com JWT.
- Adicionar validacoes de valor e tipo de operacao.
- Preencher o `requirements.txt` com as dependencias do projeto.
- Criar testes automatizados para os fluxos principais.

## Referencia do desafio

As informacoes deste README foram montadas a partir dos prints do enunciado do curso, que descrevem uma API bancaria assincrona com FastAPI, contendo cadastro de transacoes, exibicao de extrato, autenticacao com JWT, validacao de operacoes e documentacao com OpenAPI.
