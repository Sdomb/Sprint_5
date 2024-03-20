from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_actions import TestActions as actions


class TestLogin:

    login = 'sem_domb_6111@yandex.ru'
    passw = 'Ol234567'

    def test_login_in_account_button(self, driver, lk):

        # находим кнопку Войти в аккаунт на главной и кликаем на неё
        driver.find_element(*lk.login_button_for_home).click()

        # запускаем экшен логина
        actions.login_actions(self, driver, lk)

        # ассертим логин
        assert driver.find_element(*lk.logout_button_in_my_office)

    def test_login_in_personal_area_button(self, driver, lk):

        # ждем кнопку ЛК и тапаем на неё
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.my_office))
        driver.find_element(*lk.my_office).click()

        # логинимся через экшн
        actions.login_actions(self, driver, lk)

        # ассертим логин
        assert driver.find_element(*lk.logout_button_in_my_office)

    def test_login_in_registration_button(self, driver, lk):

        # ждем кнопку ЛК и тапаем на неё
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.my_office))
        driver.find_element(*lk.my_office).click()

        # Ищем кнопку Зерегистрирроваться и нажимаем на неё
        driver.find_element(*lk.register_link_button).click()

        # Ждем наличие хедера с текстом Регистрация
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.registration_header_locator))

        # Ищем кнопку Войти и тапаем на неё
        driver.find_element(*lk.register_input_link_button).click()

        # логинимся через экшн
        actions.login_actions(self, driver, lk)

        # ассертим логин
        assert driver.find_element(*lk.logout_button_in_my_office)

    def test_login_in_recovery_button(self, driver, lk):

        # ассертим заголовок страницы,  ждем кнопку ЛК и тапаем на неё
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.my_office))
        driver.find_element(*lk.my_office).click()

        # Ищем кнопку Восстановить пароль и нажимаем на неё
        driver.find_element(*lk.recovery_pass_link_button).click()

        # Ждём заголовок страницы восстановления пароля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.recovery_pass_header))

        # Ищем кнопку Войти и тапаем на неё
        driver.find_element(*lk.register_input_link_button).click()

        # логинимся через экшн и ассертим что залогинились в нем же
        actions.login_actions(self, driver, lk)

        # ассертим логин
        assert driver.find_element(*lk.logout_button_in_my_office)
