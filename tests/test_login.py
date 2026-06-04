import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "/inventory.html" in page.url


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        pytest.param(
            "invalid_user",
            "wrong_password",
            "Epic sadface: Username and password do not match any user in this service",
            id="invalid_credentials"
        ),
        pytest.param(
            "",
            "secret_sauce",
            "Epic sadface: Username is required",
            id="empty_username"
        ),
        pytest.param(
            "standard_user",
            "",
            "Epic sadface: Password is required",
            id="empty_password"
        ),
        pytest.param(
            "",
            "",
            "Epic sadface: Username is required",
            id="both_fields_empty"
        ),
    ]
)
def test_login_negative_scenarios(page, username, password, expected_error):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)

    assert login_page.get_error_message() == expected_error
