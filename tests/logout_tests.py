from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_actions import TestActions as actions


class TestLogout:

    login = 'sem_domb_6111@yandex.ru'
    passw = 'Ol234567'

    def test_logout(self, driver, lk):

        assert driver.title == "Stellar Burgers"

        # находим кнопку Войти в аккаунт на главной и кликаем на неё
        driver.find_element(*lk.login_button_for_home).click()

        # запускаем экшен логина
        actions.login_actions(self, driver, lk)

        # нажимаем на кнопку Выход чтобы разлогиниться
        driver.find_element(*lk.logout_button_in_my_office).click()

        # дожидаемся заголовка Вход
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.login_header_in_my_office))

        # ассертим налиие кнопки Войти
        assert driver.find_element(*lk.login_button_in_my_office)

        driver.quit()
