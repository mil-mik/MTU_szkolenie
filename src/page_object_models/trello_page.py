import playwright.sync_api as playwright
from src.page_object_models.trello import main_pom
from src.page_object_models.trello.dashboard_pom import DashboardPOM


class TrelloPage:
    def __init__(self, page: playwright.Page):
        self.main_pom = main_pom.MainPOM(page=page)
        self.dashboard_pom = DashboardPOM(page=page)
