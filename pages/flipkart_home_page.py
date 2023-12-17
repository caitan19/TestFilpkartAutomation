import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver

from utilities.utils import Utils


class HomePage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    CLOSE_LOGIN_POPUP_FIELD = "//span[@role='button']"
    SEARCH_BOX_FIELD = "//input[@placeholder='Search for Products, Brands and More']"
    SEARCH_RESULTS_LIST = "//div[@class='_2x2Mmc']" #"//div//ul[contains(@class, '_2x2Mmc')]" #"//div[@class='_3ZqtNW']//li"

    # Methods to get the fields
    def getLoginPopupField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CLOSE_LOGIN_POPUP_FIELD)

    def getSearchBoxField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_BOX_FIELD)

    def getSearchResultsList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_RESULTS_LIST)

    # Methods to perform the tests
    def clickLoginCloseBtn(self):
        self.getLoginPopupField().click()

    def inputSearchItem(self, search_input):
        search_item = self.getSearchBoxField()
        self.driver.execute_script("arguments[0].click()", search_item)
        time.sleep(2)
        search_item.send_keys(search_input)
        search_item.send_keys(Keys.ENTER)
        '''listResults = self.getSearchResultsList()
        for result in listResults:
            if search_input == result.text:
                # self.log.debug("Clicked on {0}".format(result.text))
                result.click()
                break'''

    # execution function
    def SearchProduct(self, search_input):
        self.clickLoginCloseBtn()
        self.inputSearchItem(search_input)
