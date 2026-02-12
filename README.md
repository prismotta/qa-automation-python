# QA Automation with Python

[![Python Tests](https://github.com/prismotta/qa-automation-python/actions/workflows/python.yml/badge.svg)](https://github.com/prismotta/qa-automation-python/actions)

Projeto de automação E2E utilizando Python + Playwright + Pytest, aplicando Page Object Model e integração contínua com GitHub Actions.

---

## Tecnologias

- Python
- Playwright
- Pytest
- GitHub Actions

---

## Estrutura do Projeto

```
qa-automation-python/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
├── conftest.py
├── requirements.txt
└── README.md
```

## Como Executar Localmente

### 1. Clonar o repositório

git clone https://github.com/prismotta/qa-automation-python.git
cd qa-automation-python

### 2. Criar ambiente virtual (opcional)

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

### 3. Instalar dependências

pip install -r requirements.txt

### 4. Instalar navegadores

playwright install

### 5. Executar testes

pytest

---

## Integração Contínua

Os testes são executados automaticamente via GitHub Actions em:
- Push na branch main
- Pull Requests

---

## Autora

Priscila Motta