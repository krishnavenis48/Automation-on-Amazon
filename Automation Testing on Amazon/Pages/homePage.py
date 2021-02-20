from Project_04.Locators.locators import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.SearchBox_textbox_id = Locators.SearchBox_textbox_id
        self.Search_button_xpath = Locators.Search_button_xpath

    def enter_product(self, product):
        self.driver.find_element_by_id(self.SearchBox_textbox_id).clear()
        self.driver.find_element_by_id(self.SearchBox_textbox_id).send_keys(product)

    def click_search(self):
        self.driver.find_element_by_xpath(self.Search_button_xpath).click()
