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

def test_login_with_invalid_credentials(page):
    """
    Caso de teste manual relacionado:
    CT-LOGIN-002 - Login com credenciais inválidas
    """

    login_page = LoginPage(page)
    login_page.open()
    login_page.login("invalid_user", "wrong_password")

    expected_error = "Epic sadface: Username and password do not match any user in this service"

    assert login_page.get_error_message() == expected_error
