# DermAnalytics

Plataforma web para registro, análise e visualização de dados dermatológicos, desenvolvida como Projeto Integrador em Computação III da UNIVESP.

## Objetivo do Projeto

O objetivo do DermAnalytics é auxiliar profissionais de dermatologia no registro estruturado de informações clínicas sobre lesões cutâneas e na análise estatística desses dados por meio de gráficos interativos.

A aplicação permite cadastrar informações como:

- Idade do paciente
- Sexo
- Tipo de lesão
- Região do corpo
- Data do diagnóstico

Esses dados são armazenados em banco de dados SQLite e posteriormente consolidados em um dashboard analítico.

## Funcionalidades

- Cadastro de dados dermatológicos
- Armazenamento em banco de dados SQLite
- API REST desenvolvida com Flask
- Dashboard com gráficos utilizando Chart.js
- Validação de campos obrigatórios
- Recursos básicos de acessibilidade (`label`, `required`, `aria-label`)
- Testes automatizados com Pytest
- Integração contínua com GitHub Actions
- Deploy em nuvem com Render

## Tecnologias Utilizadas

- Python 3.11
- Flask
- Flask-CORS
- SQLite
- HTML5
- JavaScript
- Chart.js
- Pytest
- Git e GitHub
- GitHub Actions
- Render

## Estrutura do Projeto

```text
DermAnalytics/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Backend/
│   ├── app.py
│   └── database.db
├── Frontend/
│   ├── index.html
│   ├── dashboard.html
│   └── script.js
├── tests/
│   └── test_app.py
├── requirements.txt
├── render.yaml
└── README.md