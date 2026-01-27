from playwright.sync_api import sync_playwright

def test_login_with_valid_credentials():
    """
    Caso de teste manual relacionado:
    CT-LOGIN-001 - Login com credenciais válidas

    Objetivo:
    Validar que o usuário consegue realizar login com dados válidos.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Passo 1: acessar a página de login
        page.goto("https://example.com")

        # Passos abaixo simulam um login de exemplo
        # (serão adaptados para um site real de treino)
        assert "Example Domain" in page.title()

        browser.close()