import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# DANE TESTOWE

email = "Testing129@gmail.com"
password = "1@Zakupy"
gender = "female"
name = "Barbara"
surname = "Test"


class SephoraRegistration(unittest.TestCase):
    def setUp(self):
        print("Praca nad testem")
        s = Service("/Users/bbars/Documents/Mentoring/Mentoring2/selenium/chromedriver")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://sephora.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(40)

    def tearDown(self):
        print("Sprzatanie")
        self.driver.quit()

    def testValidData(self):
        driver = self.driver

        cookies_input = driver.find_element(
            By.XPATH, '//button[@id="footer_tc_privacy_button_2"]'
        )
        cookies_input.click()
        account_btn = driver.find_element(By.XPATH, '//div[@id="header-item-account"]')
        account_btn.click()
        registration_btn = driver.find_element(
            By.XPATH,
            '//button[@class="js-create-account-button button button-important fullwidth"]',
        )
        registration_btn.click()

        sleep(2)
        email_input = driver.find_element(
            By.XPATH,
            '//input[@class="required emailAlreadyInUse input-text ui-autocomplete-input"]',
        )
        email_input.send_keys(email)
        confirmation_input = driver.find_element(
            By.CSS_SELECTOR, "button[name=dwfrm_profile_checkemail]"
        )
        confirmation_input.click()
        name_btn = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.NAME, "dwfrm_profile_customer_firstname")
            )
        )
        name_btn.send_keys(name)
        surname_btn = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.NAME, "dwfrm_profile_customer_lastname")
            )
        )
        surname_btn.send_keys(surname)
        password_btn = driver.find_element(
            By.XPATH, '//input[@class="password-strength-bar input-text"]'
        )
        password_btn.send_keys(password)
        if gender == "female":
            gender_btn = driver.find_element(
                By.XPATH, '//label[@for="dwfrm_profile_customer_gender-0"]'
            )
            gender_btn.click()
        elif gender == "male":
            gender_btn = driver.find_element(
                By.XPATH, '//label[@for="dwfrm_profile_customer_gender-1"]'
            )
            gender_btn.click()
        else:
            print("Please provide female or male!")
        confirmation1_btn = driver.find_element(
            By.XPATH, '//label[@for="dwfrm_profile_customer_subscribedbyemail"]'
        )
        confirmation1_btn.click()
        confirmation2_btn = driver.find_element(
            By.XPATH, '//input[@class=" required input-checkbox"]'
        )
        driver.execute_script("arguments[0].click();", confirmation2_btn)
        main_confirmation_btn = driver.find_element(
            By.CSS_SELECTOR,
            'button[class="button fullwidth button-important button-multiline enable-button"]',
        )
        main_confirmation_btn.click()


if __name__ == "__main__":
    unittest.main(verbosity=2)
