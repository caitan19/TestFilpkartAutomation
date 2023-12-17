import time

import pytest
import softest
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.flipkart_compare_items_page import CompareItemsPage
from pages.flipkart_search_results_page import SearchResultsPage
from pages.item_detail_page import ItemDetailPage
from pages.flipkart_home_page import HomePage
from pages.cart_page import Cart
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt()
class TestFlipkartAutomation(softest.TestCase):
    log = Utils.custom_logger()

    # @data(("caitan1wwww9@yahoo.com", "3Dsystems#1"), ("caitan19@yahoo.com", "3Dsysstems#1"), ("caitan19@yahoo.com", "3Dsystems#1"))
    # @unpack
    @file_data("../Testdata/testAddToCartData.json")
    def test_add_to_cart(self, search_input, item_input_1, item_input_2):
        flipkart_asserts = Utils()
        hp = HomePage(self.driver)
        hp.SearchProduct(search_input)
        srp = SearchResultsPage(self.driver)
        srp.page_scroll()
        srp.selectItem(item_input_1)
        idp = ItemDetailPage(self.driver)
        idp.switch_browser_tabs(1, "descendant")
        idp.clickAddToCartBtn()
        crtp = Cart(self.driver)
        srp.switch_browser_tabs(0, "ancestor")
        srp.selectItem(item_input_2)
        idp.switch_browser_tabs(1, "descendant")
        idp.clickAddToCartBtn()
        items_in_cart = crtp.getItemTextField()
        flipkart_asserts.verifyItemsInCart(items_in_cart, item_input_1)

    @file_data("../Testdata/testSearchFiltersData.json")
    def test_search_filters(self, search_input, ratings, item_input_2):
        flipkart_asserts = Utils()
        hp = HomePage(self.driver)
        hp.SearchProduct(search_input)
        srp = SearchResultsPage(self.driver)
        all_item_ratings = srp.applySearchFilters()
        flipkart_asserts.assertRatingsText(all_item_ratings, ratings)

    @file_data("../Testdata/testCompareData.json")
    def test_compare_items(self, search_input, item_input_1, item_input_2, brand_name, product_name):
        flipkart_asserts = Utils()
        hp = HomePage(self.driver)
        hp.SearchProduct(search_input)
        srp = SearchResultsPage(self.driver)
        srp.addToComparePage(item_input_1, item_input_2)
        cmp = CompareItemsPage(self.driver)
        price_list = cmp.addAProduct(brand_name, product_name)
        flipkart_asserts.assertDifference(price_list)
