# Sprint_5 - Покрытие атвотестами вебморды
MVP проекта, суть которого заключается в покрытии ui-автотестами сайта по заданию.

### Требуется проверить:

- Успешную регистрацию 
- Ошибку для некорректного пароля
- вход по кнопке «Войти в аккаунт» на главной
- вход через кнопку «Личный кабинет»,
- вход через кнопку в форме регистрации,
- вход через кнопку в форме восстановления пароля
- переход по клику на «Личный кабинет».
- переход по клику на «Конструктор» и на логотип Stellar Burgers.
- что работают переходы к разделам:«Булки», «Соусы», «Начинки»
- выход по кнопке «Выйти» в личном кабинете.



## Содержание
- [conftest](#conftest)
- [test_actions](#test_actions)
- [personal_locators](#personal_locators)
- [registration_tests](#registration_tests)
- [login_tests](#login_tests)
- [transition_tests](#transition_tests)
- [logout_tests](#logout_tests)


## conftest

Содержит стартовую фикстуру и создает клас локаторов



## test_actions
В этот файл вынесена авторизация и проверка успешного логина 

``` 
login_actions

```

## personal_locators

В этом файле собраны локаторы в виде функций с декоратором property.
Так же для удобства в функции уже добавлены селекторы поиска.


## registration_tests
Содержит в себе две функции, первая проверяет успешную регистрацию и валидность пароля:
```
def test_successful_registration(self, driver, lk)
```


вторая проверяют получение ошибки если введённый пароль не соответствует требованиям
```
def test_fail_registration_because_pass(self, driver, lk)
```

## login_tests
В этом файле лежат четыре функции которые проверяют логины на сайте через различные кнопки входа.

```
def test_login_in_account_button(self, driver, lk):
def test_login_in_personal_area_button(self, driver, lk):
def test_login_in_registration_button(self, driver, lk):
def test_login_in_recovery_button(self, driver, lk):
```
Чтобы уменьшить количество кода, авторизация и проверка залогинености вынесена в отдельный экшшн.


## transition_tests
В этом файле находятся тесты, которые проверят переходы по кликам. 


Переход по клику на «Конструктор» 
```
test_transition_tap_on_constructor
```
Переход по клику на логотип Stellar Burgers
```
test_transition_tap_on_stellar
```
Переход к разделу Булки 
```
 test_transition_tap_on_buns
```
Переход к разделу Соусы
```
test_transition_tap_on_sauce
```
Переход к разделу Начинки 
```
test_transition_tap_on_fillings
```



## logout_tests
В этом файле находится тест на проверку разлогина

```
test_logout

```
