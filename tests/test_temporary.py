import logging
from src.page_object_models.trello_page import TrelloPage


def log() -> logging.Logger:
    return logging.getLogger(__name__)


# def test_example(trello_page: TrelloPage):
#     trello_page.main_pom.goto()
#     trello_page.main_pom.login_user(login="milosz.mika@yahoo.com", password="Qwerty1234$")


def test_new_list(check, trello_page: TrelloPage):
    trello_page.main_pom.goto()
    trello_page.main_pom.login_user(login="milosz.mika@yahoo.com", password="Qwerty1234$")
    trello_page.dashboard_pom.add_new_task()
    with check:
        trello_page.dashboard_pom.is_done_visible()
    with check:
        trello_page.dashboard_pom.is_doing_visible()
    trello_page.dashboard_pom.remove_task()
