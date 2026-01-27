from pages.login_page import LoginPage

def test_login_with_valid_credentials(page):
    """
    Caso de teste manual relacionado:
    CT-LOGIN-001 - Login com credenciais válidas
    """

    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "/inventory.html" in page.url