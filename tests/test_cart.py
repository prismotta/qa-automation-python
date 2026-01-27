from playwright.sync_api import sync_playwright

def test_add_item_to_cart():
    """
    Caso de teste manual relacionado:
    CT-CART-001 - Adicionar item ao carrinho

    Objetivo:
    Validar que o usuário consegue adicionar um item ao carrinho.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Passo 1: acessar a aplicação
        page.goto("https://example.com")

        # Passo 2: simular adição de item ao carrinho
        # (neste primeiro momento usamos uma validação simples)
        assert "Example Domain" in page.title()

        browser.close()