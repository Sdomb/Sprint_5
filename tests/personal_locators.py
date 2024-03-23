from selenium.webdriver.common.by import By


class PersonalArea:
    """Текст кнопки Личный Кабинет на главной странице"""
    my_office = (By.XPATH, './/a[@class="AppHeader_header__link__3D_hX"]/p[text() ="Личный Кабинет"]')

    """ Текст кнопки Конструктор на главной странице """
    my_constructor = (By.XPATH, './/p[@class = "AppHeader_header__linkText__3q_va ml-2" and text() = "Конструктор"]')

    """Хедер блока регистрации с текстом 'Регистрация' """
    registration_header_locator = (By.XPATH, '//h2[text()="Регистрация"]')

    """Плейсхолдер и поле ввода 'Имя' в блоке Регистрации"""
    name_input_locator = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')

    """Плейсхолдер и поле ввода 'Email' в блоке Регистрации"""
    email_input_locator = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    """Плейсхолдер и поле ввода 'Password' в блоке Регистрации"""
    password_input_locator = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')

    """Кнопка регистрации в блоке регистрации нового пользователя """
    register_button = (By.XPATH, '//button[@class =  "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Зарегистрироваться"]')

    """Кнопка-гиперссылка 'Зарегистрироваться' """
    register_link_button = (By.CSS_SELECTOR, 'a.Auth_link__1fOlj[href="/register"]')

    """Кнопка-гиперссылка 'Войти' на страничке регистрации пользователя """
    register_input_link_button = (By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Войти"]')

    """Кнопка-гиперссылка 'Восстановить пароль' на страничке регистрации пользователя """
    recovery_pass_link_button = (By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Восстановить пароль"]')

    """Хедер странички Восстановления пароля"""
    recovery_pass_header = (By.XPATH, '//h2[text()="Восстановление пароля" ]')

    """Красная подсветка поля ввода пароля"""
    input_status_error = (
    By.XPATH, './/div[@class = "input pr-6 pl-6 input_type_password input_size_default input_status_error"]')

    """Текст 'Некорректный пароль' под полем ввода для пароля"""
    error_message_locator = (
    By.XPATH, '//p[@class="input__error text_type_main-default" and text()="Некорректный пароль"]')

    """Хедер блока входа с текстом 'Вход' """
    login_header_in_my_office = (By.XPATH, './/h2[text() = "Вход"]')

    """Кнопка Войти в блоке входа"""
    login_button_in_my_office = (By.XPATH, './/form/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text() = "Войти" ]')

    """Кнопка Выход в личном кабинете"""
    logout_button_in_my_office = (
    By.CSS_SELECTOR, 'button.Account_button__14Yp3.text.text_type_main-medium.text_color_inactive')

    """Кнопка 'Войти в Аккаунт на главной странице' """
    login_button_for_home = (By.XPATH, './/div/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')

    """Заголовок СОБЕРИТЕ БУРГЕР на странице конструктора """
    constructor_title = (By.CSS_SELECTOR, 'h1.text.text_type_main-large.mb-5.mt-10')

    """Хедер StellarBurgers на главной странице"""
    app_main_stellar_header = (By.CSS_SELECTOR, 'div.AppHeader_header__logo__2D0X2')

    """Кнопка раздела Булки на странице конструкторов бургеров"""
    buns_button_section = (By.XPATH, './/span[@class = "text text_type_main-default" and text() = "Булки"]')

    """"Кнопка раздела Соусы на странице конструкторов бургеров"""
    sauce_button_section = (By.XPATH, './/span[@class = "text text_type_main-default" and text() = "Соусы"]')

    """Кнопка раздел Начинки на странице конструкторов бургеров"""
    fillings_button_section = (By.XPATH, './/span[@class = "text text_type_main-default" and text() = "Начинки"]')

    """Родительский локтаор кнопки Булки в контейнере меню конструктора бургеров"""
    parent_buns_btn_section = (By.XPATH, './/span[@class = "text text_type_main-default" and text() = "Булки"]/..')

    """Родительский локтаор кнопки Соус в контейнере меню конструктора бургеров"""
    parent_sauce_btn_section = (By.XPATH, './/span[@class = "text text_type_main-default" and text() = "Соусы"]/..')

    """Родительский локтаор кнопки Начинки в контейнере меню конструктора бургеров"""
    parent_fillings_btn_section = (By.XPATH, './/span[@class = "text text_type_main-default" and text() = "Начинки"]/..')

