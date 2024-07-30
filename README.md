
# Projeto Jul.ia

Bem-vindo ao projeto Jul.ia! Este repositório contém o código e os dados necessários para o desenvolvimento de uma aplicação de gerenciamento hospitalar com funcionalidades de agendamento de consultas, gestão de médicos, pacientes e hospitais, utilizando bancos de dados SQL e NoSQL.

## Estrutura do Repositório

```plaintext
.
├── .venv
├── .vscode
├── config
│   └── ...
├── data
│   ├── mongo
│   │   ├── history-conversation.json
│   │   └── template.json
│   ├── mysql
│   │   ├── Consultas.csv
│   │   ├── Disponibilidades.csv
│   │   ├── Hospitais.csv
│   │   ├── Medicos.csv
│   │   ├── Pacientes.csv
│   │   └── Trabalha.csv
│   ├── rag
│   │   └── data-rag.txt
│   └── synthetic-data
│       ├── mongo.py
│       └── mysql.py
├── database-mongo
│   ├── config_mongo.py
│   └── insert-mongodb.py
├── database-mysql
│   ├── create-tables.sql
│   └── insert-mysql.ipynb
├── .env
├── .gitignore
├── julia.ipynb
├── LICENSE
├── README.md
└── requirements.txt
```

## Instalação

### Pré-requisitos

- Python 3.8+
- MySQL
- MongoDB

### Passos para Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/jul.ia.git
    cd jul.ia
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows, use .venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente no arquivo `.env` conforme necessário.

## Banco de Dados MySQL

### Estrutura do Banco de Dados

As tabelas do banco de dados MySQL são criadas a partir do arquivo `database-mysql/create-tables.sql`. A estrutura inclui as tabelas `Hospital`, `Paciente`, `Medico`, `Disponibilidade`, `Trabalha`, e `Consulta`.

### Criando as Tabelas

Execute o arquivo SQL para criar as tabelas:

```bash
mysql -u seu_usuario -p < database-mysql/create-tables.sql
```

### Inserindo Dados

Use o notebook `insert-mysql.ipynb` para inserir os dados dos arquivos CSV na pasta `data/mysql`.

## Banco de Dados MongoDB

### Estrutura do Banco de Dados

Os dados do MongoDB são configurados utilizando os arquivos JSON na pasta `data/mongo`.

### Configuração

Edite o arquivo `database-mongo/config_mongo.py` para configurar a conexão com o MongoDB.

### Inserindo Dados

Execute o script `insert-mongodb.py` para inserir os dados:

```bash
python database-mongo/insert-mongodb.py
```

## Uso

### Executando a Aplicação

Para iniciar a aplicação, use o notebook `julia.ipynb` ou desenvolva novos scripts conforme necessário.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
