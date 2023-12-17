import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchResultsPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    ITEM_SEARCH_RESULTS_LIST = "//div[contains(text(),'SAMSUNG Galaxy')]"
    LEFT_PRICE_SLIDER = "//div[@class='_31Kbhn WC_zGJ']//div[@class='_3FdLqY']"
    FOUR_GB_RAM_CHECKBOX_FIELD = "//div[@title='4 GB']"
    EXPAND_INTERNAL_STORAGE_LIST = "//div//div[contains(text(),'Internal Storage')]"
    ONE_TWO_EIGHT_GB_INT_STORAGE_FIELD = "//div//div[contains(text(),'128 - 255.9 GB')]"
    ALL_RATINGS_FIELDS = "//div[@class='_3LWZlK']"
    PAGINATION_FIELDS = "//span[normalize-space()='Next']//..//preceding-sibling::*"  # "//nav[@class='yFHi8N']//a"
    ITEM_TO_REPLACE_XPATH_FIELD = "//div[contains(text(),'text to replace')]//..//..//..//span//input[@type='checkbox']"
    ITEM_ADD_TO_COMPARE_FIELD = ""
    COMPARE_PAGE_LINK = "//a[@class='_11o22n _87aCMT']"

    # Methods to get the fields
    def getItemSearchResultsList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ITEM_SEARCH_RESULTS_LIST)

    def getLeftPriceSlider(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LEFT_PRICE_SLIDER)

    def getInternalStorageList(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXPAND_INTERNAL_STORAGE_LIST)

    def get128GBIntStorageField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ONE_TWO_EIGHT_GB_INT_STORAGE_FIELD)

    def get4GBRamCheckBoxField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FOUR_GB_RAM_CHECKBOX_FIELD)

    def getAllRatings(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.ALL_RATINGS_FIELDS)

    def getPaginationFields(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.PAGINATION_FIELDS)

    def getAddToCompareItem(self, item_name):
        self.ITEM_ADD_TO_COMPARE_FIELD = self.ITEM_TO_REPLACE_XPATH_FIELD.replace('text to replace', item_name)
        #print("XPATH {0}".format(self.ITEM_ADD_TO_COMPARE_FIELD))
        return self.wait_for_presence_of_element(By.XPATH, self.ITEM_ADD_TO_COMPARE_FIELD).find_element(By.XPATH,self.ITEM_ADD_TO_COMPARE_FIELD)

    def getComparePageLink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.COMPARE_PAGE_LINK)

    # Methods to interact with elements
    def findItem(self, item_input):
        ItemResultsList = self.getItemSearchResultsList()
        for item in ItemResultsList:
            self.log.debug("Item is {0}".format(item.text))
            if item_input == item.text:
                self.log.debug("Clicked on {0}".format(item.text))
                # item.click()
                self.driver.execute_script("arguments[0].click()", item)
                break

    def dragLeftPriceSlider(self):
        slider = ActionChains(self.driver)
        rightHandle = self.getLeftPriceSlider()
        slider.drag_and_drop_by_offset(rightHandle, -70, 0).perform()

    def click4GBramCheckbox(self):
        # self.driver.execute_script("arguments[0].click()", int_storage_expand)
        ram4gb = self.get4GBRamCheckBoxField()
        ram4gb.find_element(By.XPATH, self.FOUR_GB_RAM_CHECKBOX_FIELD).click()

    def CLick128GBIntStorageCheckBox(self):
        int_storage_expand = self.getInternalStorageList()
        int_storage_expand.find_element(By.XPATH, self.EXPAND_INTERNAL_STORAGE_LIST).click()
        int_storage_box = self.get128GBIntStorageField()
        int_storage_box.find_element(By.XPATH, self.ONE_TWO_EIGHT_GB_INT_STORAGE_FIELD).click()

    def selectItemsToCompare(self, item_name_1, item_name_2):
        item_1 = self.getAddToCompareItem(item_name_1)#.find_element(By.XPATH,self.ITEM_ADD_TO_COMPARE_FIELD) # .click()
        self.driver.execute_script("arguments[0].click()", item_1)
        #time.sleep(1)
        item_2 = self.getAddToCompareItem(item_name_2)#.find_element(By.XPATH,self.ITEM_ADD_TO_COMPARE_FIELD)  # .click()
        self.driver.execute_script("arguments[0].click()", item_2)
        self.getComparePageLink().click()
        time.sleep(2)

    def getRatings(self, all_ratings=None):
        if all_ratings is None:
            all_ratings = []
        for rating_text in range(len(self.getAllRatings())):
            txt = self.getAllRatings()[rating_text]
            all_ratings.append(txt.text)
        return all_ratings

    def paginateAllPages(self, all_ratings):

        no_pages = self.getPaginationFields()
        total_pg_count = len(
            no_pages)

        for i in range(total_pg_count - 1):
            self.pagination()
            all_ratings = self.getRatings(all_ratings)

        return all_ratings

    # Methods to perform the tests
    def selectItem(self, item_input):
        self.findItem(item_input)
        time.sleep(3)

    def applySearchFilters(self):
        self.dragLeftPriceSlider()
        time.sleep(1)

        self.click4GBramCheckbox()
        time.sleep(1)
        self.CLick128GBIntStorageCheckBox()
        time.sleep(1)
        all_ratings = self.getRatings()
        ratings = self.paginateAllPages(all_ratings)

        return ratings

    def addToComparePage(self, item_name_1, item_name_2):
        self.selectItemsToCompare(item_name_1, item_name_2)
