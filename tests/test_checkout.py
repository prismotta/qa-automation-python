import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
def test_checkout_success(page):
    """
    Caso de teste manual relacionado:
    CT-CHECKOUT-001 - Finalizar checkout com sucesso
    """

    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    checkout_page = CheckoutPage(page)
    checkout_page.start_checkout()
    checkout_page.fill_information("Test", "User", "12345")
    checkout_page.finish()

    assert "/checkout-complete.html" in page.url
    assert "Thank you for your order!" in page.inner_text(".complete-header")
