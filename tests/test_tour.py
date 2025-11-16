import allure
import pytest
import json
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.payment_page import PaymentPage

class TestPaymentPage:
    @pytest.fixture(autouse=True)
    def setup(self, log_api_requests):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/")
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    @pytest.fixture
    def db_connection(self):
        conn = None
        try:
            conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='app',
                password='pass',
                database='app',
                charset='utf8mb4',
            )
            yield conn
        except pymysql.Error as e:
            pytest.fail(f"Database connection failed: {e}")
        finally:
            if conn:
                conn.close()

    @allure.feature("Позитивные сценарии")
    @allure.story("Оплата тура с валидной картой со статусом 'APPROVED'")
    @allure.title("Оплата тура с картой APPROVED - сценарий 1")
    def test_payment_with_approved_card_1(self, db_connection, api_logger, db_snapshot):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 26, Test, 111"):
            payment_page.fill_card_data("4444 4444 4444 4441", "01", "26", "Test", "111")

        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()

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

        with allure.step("Проверить запись в БД"):
            with db_connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM payment_entity WHERE status = 'APPROVED'")
                count = cursor.fetchone()[0]
                assert count > 0

    @allure.feature("Позитивные сценарии")
    @allure.story("Оплата тура с валидной картой со статусом 'APPROVED'")
    @allure.title("Оплата тура с картой APPROVED - сценарий 2")
    def test_payment_with_approved_card_2(self, db_connection, api_logger, db_snapshot):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 31, Test, 111"):
            payment_page.fill_card_data("4444 4444 4444 4441", "01", "31", "Test", "111")

        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()

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

        with allure.step("Проверить запись в БД"):
            with db_connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM payment_entity WHERE status = 'APPROVED'")
                count = cursor.fetchone()[0]
                assert count > 0

    @allure.feature("Позитивные сценарии")
    @allure.story("Оплата тура в кредит с валидной картой со статусом 'APPROVED'")
    @allure.title("Оплата тура в кредит с картой APPROVED")
    def test_credit_payment_with_approved_card(self, db_connection, api_logger, db_snapshot):
        with allure.step("Нажать кнопку 'Купить в кредит'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_credit()

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 26, Test, 111"):
            payment_page.fill_card_data("4444 4444 4444 4441", "01", "26", "Test", "111")

        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()

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

        with allure.step("Проверить запись в БД"):
            with db_connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM credit_request_entity WHERE status = 'APPROVED'")
                count = cursor.fetchone()[0]
                assert count > 0

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод невалидного номера карты")
    @allure.title("Оплата с картой 4444 4444 4444 4442")
    def test_payment_with_declined_card_1(self, db_connection, api_logger, db_snapshot):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()

        with allure.step("Ввести данные карты: 4444 4444 4444 4442, 01, 26, Test, 111"):
            payment_page.fill_card_data("4444 4444 4444 4442", "01", "26", "Test", "111")

        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()

        with allure.step("Проверить появление всплывающего окна с текстом 'Ошибка! Банк отказал в проведении операции.'"):
            popup_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ошибка! Банк отказал в проведении операции.')]")))
            assert popup_element.text == "Ошибка! Банк отказал в проведении операции."
            assert "Ошибка! Банк отказал в проведении операции." in popup_element.text

        with allure.step("Проверить запись со статусом 'DECLINED' в Response по API"):
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
            declined_found = False
            for response in api_responses:
                if response.get("status") == "DECLINED":
                    declined_found = True
                    allure.attach(json.dumps(response, indent=2), name="API Response with DECLINED")
                    break
            assert declined_found

        with allure.step("Проверить запись в БД"):
            with db_connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM payment_entity WHERE status = 'DECLINED'")
                count = cursor.fetchone()[0]
                assert count > 0

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод невалидного номера карты")
    @allure.title("Оплата с картой 4444 4444 4444 4443")
    def test_payment_with_declined_card_2(self, api_logger, db_snapshot):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()

        with allure.step("Ввести данные карты: 4444 4444 4444 4443, 01, 26, Test, 111"):
            payment_page.fill_card_data("4444 4444 4444 4443", "01", "26", "Test", "111")

        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()

        with allure.step(
                "Проверить появление всплывающего окна с текстом 'Ошибка! Банк отказал в проведении операции.'"):
            popup_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ошибка! Банк отказал в проведении операции.')]")))
            assert popup_element.text == "Ошибка! Банк отказал в проведении операции."
            assert "Ошибка! Банк отказал в проведении операции." in popup_element.text

        with allure.step("Проверить запись со статусом 'DECLINED' в Response по API"):
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
            declined_found = False
            for response in api_responses:
                if response.get("status") == "DECLINED":
                    declined_found = True
                    allure.attach(json.dumps(response, indent=2), name="API Response with DECLINED")
                    break
            assert declined_found

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод невалидного срока действия карты")
    @allure.title("Невалидный месяц (00)")
    def test_invalid_month(self, api_logger, db_snapshot):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 00, 26, Test, 111"):
            payment_page.fill_card_data("4444 4444 4444 4441", "00", "26", "Test", "111")

        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()

        with allure.step("Проверить сообщение об ошибке под полем 'Месяц'"):
            element = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "input__sub"), "Неверно указан срок действия карты")
            )

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод невалидного CVC/CVV")
    @allure.title("Невалидный CVC/CVV (11)")
    def test_invalid_cvc(self, api_logger, db_snapshot):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 26, Test, 11"):
            payment_page.fill_card_data("4444 4444 4444 4441", "01", "26", "Test", "11")

        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()

        with allure.step("Проверить сообщение об ошибке под полем 'CVC/CVV'"):
            element = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "input__sub"), "Неверный формат")
            )

    @allure.feature("Негативные сценарии")
    @allure.story("Пустое поле 'Владелец'")
    @allure.title("Пустое поле владельца")
    def test_empty_cardholder(self, api_logger, db_snapshot):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 26, пустое поле владельца, 111"):
            payment_page.fill_card_data("4444 4444 4444 4441", "01", "26", "", "111")

        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()

        with allure.step("Проверить сообщение об ошибке под полем 'Владелец'"):
            element = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "input__sub"), "Поле обязательно для заполнения")
            )

    @allure.feature("Негативные сценарии")
    @allure.story("Ввод данных просроченной карты")
    @allure.title("Просроченная карта (год 24)")
    def test_expired_card(self, api_logger, db_snapshot):
        with allure.step("Нажать кнопку 'Купить'"):
            payment_page = PaymentPage(self.driver)
            payment_page.open_payment_form_pay()

        with allure.step("Ввести данные карты: 4444 4444 4444 4441, 01, 24, Test, 111"):
            payment_page.fill_card_data("4444 4444 4444 4441", "01", "24", "Test", "111")

        with allure.step("Нажать кнопку 'Продолжить'"):
            payment_page.submit()

        with allure.step("Проверить сообщение об ошибке под полем 'Год'"):
            element = WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "input__sub"), "Истёк срок действия карты")
            )

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--alluredir=allure-results"])