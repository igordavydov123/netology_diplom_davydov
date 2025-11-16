# Отчет о запуске автотестов

## Общая информация

- **Файл с тестами:** `test_tour.py`
- **Дата запуска:** 2025-11-16 17:50:58
- **Время завершения:** 2025-11-16 17:52:28
- **Общее время выполнения:** 0:01:29.751128

## Статистика

- **Всего тестов:** 9
- **Успешно:** 5
- **Провалено:** 4
- **Пропущено:** 0
- **Процент успешных:** 55.56%

## Проваленные тесты

### ❌ test_payment_with_approved_card_2
- **Время выполнения:** 10.87 сек
- **Ошибка:** 
```
self = <tests.test_tour.TestPaymentPage object at 0x000001A297E12FD0>, db_connection = <pymysql.connections.Connection object at 0x000001A297E13B10>

    @allure.feature("Позитивные сценарии")
    @allure.story("Оплата тура с валидной картой со статусом 'APPROVED'")
    @allure.title("Оплата тура с картой APPROVED - сценарий 2")
    def test_payment_with_approved_card_2(self, db_connection):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()
    
        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 31, Test, 111"):
            payment_page.fill_card_data("4444 4444 4444 4441", "01", "31", "Test", "111")
    
        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()
    
        with allure.step("Проверить появление всплывающего окна с текстом 'Операция одобрена Банком.'"):
>           popup_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Операция одобрена Банком.')]")))

tests\test_tour.py:102: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <selenium.webdriver.support.wait.WebDriverWait (session="cd33be974490bd6a11a89f204c7a1e01")>, method = <function visibility_of_element_located.<locals>._predicate at 0x000001A297E83D80>, message = ''

    def until(self, method: Callable[[D], Union[Literal[False], T]], message: str = "") -> T:
        """Wait until the method returns a value that is not False.
    
        Calls the method provided with the driver as an argument until the
        return value does not evaluate to ``False``.
    
        Parameters:
        -----------
        method: callable(WebDriver)
            - A callable object that takes a WebDriver instance as an argument.
    
        message: str
            - Optional message for :exc:`TimeoutException`
    
        Return:
        -------
        object: T
            - The result of the last call to `method`
    
        Raises:
        -------
        TimeoutException
            - If 'method' does not return a truthy value within the WebDriverWait
            object's timeout
    
        Example:
        --------
        >>> from selenium.webdriver.common.by import By
        >>> from selenium.webdriver.support.ui import WebDriverWait
        >>> from selenium.webdriver.support import expected_conditions as EC
    
        # Wait until an element is visible on the page
        >>> wait = WebDriverWait(driver, 10)
        >>> element = wait.until(EC.visibility_of_element_located((By.ID, "exampleId")))
        >>> print(element.text)
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message:

..\..\PycharmProjects\PatternsAndBDD\.venv\Lib\site-packages\selenium\webdriver\support\wait.py:138: TimeoutException
```

### ❌ test_payment_with_declined_card_1
- **Время выполнения:** 10.86 сек
- **Ошибка:** 
```
self = <tests.test_tour.TestPaymentPage object at 0x000001A297DC5810>, db_connection = <pymysql.connections.Connection object at 0x000001A297EC4A50>

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод невалидного номера карты")
    @allure.title("Оплата с картой 4444 4444 4444 4442")
    def test_payment_with_declined_card_1(self, db_connection):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()
    
        with allure.step("Ввести данные карты: 4444 4444 4444 4442, 01, 26, Test, 111"):
            payment_page.fill_card_data("4444 4444 4444 4442", "01", "26", "Test", "111")
    
        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()
    
        with allure.step("Проверить появление всплывающего окна с текстом 'Ошибка! Банк отказал в проведении операции.'"):
>           popup_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ошибка! Банк отказал в проведении операции.')]")))

tests\test_tour.py:200: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <selenium.webdriver.support.wait.WebDriverWait (session="b826c543324f73390e6cabbe67c96420")>, method = <function visibility_of_element_located.<locals>._predicate at 0x000001A297EECB80>, message = ''

    def until(self, method: Callable[[D], Union[Literal[False], T]], message: str = "") -> T:
        """Wait until the method returns a value that is not False.
    
        Calls the method provided with the driver as an argument until the
        return value does not evaluate to ``False``.
    
        Parameters:
        -----------
        method: callable(WebDriver)
            - A callable object that takes a WebDriver instance as an argument.
    
        message: str
            - Optional message for :exc:`TimeoutException`
    
        Return:
        -------
        object: T
            - The result of the last call to `method`
    
        Raises:
        -------
        TimeoutException
            - If 'method' does not return a truthy value within the WebDriverWait
            object's timeout
    
        Example:
        --------
        >>> from selenium.webdriver.common.by import By
        >>> from selenium.webdriver.support.ui import WebDriverWait
        >>> from selenium.webdriver.support import expected_conditions as EC
    
        # Wait until an element is visible on the page
        >>> wait = WebDriverWait(driver, 10)
        >>> element = wait.until(EC.visibility_of_element_located((By.ID, "exampleId")))
        >>> print(element.text)
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message:

..\..\PycharmProjects\PatternsAndBDD\.venv\Lib\site-packages\selenium\webdriver\support\wait.py:138: TimeoutException
```

### ❌ test_invalid_month
- **Время выполнения:** 3.60 сек
- **Ошибка:** 
```
self = <tests.test_tour.TestPaymentPage object at 0x000001A297E548D0>

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод невалидного срока действия карты")
    @allure.title("Невалидный месяц (00)")
    def test_invalid_month(self):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()
    
        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 00, 26, Test, 111"):
            payment_page.fill_card_data("4444 4444 4444 4441", "00", "26", "Test", "111")
    
        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()
    
        with allure.step("Проверить сообщение об ошибке под полем 'Месяц'"):
>           element = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "input__sub"), "Неверно указан срок действия карты")
            )

tests\test_tour.py:296: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <selenium.webdriver.support.wait.WebDriverWait (session="e13febb3b5446b8616d44b8b63b2ffb7")>, method = <function text_to_be_present_in_element.<locals>._predicate at 0x000001A297EEDB20>, message = ''

    def until(self, method: Callable[[D], Union[Literal[False], T]], message: str = "") -> T:
        """Wait until the method returns a value that is not False.
    
        Calls the method provided with the driver as an argument until the
        return value does not evaluate to ``False``.
    
        Parameters:
        -----------
        method: callable(WebDriver)
            - A callable object that takes a WebDriver instance as an argument.
    
        message: str
            - Optional message for :exc:`TimeoutException`
    
        Return:
        -------
        object: T
            - The result of the last call to `method`
    
        Raises:
        -------
        TimeoutException
            - If 'method' does not return a truthy value within the WebDriverWait
            object's timeout
    
        Example:
        --------
        >>> from selenium.webdriver.common.by import By
        >>> from selenium.webdriver.support.ui import WebDriverWait
        >>> from selenium.webdriver.support import expected_conditions as EC
    
        # Wait until an element is visible on the page
        >>> wait = WebDriverWait(driver, 10)
        >>> element = wait.until(EC.visibility_of_element_located((By.ID, "exampleId")))
        >>> print(element.text)
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       Symbols not available. Dumping unresolved backtrace:
E       	0x7ff7aed0a235
E       	0x7ff7aea62650
E       	0x7ff7ae7f16dd
E       	0x7ff7ae84a27e
E       	0x7ff7ae84a58c
E       	0x7ff7ae89ed77
E       	0x7ff7ae89baba
E       	0x7ff7ae83b0ed
E       	0x7ff7ae83bf63
E       	0x7ff7aed35d60
E       	0x7ff7aed2fe8a
E       	0x7ff7aed51005
E       	0x7ff7aea7d73e
E       	0x7ff7aea84e3f
E       	0x7ff7aea6b7e4
E       	0x7ff7aea6b99f
E       	0x7ff7aea51908
E       	0x7ff9cda5e8d7
E       	0x7ff9cfc0c53c

..\..\PycharmProjects\PatternsAndBDD\.venv\Lib\site-packages\selenium\webdriver\support\wait.py:138: TimeoutException
```

### ❌ test_empty_cardholder
- **Время выполнения:** 10.33 сек
- **Ошибка:** 
```
self = <tests.test_tour.TestPaymentPage object at 0x000001A297E48E50>

    @allure.feature("Негативные сценарии")
    @allure.story("Пустое поле 'Владелец'")
    @allure.title("Пустое поле владельца")
    def test_empty_cardholder(self):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()
    
        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 26, пустое поле владельца, 111"):
>           payment_page.fill_card_data("4444 4444 4444 4441", "01", "26", "", "111")

tests\test_tour.py:328: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
pages\payment_page.py:29: in fill_card_data
    field1 = self.wait.until(EC.visibility_of_element_located(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <selenium.webdriver.support.wait.WebDriverWait (session="8de6ad41b0febdf558f1a1deb4231504")>, method = <function visibility_of_element_located.<locals>._predicate at 0x000001A297EEDC60>, message = ''

    def until(self, method: Callable[[D], Union[Literal[False], T]], message: str = "") -> T:
        """Wait until the method returns a value that is not False.
    
        Calls the method provided with the driver as an argument until the
        return value does not evaluate to ``False``.
    
        Parameters:
        -----------
        method: callable(WebDriver)
            - A callable object that takes a WebDriver instance as an argument.
    
        message: str
            - Optional message for :exc:`TimeoutException`
    
        Return:
        -------
        object: T
            - The result of the last call to `method`
    
        Raises:
        -------
        TimeoutException
            - If 'method' does not return a truthy value within the WebDriverWait
            object's timeout
    
        Example:
        --------
        >>> from selenium.webdriver.common.by import By
        >>> from selenium.webdriver.support.ui import WebDriverWait
        >>> from selenium.webdriver.support import expected_conditions as EC
    
        # Wait until an element is visible on the page
        >>> wait = WebDriverWait(driver, 10)
        >>> element = wait.until(EC.visibility_of_element_located((By.ID, "exampleId")))
        >>> print(element.text)
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            if time.monotonic() > end_time:
                break
            time.sleep(self._poll)
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       Symbols not available. Dumping unresolved backtrace:
E       	0x7ff7aed0a235
E       	0x7ff7aea62650
E       	0x7ff7ae7f16dd
E       	0x7ff7ae84a27e
E       	0x7ff7ae84a58c
E       	0x7ff7ae89ed77
E       	0x7ff7ae89baba
E       	0x7ff7ae83b0ed
E       	0x7ff7ae83bf63
E       	0x7ff7aed35d60
E       	0x7ff7aed2fe8a
E       	0x7ff7aed51005
E       	0x7ff7aea7d73e
E       	0x7ff7aea84e3f
E       	0x7ff7aea6b7e4
E       	0x7ff7aea6b99f
E       	0x7ff7aea51908
E       	0x7ff9cda5e8d7
E       	0x7ff9cfc0c53c

..\..\PycharmProjects\PatternsAndBDD\.venv\Lib\site-packages\selenium\webdriver\support\wait.py:138: TimeoutException
```

## Успешные тесты

### ✅ test_payment_with_approved_card_1
- **Время выполнения:** 6.98 сек

### ✅ test_credit_payment_with_approved_card
- **Время выполнения:** 4.15 сек

### ✅ test_payment_with_declined_card_2
- **Время выполнения:** 10.29 сек

### ✅ test_invalid_cvc
- **Время выполнения:** 0.79 сек

### ✅ test_expired_card
- **Время выполнения:** 0.58 сек

## Сводка

❌ **Есть проваленные тесты, требуется исправление**
