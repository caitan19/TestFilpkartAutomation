import time

from selenium.common import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.utils import Utils
import softest


class BaseDriver(softest.TestCase):
    log = Utils.custom_logger()

    def __init__(self, driver):
        self.driver = driver
        # self.ewait = WebDriverWait(driver, 30, ignored_exceptions=(StaleElementReferenceException,))

    IFRAME_POPUP = "//iframe[@id='webklipper-publisher-widget-container-notification-frame']"
    POPUP_CLOSE_BTN = "//i[@class='wewidgeticon we_close']"
<<<<<<< HEAD
    NEXT_PAGE_BTN = "//span[normalize-space()='Next']"

    def getNextPageBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NEXT_PAGE_BTN)
=======
>>>>>>> 2314f7628be470adb715f66886f5842285c84841

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
        match = False
        while match == False:
            lastCount = pageLength
<<<<<<< HEAD
            time.sleep(2)
=======
            time.sleep(4)
>>>>>>> 2314f7628be470adb715f66886f5842285c84841
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
            if lastCount == pageLength:
                match = True

<<<<<<< HEAD
        time.sleep(2)
=======
        time.sleep(4)
>>>>>>> 2314f7628be470adb715f66886f5842285c84841

    def close_popup(self):
        popup_iframe = self.wait_for_presence_of_element(By.XPATH, self.IFRAME_POPUP)
        self.log.debug(popup_iframe)
        self.driver.switch_to.frame(popup_iframe)
        close = self.wait_for_presence_of_element(By.XPATH, self.POPUP_CLOSE_BTN).find_element(By.XPATH,
                                                                                               self.POPUP_CLOSE_BTN)
        self.driver.execute_script("arguments[0].click()", close)
        self.driver.switch_to.default_content()

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        # list_of_elements = None
        attempt = 1
        while True:
            try:
                ewait = WebDriverWait(self.driver, 30)
                list_of_elements = ewait.until(EC.presence_of_all_elements_located((locator_type, locator)))
                return list_of_elements
            except StaleElementReferenceException:
                # print("Exception occurred during waiting for all elements.")
                if attempt == 15:
                    # self.assertRaises(NoSuchElementException)
                    raise
                attempt += 1

    def wait_until_element_is_clickable(self, locator_type, locator):
        # element = None
        attempt = 1
        while True:
            try:
                ewait = WebDriverWait(self.driver, 30)
                element = ewait.until(EC.element_to_be_clickable((locator_type, locator)))
                return element
            except StaleElementReferenceException:
                # print("Exception occurred during waiting for object to be clickable.")
                if attempt == 15:
                    # self.assertRaises(NoSuchElementException)
                    raise
                attempt += 1

    def wait_for_presence_of_element(self, locator_type, locator):
        # element = None
        attempt = 1
        while True:
            try:
                ewait = WebDriverWait(self.driver, 30)
                element = ewait.until(EC.presence_of_element_located((locator_type, locator)))
                return element
            except StaleElementReferenceException:
                # print("Exception occurred during waiting for object to be clickable.")
                if attempt == 15:
                    # self.assertRaises(NoSuchElementException)
                    raise
                attempt += 1

    def switch_browser_tabs(self, tab_number, tab_type):
        # http://allselenium.info/handling-multiple-windows-python-selenium/
<<<<<<< HEAD
        if tab_type == "descendant":
            # If a newly opened tab, then
            self.log.debug("Moving to {0} child tab".format(self.driver.current_window_handle))
            self.driver.switch_to.window(self.driver.window_handles[tab_number])
        else:
            # If moving to a previous tab, then close the current tab and then move
            self.log.debug("Moving to {0} parent tab".format(self.driver.current_window_handle))
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[tab_number])

    def pagination(self):
        next_btn = self.getNextPageBtn()
        self.page_scroll()
        self.driver.execute_script("arguments[0].click()", next_btn)
        self.page_scroll()
        time.sleep(1)
=======
        # get current window handle
        '''curr_win_tab = self.driver.current_window_handle

        # get first child window
        child_win_tab = self.driver.window_handles
        if tab == "child":
            print("Child window")
            self.driver.switch_to.window(self.driver.window_handles[1])
                    # break
        elif tab == "parent":
            #self.driver.close()
            self.driver.close()
            print("Parent window")
            self.driver.switch_to.window(self.driver.window_handles[0])'''
        if tab_type == "descendant":
            # If a newly opened tab, then
            self.driver.switch_to.window(self.driver.window_handles[tab_number])
        else:
            # If moving to a previous tab, then close the current tab and then move
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[tab_number])
>>>>>>> 2314f7628be470adb715f66886f5842285c84841
