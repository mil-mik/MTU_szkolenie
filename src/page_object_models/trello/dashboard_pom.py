import playwright

from src.page_object_models import base_pom


class DashboardPOM(base_pom.PageObjectModelBase):

    def __init__(self, page: playwright.page):
        super().__init__(page)
        # self.top_menu_pom = TopMenuPOM(page)
        pass

    @property
    def default_url(self):
        return rf"{self.env.url_ui}/u/miloszmika/boards"

    def is_opened(self, selector: str = ""):
        self.page.wait_for_url(self.default_url)
