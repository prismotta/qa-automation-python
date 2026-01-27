from playwright.sync_api import sync_playwright

def test_add_item_to_cart():
    """
    Caso de teste manual relacionado:
    CT-CART-001 - Adicionar item ao carrinho

    Objetivo:
    Validar que o usuário consegue adicionar um produto ao carrinho.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Login (pré-condição)
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Garantir que está na página de produtos
        assert "/inventory.html" in page.url

        # Adicionar primeiro produto ao carrinho
        page.click("#add-to-cart-sauce-labs-backpack")

        # Ir para o carrinho
        page.click(".shopping_cart_link")

        # Validar que o produto aparece no carrinho
        assert "/cart.html" in page.url
        assert page.locator(".inventory_item_name").inner_text() == "Sauce Labs Backpack"

        browser.close()