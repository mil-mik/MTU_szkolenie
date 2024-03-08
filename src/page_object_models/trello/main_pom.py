from playwright.async_api import expect

from src.page_object_models import base_pom


class MainPOM(base_pom.PageObjectModelBase):
    # methods goes here
    @property
    def default_url(self):
        return f"{self.env.url_ui}"

    def login_user(self, login, password):
        self.page.get_by_test_id("bignav").get_by_role("link", name="Log in").click()
        self.page.get_by_placeholder("Wprowadź adres e-mail").click()
        self.page.get_by_placeholder("Wprowadź adres e-mail").fill(login)
        self.page.get_by_role("button", name="Kontynuuj").click()
        self.page.get_by_placeholder("Wprowadź hasło").fill(password)
        self.page.get_by_role("button", name="Zaloguj się").click()
