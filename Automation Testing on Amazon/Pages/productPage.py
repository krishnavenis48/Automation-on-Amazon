from Project_04.Locators.locators import Locators
import time


class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.product_link_xpath = Locators.product_link_xpath
        self.add_cart_button_xpath = Locators.add_cart_button_xpath

    def click_product(self):
        self.driver.find_element_by_xpath(self.product_link_xpath).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)

    def click_add_cart(self):
        self.driver.find_element_by_xpath(self.add_cart_button_xpath).click()
        time.sleep(5)