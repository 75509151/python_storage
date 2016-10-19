from sele.baidu_test import Buidu
from selenium.webdriver import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    baidu = Baidu(driver)
    baidu.search("python")
    time.sleep(10)
    driver.close()
