from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTransition:

    def test_transition_tap_on_constructor(self, driver, lk):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.my_office))
        driver.find_element(*lk.my_office).click()

        # дожидаемся заголовка Вход
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.login_header_in_my_office))

        # ищем кнопку конструктор и нажимаем на неё
        driver.find_element(*lk.my_constructor).click()

        # ассeртим факт перехода на страницу конструктора
        assert driver.find_element(*lk.constructor_title)

    def test_transition_tap_on_stellar(self, driver, lk):

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.my_office))
        driver.find_element(*lk.my_office).click()

        # дожидаемся заголовка Вход
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.login_header_in_my_office))

        # ищем Хедер StellarBurgers на главной странице и нажимаем на неё
        driver.find_element(*lk.app_main_stellar_header).click()

        # ассeртим факт перехода на страницу конструктора
        assert driver.find_element(*lk.constructor_title)

    def test_transition_tap_on_sauce(self, driver, lk):

        # Ждём Хедер StellarBurgers на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.app_main_stellar_header))

        # ищем кнопку соуса и нажимаем на неё
        driver.find_element(*lk.sauce_button_section).click()

        # ассертим наличие в родительском локаторе Соуса атрибута выбранности
        parent_loc_sauce = driver.find_element(*lk.parent_sauce_btn_section)
        assert 'tab_tab_type_current__2BEPc' in parent_loc_sauce.get_attribute('class')

    def test_transition_tap_on_buns(self, driver, lk):

        # Ждём Хедер StellarBurgers на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.app_main_stellar_header))

        # ищем кнопку Начинок и нажимаем на неё
        driver.find_element(*lk.fillings_button_section).click()

        # ищем кнопку Булочек и нажимаем на неё
        driver.find_element(*lk.buns_button_section).click()

        # ассертим наличие в родительском локаторе Булочек атрибута выбранности
        parent_loc_bun = driver.find_element(*lk.parent_buns_btn_section)
        assert 'tab_tab_type_current__2BEPc' in parent_loc_bun.get_attribute('class')

    def test_transition_tap_on_fillings(self, driver, lk):

        # Ждём Хедер StellarBurgers на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.app_main_stellar_header))

        # Ищем кнопку Начинок и нажимаем на неё
        driver.find_element(*lk.fillings_button_section).click()

        # ассертим наличие в родительском локаторе Булочек атрибута выбранности
        parent_loc_fill = driver.find_element(*lk.parent_fillings_btn_section)
        assert 'tab_tab_type_current__2BEPc' in parent_loc_fill.get_attribute('class')
