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

        # Login (pré-condição)
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Garantir que está na página de produtos
        assert "/inventory.html" in page.url

        # Adicionar produto ao carrinho
        page.click("#add-to-cart-sauce-labs-backpack")
        page.click(".shopping_cart_link")
        assert "/cart.html" in page.url

        # Iniciar checkout
        page.click("#checkout")

        # Preencher informações do checkout
        page.fill("#first-name", "Test")
        page.fill("#last-name", "User")
        page.fill("#postal-code", "12345")
        page.click("#continue")

        # Finalizar compra
        page.click("#finish")

        # Validação final
        assert "/checkout-complete.html" in page.url
        assert "Thank you for your order!" in page.inner_text(".complete-header")

        browser.close()