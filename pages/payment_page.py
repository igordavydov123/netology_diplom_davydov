from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_payment_form_pay(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
        for button in buttons:
            if "Купить" in button.text:
                button.click()
                break
        return self

    def open_payment_form_credit(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
        for button in buttons:
            if "Купить в кредит" in button.text:
                button.click()
                break
        return self

    def fill_card_data(self, card_number, month, year, holder, cvc):
        field1 = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'input.input__control[placeholder="0000 0000 0000 0000"]')))
        field1.send_keys(card_number)
        field2 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="08"]')
        field2.send_keys(month)
        field3 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="22"]')
        field3.send_keys(year)
        field4 = self.driver.find_element(By.XPATH,
                                          '//*[contains(@class, "input__top") and contains(text(), "Владелец")]//following::input[1]')
        field4.send_keys(holder)
        field5 = self.driver.find_element(By.CSS_SELECTOR, 'input.input__control[placeholder="999"]')
        field5.send_keys(cvc)

    def submit(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
        for button in buttons:
            if "Продолжить" in button.text:
                button.click()
                break
        return self