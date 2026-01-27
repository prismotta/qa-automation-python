from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

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

        # Login
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        assert "/inventory.html" in page.url

        # Ações de produto/carrinho
        inventory_page = InventoryPage(page)
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()

        # Validação
        assert "/cart.html" in page.url
        assert page.locator(".inventory_item_name").inner_text() == "Sauce Labs Backpack"

        browser.close()