from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestActions:

    def __init__(self):
        self.login = None
        self.passw = None

    def login_actions(self, driver, lk):
        # Ждём хедер блока входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(lk.login_header_in_my_office))

        # Вводим емейл в поле вода логина
        driver.find_element(*lk.email_input_locator).send_keys(self.login)

        # Вводим пароль в поле ввода пароля
        driver.find_element(*lk.password_input_locator).send_keys(self.passw)

        # Нажимаем на кнопку Войти
        driver.find_element(*lk.login_button_in_my_office).click()

        # Проверяем что блок логина исчез с кнопкой Войти
        WebDriverWait(driver, 4).until(
            expected_conditions.invisibility_of_element_located(lk.login_button_in_my_office))

        # Переходим в ЛК
        driver.find_element(*lk.my_office).click()

        # Дожидаемся кнопку Выход и ассертим
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(lk.logout_button_in_my_office))
