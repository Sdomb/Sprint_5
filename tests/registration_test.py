import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

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

        # Ассертим факт перехода в лк по клику на «Личный кабинет»
        driver.find_element(*lk.login_header_in_my_office)

        # ищем кнопку регистрации и кликаем на нее
        driver.find_element(*lk.register_link_button).click()

        # дожидаемся  поле ввода имени
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(lk.name_input_locator))

        # кладем в переменную  полt ввода в блоке регистрации
        name_input = driver.find_element(*lk.name_input_locator)

        # тапаем на поле ввода и и пишем туда имя
        name_input.send_keys('Бургермистер Оладьевич')

        #генерируем уникальную почту
        email = 'sem_domb_6' + str(random.randint(100, 999)) + '@yandex.ru'

        # тапаем на эмайл и печатаем туда емейл,
        email_input = driver.find_element(*lk.email_input_locator)
        email_input.send_keys(email)

        # тапаем на пароль и вводим известный и правильный пароль
        password_input = driver.find_element(*lk.password_input_locator)
        password_input.send_keys('Ol234567')

        # ассертим что поле имени не пустое
        assert name_input.get_attribute('value') != ''
        current_value = email_input.get_attribute('value')

        #  разделяем почту на до собаки и после, проверяем что в части "до" есть имя а в части "после" есть "yandex.ru"
        assert "sem_domb_6" in current_value.split("@")[0] and "yandex.ru" in current_value.split("@")[-1]  # ассертим что  логин соответствует эталону

        # ассертим что пароль не короче 6 символов
        assert len(password_input.get_attribute('value')) > 6

        # тапаем на кнопку зарегистрироваться
        driver.find_element(*lk.register_button).click()

        # дождиаемся что блок регистрации исчез вместе по исчезновению хедера Регистрация
        WebDriverWait(driver, 2).until(expected_conditions.invisibility_of_element_located(lk.registration_header_locator))

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
