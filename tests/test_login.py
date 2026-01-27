from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login_with_valid_credentials():
    """
    Caso de teste manual relacionado:
    CT-LOGIN-001 - Login com credenciais válidas

    Objetivo:
    Validar que o usuário consegue realizar login com credenciais válidas.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Validação continua no teste
        assert "/inventory.html" in page.url

        browser.close()