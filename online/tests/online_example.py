#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from online.helpers.page import Page

class SeleniumTest(TestCase):

    def test_search(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        page.search_bar.search(u'кафе')
        self.assertTrue(page.search_result.count > 0, 'Wrong count of firms')
        driver.close()

if __name__ == '__main__':
    unittest.main()
