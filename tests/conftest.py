import pytest
from selenium import webdriver
from personal_locators import PersonalArea


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def lk():
    lk = PersonalArea()
    return lk
