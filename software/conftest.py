import pytest
from selenium import webdriver
from config import Env
from allure import step


@step('Запуск веб-драйвера перед началом теста и отключение после прохождения')
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@step('Подготовка данных окружения')
@pytest.fixture
def env():
    return Env
