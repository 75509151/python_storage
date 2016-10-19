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
        # self.driver.get("http://www.python.org/")
        # py_elem = self.driver.find_elements_by_xpath("//a[@class='readmore']")
        # log.info("hehhe")
        # for elem in py_elem:
        #     elem.send_keys(Keys.ENTER)
        # log.info("ele: %s" % elem)

    def tearDown(self):
        time.sleep(10)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
