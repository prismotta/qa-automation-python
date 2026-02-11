[![Python Tests](https://github.com/prismotta/qa-automation-python/actions/workflows/python.yml/badge.svg)](https://github.com/prismotta/qa-automation-python/actions)

# QA Automation with Python

Este repositório faz parte do meu processo de evolução na área de **Qualidade de Software (QA)**, com foco em **automação de testes end-to-end utilizando Python e Playwright**.

O projeto demonstra a transição de **testes manuais** para **testes automatizados**, mantendo alinhamento e rastreabilidade entre os cenários documentados e a automação implementada.

---

## Objetivo do projeto
Aplicar, na prática, conceitos fundamentais de QA, como:
- Análise e criação de casos de teste
- Automação de testes end-to-end
- Organização e manutenção de testes automatizados
- Aplicação de boas práticas de automação com Page Object Model

---

## Aplicação utilizada para testes
Os testes automatizados são executados sobre o site de treino **SauceDemo**, amplamente utilizado para aprendizado e prática de automação de testes.

Fluxos automatizados:
- Login
- Adição de produto ao carrinho
- Finalização do checkout

---

## Estrutura do projeto

```text
qa-automation-python/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
└── README.md
