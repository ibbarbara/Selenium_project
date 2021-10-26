import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


# DANE TESTOWE
product = "ARMANI My Way"


class ProductToBasket(unittest.TestCase):
    def setUp(self):
        print("Praca nad testem")
        s = Service("/Users/bbars/Documents/Mentoring/Mentoring2/selenium/chromedriver")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://www.sephora.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(40)

    def tearDown(self):
        print("Sprzatanie")
        self.driver.quit()

    def testValidData2(self):
        driver = self.driver
        cookies_input = driver.find_element(
            By.XPATH, '//button[@id="footer_tc_privacy_button_2"]'
        )
        cookies_input.click()

        account_btn = driver.find_element(By.XPATH, '//div[@id="header-item-account"]')
        account_btn.click()
        searching_btn = driver.find_element(By.ID, "fake-search-input")
        driver.execute_script("arguments[0].click();", searching_btn)
        searching_box_btn = driver.find_element(
            By.XPATH, '//div[@class="input-box"]//input[@id="q"]'
        )
        searching_box_btn.send_keys(product + Keys.ENTER)
        product_btn = driver.find_element(
            By.CSS_SELECTOR, 'a[title="My Way - Woda perfumowana"]'
        )
        product_btn.click()
        products_btn1 = driver.find_element(By.CSS_SELECTOR, 'a[title="90 ml"]')
        products_btn1.click()
        sleep(3)
        add_to_basket = driver.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart"]')
        add_to_basket.click()
        order_details_btn = driver.find_element(
            By.XPATH, '//a[@class="show-cart button important"]'
        )
        order_details_btn.click()


if __name__ == "__main__":
    unittest.main(verbosity=2)
