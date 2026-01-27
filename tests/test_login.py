from playwright.sync_api import sync_playwright

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

        # Acessar página de login
        page.goto("https://www.saucedemo.com/")

        # Preencher credenciais válidas
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        # Clicar no botão de login
        page.click("#login-button")

        # Validar redirecionamento para a página de produtos
        assert "/inventory.html" in page.url

        browser.close()