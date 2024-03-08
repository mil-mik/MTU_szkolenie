import logging
from src.page_object_models.trello_page import TrelloPage


def log() -> logging.Logger:
    return logging.getLogger(__name__)


def test_example(trello_page: TrelloPage):
    trello_page.main_pom.goto()
    trello_page.main_pom.login_user(login="milosz.mika@yahoo.com", password="Qwerty1234$")
