# Отчет о запуске автотестов

## Общая информация

- **Файл с тестами:** `test_tour.py`
- **Дата запуска:** 2025-11-04 22:40:07
- **Время завершения:** 2025-11-04 22:41:45
- **Общее время выполнения:** 0:01:38.410108

## Статистика

- **Всего тестов:** 9
- **Успешно:** 5
- **Провалено:** 4
- **Пропущено:** 0
- **Процент успешных:** 55.56%

## Проваленные тесты

### ❌ test_payment_with_approved_card_2
- **Время выполнения:** 12.81 сек
- **Ошибка:** 
```
self = <tests.test_tour.TestPaymentPage object at 0x000002163B46A210>

    @allure.feature("Позитивные сценарии")
    @allure.story("Оплата тура с валидной картой со статусом 'APPROVED'")
    @allure.title("Оплата тура с картой APPROVED - сценарий 2")
    def test_payment_with_approved_card_2(self):
        with allure.step("Нажать кнопку 'Купить'"):
            time.sleep(1)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Купить" in button.text:
                    button.click()
                    break
            time.sleep(1)
    
        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 31, Test, 111"):
            field1 = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input.input__control[placeholder="0000 0000 0000 0000"]')))
            field1.send_keys("4444444444444441")
            field2 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="08"]')
            field2.send_keys("01")
            field3 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="22"]')
            field3.send_keys("31")
            field4 = self.driver.find_element(By.XPATH,
                                              '//*[contains(@class, "input__top") and contains(text(), "Владелец")]//following::input[1]')
            field4.send_keys("Test")
            field5 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="999"]')
            field5.send_keys("111")
    
        with allure.step("Нажать кнопку 'Продолжить'"):
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Продолжить" in button.text:
                    button.click()
                    break
    
        with allure.step("Проверить появление всплывающего окна с текстом 'Операция одобрена Банком.'"):
>           popup_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Операция одобрена Банком.')]")))

tests\test_tour.py:115: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <selenium.webdriver.support.wait.WebDriverWait (session="3f0659a2e05401ad123e224914548f9f")>, method = <function visibility_of_element_located.<locals>._predicate at 0x000002163B487A60>, message = ''

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
- **Время выполнения:** 12.87 сек
- **Ошибка:** 
```
self = <tests.test_tour.TestPaymentPage object at 0x000002163B3FA060>

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод невалидного номера карты")
    @allure.title("Оплата с картой 4444 4444 4444 4442")
    def test_payment_with_declined_card_1(self):
        with allure.step("Нажать кнопку 'Купить'"):
            time.sleep(1)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Купить" in button.text:
                    button.click()
                    break
            time.sleep(1)
    
        with allure.step("Ввести данные карты: 4444 4444 4444 4442, 01, 26, Test, 111"):
            field1 = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input.input__control[placeholder="0000 0000 0000 0000"]')))
            field1.send_keys("4444444444444442")
            field2 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="08"]')
            field2.send_keys("01")
            field3 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="22"]')
            field3.send_keys("26")
            field4 = self.driver.find_element(By.XPATH,
                                              '//*[contains(@class, "input__top") and contains(text(), "Владелец")]//following::input[1]')
            field4.send_keys("Test")
            field5 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="999"]')
            field5.send_keys("111")
    
        with allure.step("Нажать кнопку 'Продолжить'"):
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Продолжить" in button.text:
                    button.click()
                    break
    
        with allure.step("Проверить появление всплывающего окна с текстом 'Ошибка! Банк отказал в проведении операции.'"):
>           popup_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ошибка! Банк отказал в проведении операции.')]")))

tests\test_tour.py:241: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <selenium.webdriver.support.wait.WebDriverWait (session="26beaac3c298f7c7403f54264aab8ff9")>, method = <function visibility_of_element_located.<locals>._predicate at 0x000002163B532F20>, message = ''

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

### ❌ test_payment_with_declined_card_2
- **Время выполнения:** 11.32 сек
- **Ошибка:** 
```
self = <tests.test_tour.TestPaymentPage object at 0x000002163B5B5B50>

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод невалидного номера карты")
    @allure.title("Оплата с картой 4444 4444 4444 4443")
    def test_payment_with_declined_card_2(self):
        with allure.step("Нажать кнопку 'Купить'"):
            time.sleep(1)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Купить" in button.text:
                    button.click()
                    break
            time.sleep(1)
    
        with allure.step("Ввести данные карты: 4444 4444 4444 4443, 01, 26, Test, 111"):
            field1 = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input.input__control[placeholder="0000 0000 0000 0000"]')))
            field1.send_keys("4444444444444443")
            field2 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="08"]')
            field2.send_keys("01")
            field3 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="22"]')
            field3.send_keys("26")
            field4 = self.driver.find_element(By.XPATH,
                                              '//*[contains(@class, "input__top") and contains(text(), "Владелец")]//following::input[1]')
            field4.send_keys("Test")
            field5 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="999"]')
            field5.send_keys("111")
    
        with allure.step("Нажать кнопку 'Продолжить'"):
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Продолжить" in button.text:
                    button.click()
                    break
    
        with allure.step(
                "Проверить появление всплывающего окна с текстом 'Ошибка! Банк отказал в проведении операции.'"):
            popup_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ошибка! Банк отказал в проведении операции.')]")))
            assert popup_element.text == "Ошибка! Банк отказал в проведении операции."
            assert "Ошибка! Банк отказал в проведении операции." in popup_element.text
    
        with allure.step("Проверить код ответа сервера 500 и сообщение 'Internal Server Error'"):
            self.driver.execute_script("window.apiResponses = [];")
            self.driver.execute_script("""
                const originalFetch = window.fetch;
                window.fetch = function(...args) {
                    return originalFetch.apply(this, args).then(response => {
                        if (typeof args[0] === 'string' && args[0].includes('/api/v1/pay')) {
                            response.clone().json().then(data => {
                                window.apiResponses.push(data);
                            });
                        }
                        return response;
                    });
                };
            """)
    
            api_responses = self.driver.execute_script("return window.apiResponses;")
    
            error_found = False
            for response in api_responses:
                print("Проверяем ответ:", response)
                if (response.get("status") == 500 and
                        response.get("error") == "Internal Server Error" and
                        response.get("message") == "Database connection failed"):
                    error_found = True
                    allure.attach(json.dumps(response, indent=2), name="API Response with Database Error")
                    break
>           assert error_found
E           assert False

tests\test_tour.py:338: AssertionError
```

### ❌ test_invalid_month
- **Время выполнения:** 5.64 сек
- **Ошибка:** 
```
self = <tests.test_tour.TestPaymentPage object at 0x000002163B441370>

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод невалидного срока действия карты")
    @allure.title("Невалидный месяц (00)")
    def test_invalid_month(self):
        with allure.step("Нажать кнопку 'Купить'"):
            time.sleep(1)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Купить" in button.text:
                    button.click()
                    break
            time.sleep(1)
    
        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 00, 26, Test, 111"):
            field1 = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input.input__control[placeholder="0000 0000 0000 0000"]')))
            field1.send_keys("4444444444444441")
            field2 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="08"]')
            field2.send_keys("00")
            field3 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="22"]')
            field3.send_keys("26")
            field4 = self.driver.find_element(By.XPATH,
                                              '//*[contains(@class, "input__top") and contains(text(), "Владелец")]//following::input[1]')
            field4.send_keys("Test")
            field5 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="999"]')
            field5.send_keys("111")
    
        with allure.step("Нажать кнопку 'Продолжить'"):
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Продолжить" in button.text:
                    button.click()
                    break
    
        with allure.step("Проверить сообщение об ошибке под полем 'Месяц'"):
>           element = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "input__sub"), "Неверно указан срок действия карты")
            )

tests\test_tour.py:375: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <selenium.webdriver.support.wait.WebDriverWait (session="0bf2782cf62806a22fc829db526b15ca")>, method = <function text_to_be_present_in_element.<locals>._predicate at 0x000002163B5327A0>, message = ''

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
E       	0x7ff667e77a35
E       	0x7ff667e77a90
E       	0x7ff667bf16ad
E       	0x7ff667c4a13e
E       	0x7ff667c4a44c
E       	0x7ff667c9ebe7
E       	0x7ff667c9b8fb
E       	0x7ff667c3b068
E       	0x7ff667c3be93
E       	0x7ff6681329d0
E       	0x7ff66812ce50
E       	0x7ff66814cc45
E       	0x7ff667e930ce
E       	0x7ff667e9adbf
E       	0x7ff667e80c14
E       	0x7ff667e80dcf
E       	0x7ff667e66828
E       	0x7ff94e45e8d7
E       	0x7ff94fa0c53c

..\..\PycharmProjects\PatternsAndBDD\.venv\Lib\site-packages\selenium\webdriver\support\wait.py:138: TimeoutException
```

## Успешные тесты

### ✅ test_payment_with_approved_card_1
- **Время выполнения:** 8.70 сек

### ✅ test_credit_payment_with_approved_card
- **Время выполнения:** 8.22 сек

### ✅ test_invalid_cvc
- **Время выполнения:** 2.49 сек

### ✅ test_empty_cardholder
- **Время выполнения:** 2.51 сек

### ✅ test_expired_card
- **Время выполнения:** 2.55 сек

## Сводка

❌ **Есть проваленные тесты, требуется исправление**
