import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils


class CompareItemsPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    CHOOSE_BRAND_DD_FIELD = "//div[@class='col-2-5']/div[@class='col col-6-12'][1]//div[contains(text(),'Choose Brand')]"
    CHOOSE_PRODUCT_DD_FIELD = "//div[@class='col-2-5']/div[@class='col col-6-12'][1]//div[contains(text(),'Choose a Product')]"
    BRAND_NAME_DD_LIST_FIELD = "//div[@class='_1z5ndO']//div[@class='vd8GqM']"
    PRODUCT_NAME_DD_LIST_FIELD = "//div[@class='_3mL9c2']//div[@class='vd8GqM']"
    SHOW_DIFF_CHECKBOX_FIELD = "//div[@class='_24_Dny']" #"//label[@class='_2iDkf8']"  # "//div[@class='_24_Dny']"//input[@class='_30VH1S']
    ITEM_TO_REPLACE_XPATH_FIELD = "//div[contains(text(),'text to replace')]//..//..//..//span//input[@type='checkbox']"
    ITEM_ADD_TO_COMPARE_FIELD = ""
    COMPARE_PAGE_LINK = "//a[@class='_11o22n _87aCMT']"
    PRICE_LIST_COMPARE_ITEM = "//div[@class='col col-3-12 _1Z-FPJ']//div[@class='_30jeq3']"

    # Methods to get the fields
    def getChooseBrandDDField(self):
        return self.wait_for_presence_of_element(By.XPATH, self.CHOOSE_BRAND_DD_FIELD)

    def getChooseProductDDField(self):
        return self.wait_for_presence_of_element(By.XPATH, self.CHOOSE_PRODUCT_DD_FIELD)

    def getBrandNameDDListField(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.BRAND_NAME_DD_LIST_FIELD)

    def getProductNameDDListField(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.PRODUCT_NAME_DD_LIST_FIELD)

    def getShowDiffCheckBoxField(self):
        return self.wait_for_presence_of_element(By.XPATH, self.SHOW_DIFF_CHECKBOX_FIELD)

    def getPriceListCompareItems(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.PRICE_LIST_COMPARE_ITEM)

    # Methods to interact with elements
    def chooseBrand(self, item_input):
        self.getChooseBrandDDField().click()
        brand_name = self.getBrandNameDDListField()
        # Need to click on the brand_name field and then the list of items that appear capture all those and then iterate through that list
        for item in brand_name:
            self.log.debug("Item is {0}".format(item.text))
            if item_input == item.text:
                self.log.debug("Clicked on {0}".format(item.text))
                # item.click()
                self.driver.execute_script("arguments[0].click()", item)
                break

    def chooseProduct(self, item_input):
        self.getChooseProductDDField().click()
        product_name = self.getProductNameDDListField()
        for item in product_name:
            self.log.debug("Item is {0}".format(item.text))
            if item_input == item.text:
                self.log.debug("Clicked on {0}".format(item.text))
                # item.click()
                self.driver.execute_script("arguments[0].click()", item)
                break

    def checkShowDiff(self):
        diff_checkbox = self.getShowDiffCheckBoxField().find_element(By.XPATH,self.SHOW_DIFF_CHECKBOX_FIELD)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click()", diff_checkbox)

    # Methods to perform the tests

    def addAProduct(self, item_name_1, item_name_2):
        self.chooseBrand(item_name_1)
        self.chooseProduct(item_name_2)
        self.checkShowDiff()
        time.sleep(2)
        return self.getPriceListCompareItems()
