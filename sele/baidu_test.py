# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

import logging
import logging.config
# log

# import unit

logging.config.fileConfig("sele_log.conf")  # 采用配置文件

log = logging.getLogger('sele')


class Baidu(object):
    """docstring for BaiduSearch"""
    HOME_PAGE = "http://www.baidu.com"
    HOME_SEARCH_ID = "kw"

    def __init__(self, browser):
        self.brow = browser

    def _in_baidu(self):
        return True

    def search(self, keys):
        # if self._in_baidu():
        # need kown sele wait explict and implict
        self.brow.get(Baidu.HOME_PAGE)
        try:
            element = WebDriverWait(self.brow, 10).until(EC.presence_of_element_located((By.ID, Baidu.HOME_SEARCH_ID)))
            element.send_keys(keys)
            element.send_keys(Keys.ENTER)
        except Exception, e:
            log.warning("search failed: %s" % str(e))


if __name__ == "__main__":
    driver = webdriver.Firefox()
    baidu = Baidu(driver)
    baidu.search("python")
    assert "python" in driver.title
    time.sleep(10)
    # driver.close()
