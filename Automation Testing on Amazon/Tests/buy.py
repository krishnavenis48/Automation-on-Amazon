import HtmlTestRunner
from selenium import webdriver
import time
import unittest
from Project_04.Pages.homePage import HomePage
from Project_04.Pages.productPage import ProductPage
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class Amazon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/home/jackdaniel/PycharmProjects/selenium/Project_04/Driver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_add_to_Cart(self):
        driver = self.driver
        driver.get("https://www.amazon.in/")

        homepage = HomePage(driver)
        homepage.enter_product("Bluetooth earphones")
        homepage.click_search()

        product_page = ProductPage(driver)
        product_page.click_product()
        product_page.click_add_cart()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="/home/jackdaniel/PycharmProjects/selenium/Project_04/Reports"))
