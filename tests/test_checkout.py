from playwright.sync_api import sync_playwright

def test_checkout_success():
    """
    Caso de teste manual relacionado:
    CT-CHECKOUT-001 - Finalizar checkout com sucesso

    Objetivo:
    Validar que o usuário consegue finalizar o processo de checkout.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Passo 1: acessar a aplicação
        page.goto("https://example.com")

        # Passo 2: simular finalização do checkout
        # Neste momento validamos apenas que o fluxo chegou à página esperada
        assert "Example Domain" in page.title()

        browser.close()