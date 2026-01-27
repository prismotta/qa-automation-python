from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

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

        # Login
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        assert "/inventory.html" in page.url

        # Produto e carrinho
        inventory_page = InventoryPage(page)
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()
        assert "/cart.html" in page.url

        # Checkout
        checkout_page = CheckoutPage(page)
        checkout_page.start_checkout()
        checkout_page.fill_information("Test", "User", "12345")
        checkout_page.finish()

        # Validação final
        assert "/checkout-complete.html" in page.url
        assert "Thank you for your order!" in page.inner_text(".complete-header")

        browser.close()