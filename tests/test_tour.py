import allure
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPaymentPage:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/")
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    @allure.feature("Позитивные сценарии")
    @allure.story("Оплата тура с валидной картой со статусом 'APPROVED'")
    @allure.title("Оплата тура с картой APPROVED - сценарий 1")
    def test_payment_with_approved_card_1(self):
        with allure.step("Нажать кнопку 'Купить'"):
            time.sleep(1)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Купить" in button.text:
                    button.click()
                    break
            time.sleep(1)

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 26, Test, 111"):
            field1 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.input__control[placeholder="0000 0000 0000 0000"]')))
            field1.send_keys("4444444444444441")
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

        with allure.step("Проверить появление всплывающего окна с текстом 'Операция одобрена Банком.'"):
            popup_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Операция одобрена Банком.')]")))
            assert popup_element.text == "Операция одобрена Банком."
            assert "Операция одобрена Банком." in popup_element.text

        with allure.step("Проверить запись со статусом 'APPROVED' в Response по API"):
            self.driver.execute_script("""
                    window.apiResponses = [];
                    const originalFetch = window.fetch;
                    window.fetch = function(...args) {
                        return originalFetch.apply(this, args).then(response => {
                            if (args[0].includes('/api/v1/pay')) {
                                response.clone().json().then(data => {
                                    window.apiResponses.push(data);
                                });
                            }
                            return response;
                        });
                    };
                """)
            api_responses = self.driver.execute_script("return window.apiResponses;")
            approved_found = False
            for response in api_responses:
                if response.get("status") == "APPROVED":
                    approved_found = True
                    allure.attach(json.dumps(response, indent=2), name="API Response with APPROVED")
                    break

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
            popup_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Операция одобрена Банком.')]")))
            assert popup_element.text == "Операция одобрена Банком."
            assert "Операция одобрена Банком." in popup_element.text

        with allure.step("Проверить запись со статусом 'APPROVED' в Response по API"):
            self.driver.execute_script("""
                                window.apiResponses = [];
                                const originalFetch = window.fetch;
                                window.fetch = function(...args) {
                                    return originalFetch.apply(this, args).then(response => {
                                        if (args[0].includes('/api/v1/pay')) {
                                            response.clone().json().then(data => {
                                                window.apiResponses.push(data);
                                            });
                                        }
                                        return response;
                                    });
                                };
                            """)
            api_responses = self.driver.execute_script("return window.apiResponses;")
            approved_found = False
            for response in api_responses:
                if response.get("status") == "APPROVED":
                    approved_found = True
                    allure.attach(json.dumps(response, indent=2), name="API Response with APPROVED")
                    break

    @allure.feature("Позитивные сценарии")
    @allure.story("Оплата тура в кредит с валидной картой со статусом 'APPROVED'")
    @allure.title("Оплата тура в кредит с картой APPROVED")
    def test_credit_payment_with_approved_card(self):
        with allure.step("Нажать кнопку 'Купить в кредит'"):
            time.sleep(1)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Купить в кредит" in button.text:
                    button.click()
                    break
            time.sleep(1)

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 26, Test, 111"):
            field1 = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input.input__control[placeholder="0000 0000 0000 0000"]')))
            field1.send_keys("4444444444444441")
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

        with allure.step("Проверить появление всплывающего окна с текстом 'Операция одобрена Банком.'"):
            popup_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Операция одобрена Банком.')]")))
            assert popup_element.text == "Операция одобрена Банком."
            assert "Операция одобрена Банком." in popup_element.text

        with allure.step("Проверить запись со статусом 'APPROVED' в Response по API"):
            self.driver.execute_script("""
                                            window.apiResponses = [];
                                            const originalFetch = window.fetch;
                                            window.fetch = function(...args) {
                                                return originalFetch.apply(this, args).then(response => {
                                                    if (args[0].includes('/api/v1/pay')) {
                                                        response.clone().json().then(data => {
                                                            window.apiResponses.push(data);
                                                        });
                                                    }
                                                    return response;
                                                });
                                            };
                                        """)
            api_responses = self.driver.execute_script("return window.apiResponses;")
            approved_found = False
            for response in api_responses:
                if response.get("status") == "APPROVED":
                    approved_found = True
                    allure.attach(json.dumps(response, indent=2), name="API Response with APPROVED")
                    break

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
            popup_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ошибка! Банк отказал в проведении операции.')]")))
            assert popup_element.text == "Ошибка! Банк отказал в проведении операции."
            assert "Ошибка! Банк отказал в проведении операции." in popup_element.text

        with allure.step("Проверить запись со статусом 'REJECTED' в Response по API"):
            self.driver.execute_script("""
                                                        window.apiResponses = [];
                                                        const originalFetch = window.fetch;
                                                        window.fetch = function(...args) {
                                                            return originalFetch.apply(this, args).then(response => {
                                                                if (args[0].includes('/api/v1/pay')) {
                                                                    response.clone().json().then(data => {
                                                                        window.apiResponses.push(data);
                                                                    });
                                                                }
                                                                return response;
                                                            });
                                                        };
                                                    """)
            api_responses = self.driver.execute_script("return window.apiResponses;")
            approved_found = False
            for response in api_responses:
                if response.get("status") == "REJECTED":
                    approved_found = True
                    allure.attach(json.dumps(response, indent=2), name="API Response with REJECTED")
                    break
            assert approved_found

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
            assert error_found

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
            element = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "input__sub"), "Неверно указан срок действия карты")
            )

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод невалидного CVC/CVV")
    @allure.title("Невалидный CVC/CVV (11)")
    def test_invalid_cvc(self):
        with allure.step("Нажать кнопку 'Купить'"):
            time.sleep(1)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Купить" in button.text:
                    button.click()
                    break
            time.sleep(1)

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 26, Test, 11"):
            field1 = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input.input__control[placeholder="0000 0000 0000 0000"]')))
            field1.send_keys("4444444444444441")
            field2 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="08"]')
            field2.send_keys("01")
            field3 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="22"]')
            field3.send_keys("26")
            field4 = self.driver.find_element(By.XPATH,
                                              '//*[contains(@class, "input__top") and contains(text(), "Владелец")]//following::input[1]')
            field4.send_keys("Test")
            field5 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="999"]')
            field5.send_keys("11")

        with allure.step("Нажать кнопку 'Продолжить'"):
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Продолжить" in button.text:
                    button.click()
                    break

        with allure.step("Проверить сообщение об ошибке под полем 'CVC/CVV'"):
            element = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "input__sub"), "Неверный формат")
            )

    @allure.feature("Негативные сценарии")
    @allure.story("Пустое поле 'Владелец'")
    @allure.title("Пустое поле владельца")
    def test_empty_cardholder(self):
        with allure.step("Нажать кнопку 'Купить'"):
            time.sleep(1)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Купить" in button.text:
                    button.click()
                    break
            time.sleep(1)

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 26, пустое поле владельца, 111"):
            field1 = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input.input__control[placeholder="0000 0000 0000 0000"]')))
            field1.send_keys("4444444444444441")
            field2 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="08"]')
            field2.send_keys("01")
            field3 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="22"]')
            field3.send_keys("26")
            field4 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="999"]')
            field4.send_keys("111")

        with allure.step("Нажать кнопку 'Продолжить'"):
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Продолжить" in button.text:
                    button.click()
                    break

        with allure.step("Проверить сообщение об ошибке под полем 'Владелец'"):
            element = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "input__sub"), "Поле обязательно для заполнения")
            )

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод данных просроченной карты")
    @allure.title("Просроченная карта (год 24)")
    def test_expired_card(self):
        with allure.step("Нажать кнопку 'Купить'"):
            time.sleep(1)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            for button in buttons:
                if "Купить" in button.text:
                    button.click()
                    break
            time.sleep(1)

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 24, Test, 111"):
            field1 = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input.input__control[placeholder="0000 0000 0000 0000"]')))
            field1.send_keys("4444444444444441")
            field2 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="08"]')
            field2.send_keys("01")
            field3 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="22"]')
            field3.send_keys("24")
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

        with allure.step("Проверить сообщение об ошибке под полем 'Год'"):
            element = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "input__sub"), "Истёк срок действия карты")
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--alluredir=allure-results"])