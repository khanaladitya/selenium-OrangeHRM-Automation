# importing modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

baseurl = "https://opensource-demo.orangehrmlive.com"
Gname = "Admin"
Gpass = "admin123"
EmpUname = "aditya47"
EmpPass = "ak47@134"
EmChangepass = "aditya12345"

# browser configuration
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920x1080")
options.add_argument("--start-maximized")
options.add_argument("--incognito")

driver = webdriver.Chrome(options)


def BrowserCall():
    driver.get(baseurl)
    time.sleep(1)
