# taco-project

## Descrição do Projeto

Este projeto tem como objetivo extrair e analisar informações da TACO (Tabela Brasileira de Composição de Alimentos). Utilizando uma versão "limpa" da tabela TACO, o projeto utiliza Python para a leitura e parse da tabela, empregando a biblioteca Pandas para organizar os dados em formato CSV. A exportação final é realizada em formato JSON.


## Funcionalidades Principais

1. **Extração de Dados:** O projeto extrai dados da tabela TACO, garantindo uma representação limpa e organizada das informações.

2. **Parse com Pandas e exportação para JSON:** Utiliza a biblioteca Pandas para realizar o parse dos dados, proporcionando uma estrutura tabular adequada. Para fornecer os dados para o front-end a exportação final é feita por meio de um arquivo JSON

3. **Front-end em Vue (Em Desenvolvimento):** Desenvolvimento de um front-end em Vue para a visualização dos dados de todos os alimentos da tabela.

## Como Usar

1. Clone o repositório para o seu ambiente local.

    ```bash
    git clone https://github.com/alissa-l/taco-project.git
   ```

1. Instale as depêndencias.

    ```bash
    pip install -r scripts/requirements.txt
   ```

1. Execute o script.

    ```bash
    python3 scripts/main.py
   ```

1. Inicie o front-end em vue.

    ```bash
    cd taco-site
    npm run dev
   ```