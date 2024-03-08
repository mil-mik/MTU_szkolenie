import logging
from src.page_object_models.trello_page import TrelloPage


def log() -> logging.Logger:
    return logging.getLogger(__name__)


def test_temp_open_trello(trello_page: TrelloPage):
    ...
    # trello_page.main_pom.goto()
    # trello_page.dashboard_pom.is_opened()


