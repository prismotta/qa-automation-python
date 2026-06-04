from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest

@pytest.mark.smoke
def test_add_item_to_cart(page):
    """
    Caso de teste manual relacionado:
    CT-CART-001 - Adicionar item ao carrinho
    """

    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    assert "/cart.html" in page.url
    assert page.locator(".inventory_item_name").inner_text() == "Sauce Labs Backpack"