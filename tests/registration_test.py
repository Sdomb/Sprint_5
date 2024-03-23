import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_actions import TestActions as actions


class TestRegistration:

    login = 'sem_domb_6' + str(random.randint(100, 999)) + '@yandex.ru'
    passw = 'Ol234567'

    def test_successful_registration(self, driver, lk):
        """
        Тест совершает регистрацию и проверяет что :
        Поле «Имя» должно быть не пустым,
        в поле Email введён email в формате логин@домен,
        Минимальный пароль — шесть символов.

        :param driver: объект вебдрайвера
        :param lk: локаторы личного кабинета
        :return: и такое есть

        """
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.my_office))
        driver.find_element(*lk.my_office).click()

        # ищем кнопку регистрации и кликаем на нее
        driver.find_element(*lk.register_link_button).click()

        # дожидаемся  поле ввода имени
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(lk.name_input_locator))

        # кладем в переменную  поле ввода в блоке регистрации
        name_input = driver.find_element(*lk.name_input_locator)

        # тапаем на поле ввода и и пишем туда имя
        name_input.send_keys('Бургермистер Оладьевич')

        # тапаем на эмайл и печатаем туда емейл,
        email_input = driver.find_element(*lk.email_input_locator)
        email_input.send_keys(self.login)

        # тапаем на пароль и вводим известный и правильный пароль
        password_input = driver.find_element(*lk.password_input_locator)
        password_input.send_keys(self.passw)

        # тапаем на кнопку зарегистрироваться
        driver.find_element(*lk.register_button).click()

        # дождиаемся что блок регистрации исчез вместе по исчезновению хедера Регистрация
        WebDriverWait(driver, 2).until(expected_conditions.invisibility_of_element_located(lk.registration_header_locator))

        # логинимся новыми данными
        actions.login_actions(self, driver, lk)

        # ассертим успешный логин данными с новой авторизацией
        assert driver.find_element(*lk.logout_button_in_my_office)

    def test_fail_registration_because_pass(self, driver, lk):

        """
        Тест проверяет появление ошибки при вводе пароля недостаточной длины
        :param driver: объект вебдрайвера
        :param lk: локаторы личного кабинета
        :return: и такое есть
        """

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.my_office))
        driver.find_element(*lk.my_office).click()

        # ищем кнопку регистрации и кликаем на нее
        driver.find_element(*lk.register_link_button).click()

        # дожидаемся  поле ввода имени
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(lk.name_input_locator))

        # тапаем на пароль и вводим известный и неправильный пароль
        password_input = driver.find_element(*lk.password_input_locator)
        password_input.send_keys('12345')

        #  жмём на кнопк Зарегестрироваться
        driver.find_element(*lk.register_button).click()

        # ждём локатор проваленного статуса для поля ввода пароля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.input_status_error))

        #  ассертим появление текста "Некорректный пароль"
        assert driver.find_element(*lk.error_message_locator)
