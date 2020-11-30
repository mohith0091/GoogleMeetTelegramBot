from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
# import pause
# import pynput
import os
# from pynput.keyboard import Key, Controller
from datetime import datetime
# YEAR#MONTH#DAY#HOUR#MINUTE###### DO NOT PUT ZERO BEFORE A NUMBER
# pause.until(datetime(2020, 3, 27, 11, 29))
# MAIL & PASSWORD (THE MAIL U WILL USE TO ENTER TO THE MEET)


class Google:
    def __init__(self, username, password, options, url_meet, tim):
        try:
            self.driver = webdriver.Firefox(options=options)
            self.driver.get(
                'https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
            time.sleep(5)
            self.driver.find_element_by_xpath(
                '//*[@id="openid-buttons"]/button[1]').click()
            self.driver.find_element_by_xpath(
                '//input[@type="email"]').send_keys(username)
            self.driver.find_element_by_xpath(
                '//*[@id="identifierNext"]').click()
            time.sleep(5)
            self.driver.find_element_by_xpath(
                '//input[@type="password"]').send_keys(password)
            self.driver.find_element_by_xpath(
                '//*[@id="passwordNext"]').click()
            time.sleep(5)
            self.driver.get(url_meet)
            time.sleep(10)
            self.driver.find_element_by_xpath(
                "//span[@class='NPEfkd RveJvd snByac']").click()
            time.sleep(tim)
            # time.sleep(5400)
            self.driver.quit()

        except:
            time.sleep(3)
            self.driver.quit()
