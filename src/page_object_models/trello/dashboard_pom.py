import logging
import time
import allure

import playwright
from playwright.sync_api import expect

from src.page_object_models import base_pom


def log() -> logging.Logger:
    return logging.getLogger(__name__)


class DashboardPOM(base_pom.PageObjectModelBase):

    # def __init__(self, page: playwright.page):
    #     super().__init__(page)
    #     # self.top_menu_pom = TopMenuPOM(page)
    #     pass

    @property
    def default_url(self):
        return rf"{self.env.url_ui}/u/miloszmika/boards"

    def is_opened(self, selector: str = ""):
        self.page.wait_for_url(self.default_url)

    def add_new_task(self, task_name: str = "task1"):
        self.page.get_by_role("link", name="tab1 ").click()
        self.page.locator("li").filter(has_text="Do zrobieniaDo").get_by_test_id("list-add-card-button").click()
        self.page.get_by_test_id("list-card-composer-textarea").fill(f"{task_name}")

    def remove_task(self, task_name: str = "task1"):
        self.page.get_by_test_id("list-card-composer-add-card-button").click()
        time.sleep(1)
        self.page.get_by_test_id("lists").locator("div").filter(has_text=f"{task_name}").nth(2).click()
        self.page.get_by_role("link", name=" Zarchiwizuj").click()
        self.page.get_by_role("link", name=" Usuń").click()
        self.page.get_by_role("button", name="Skasuj").click()

    @allure.step("Check for doing")
    def is_doing_visible(self):
        log().debug('Check for doing')
        expect(self.page.locator("h2").filter(has_text="Do zrobienia")).to_be_visible()

    def is_done_visible(self):
        log().debug('Check for done')
        expect(self.page.locator("h2").filter(has_text="Zrobione23")).to_be_visible()
        # expect(self.page.locator("h2").filter(has_text="Zrobione")).to_be_visible()
