import time

import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from utilities.utils import Utils


class ItemDetailPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    ADD_TO_CART_BTN_FIELD = "//li/button"

    # Methods to get the fields
    def getAddToCartBtnField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADD_TO_CART_BTN_FIELD)

    # Methods to interact with elements
    def clickAddToCartBtn(self):
        self.getAddToCartBtnField().click()
        # self.getAddToCartBtnField().click()
        # self.driver.execute_script("arguments[0].click()", add_btn)
        self.log.debug("Add to cart button clicked.")
        time.sleep(5)

    # Methods to perform the tests
