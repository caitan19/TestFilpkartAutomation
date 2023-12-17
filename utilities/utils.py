import inspect
import logging

import softest
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Utils(softest.TestCase):
    def assertListItemText(self, list, value):
        for item1 in list:
            print("The text is: ", item1.text)
            # self.soft_assert(self.assertEquals, item1.text, value)#assert item1.text == value
            self.soft_assert(self.assertEqual, item1.text, value)  # assert item1.text == value
            # self.soft_assert(self.assertTrue, item1.text == value)
            if item1.text == value:
                print("Test passed")
            else:
                print("Test failed")
        self.assert_all()

    def assertRatingsText(self, list, value):
        rate = value.find("+")
        rate_num = value[0:rate]
        for item1 in list:
            if item1.text != '':
                ind = item1.text.find("/")
                rating = item1.text[0:ind]
                print("The rating is: ", float(rating))
                self.soft_assert(self.assertGreaterEqual, rating, rate_num)
                if float(rating) >= int(rate_num) * 1.0:
                    print("Test passed")
                else:
                    print("Test failed")
        self.assert_all()

    def verifyItemsInCart(self, items_in_cart, item_input):
        list_len = len(items_in_cart)
        counter = 0
        item_list = []
        while list_len > counter:
            for item in items_in_cart:
                item_list.append(item.text)

            counter = counter + 1

        self.assertIn(item_input, item_list, "Item is not in cart.")

    def assertDifference(self, price_list):
        # temp = ["61,999", "61,999", "61,999"]
        # self.assertTrue(len(set(temp)) == len(price_list))
        self.assertTrue(len(set(price_list)) == len(price_list))

    def custom_logger(logLevel=logging.DEBUG):
        # Get the function name
        loggerName = inspect.stack()[1][3]
        # create the logger
        logger = logging.getLogger(loggerName)
        logger.setLevel(logLevel)
        # create console handler or file handler and set the log level
        consoleHandler = logging.StreamHandler()
        fileHandler = logging.FileHandler("testRun.log")
        # create formater
        formatter = logging.Formatter("%(asctime)s - %(levelname)s :- %(message)s")
        # add formater to console or file handler)
        consoleHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)
        # add console handler or filehandler to the logger
        logger.addHandler(consoleHandler)
        logger.addHandler(fileHandler)
        return logger
