from allure import step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"
        self.assertions = self.Assertions()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Локатор {locator} не был найден")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Множество локаторов: {locator} не были найдены")

    def go_to_page(self):
        return self.driver.get(self.base_url)

    class Assertions:
        @staticmethod
        @step('Проверка ожидаемого статус-кода')
        def assertion_status_code(response=None, code=None):
            assert response.status_code == code, (f'Статус код: {response.status_code} '
                                                  f'не соответствует ожидаемому результату:{code}')

        @staticmethod
        @step('Проверка ожидаемого ресурса в ответе от сервера')
        def assertion_value_in_response(value=None, response=None):
            assert value in response, f'Ожидаемого {value} не оказалось в {response}'