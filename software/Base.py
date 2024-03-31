import requests
from allure import step
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Env


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Env().host
        self.fake_url = 'https://www.randomlists.com/urls'
        self.assertions = self.Assertions()

    @step('Поиск элемента')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Локатор {locator} не был найден")

    @step('Поиск множества элементов')
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Множество локаторов: {locator} не были найдены")

    @step('Переход на заданную страницу')
    def go_to_site(self, url=None):
        if url is None: url = self.base_url
        return self.driver.get(url)

    @step('Получение статус-кода страницы')
    def get_page_status_code(self, page):
        response = requests.get(page)
        return response

    class Assertions:
        @staticmethod
        @step('Проверка ожидаемого статус-кода')
        def assertion_status_code(response=None, status=None):
            assert response.status_code == status, (f'Статус код: {response.status_code} '
                                                  f'не соответствует ожидаемому результату:{status}')

        @staticmethod
        @step('Проверка ожидаемого ресурса в ответе от сервера')
        def assertion_value_in_response(value=None, response=None):
            assert value in response, f'Ожидаемого {value} не оказалось в {response}'

        @staticmethod
        def element_is_visible(locator=None):
            try:
                locator.is_displayed()
                print("Элемент видим на странице.")
            except (NoSuchElementException, ElementNotVisibleException):
                print("Элемент скрыт на странице.")
