from src.page_object_models import base_pom


class MainPOM(base_pom.PageObjectModelBase):
    # methods goes here
    @property
    def default_url(self):
        return f"{self.env.url_ui}"

    def login(self):
        self.page.get_by_role()
        self.page.fill()
