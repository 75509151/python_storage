# coding: utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging
import logging.config
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.config.fileConfig("../sele_log.conf")  # 采用配置文件

log = logging.getLogger('sele')


class PythonOrgSearch(unittest.TestCase):
    # HOME_SEARCH_ID = "kw"
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_gw(self):
        self.driver.get("http://www.baidu.com")
        # self.assertIn("baidu", self.driver.title)

        elem = self.driver.find_element_by_id("kw")
        elem.send_keys("java")
        elem.send_keys(Keys.ENTER)

        py_elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//a[@target='_blank' and @href='http://trust.baidu.com/vstar/official/intro?type=gw']/preceding-sibling::*")))
        # py_elem = self.driver.find_elements_by_xpath("//a[@href='http://trust.baidu.com/vstar/official/intro?type=gw']/preceding-sibling::*")
        log.info(py_elem)
        if py_elem:
            py_elem.send_keys(Keys.ENTER)
        for window in self.driver.window_handles:

            log.info("window: %s" % window)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        log.info(self.driver.title)

    def test_switch(self):
        self.driver.get("http://www.baidu.com")
        # self.assertIn("baidu", self.driver.title)

        elem = self.driver.find_element_by_id("kw")
        elem.send_keys("java")
        elem.send_keys(Keys.ENTER)

        py_elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//a[@target='_blank' and @href='http://trust.baidu.com/vstar/official/intro?type=gw']/preceding-sibling::*")))
        # py_elem = self.driver.find_elements_by_xpath("//a[@href='http://trust.baidu.com/vstar/official/intro?type=gw']/preceding-sibling::*")
        log.info(py_elem)
        if py_elem:
            py_elem.send_keys(Keys.ENTER)
        for window in self.driver.window_handles:

            log.info("window: %s" % window)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        log.info(self.driver.title)

    def test_navigation(self):
        self.driver.get("http://www.baidu.com")
        self.driver.get("http://www.taobao.com")
        self.driver.forward()
        self.driver.back()

    def test_cookies(self):
        # Go to the correct domain
        self.driver.get("http://www.example.com")

        # Now set the cookie. This one's valid for the entire domain
        cookie = {'name': 'mm', 'value': '13'}
        self.driver.add_cookie(cookie)

        # And now output all the available cookies for the current URL
        print self.driver.get_cookies()

    def tearDown(self):
        time.sleep(10)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
