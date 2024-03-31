import pytest
from selenium import webdriver
from config import Env


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def env():
    return Env
