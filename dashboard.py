from config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def addEmployee():
    # click on  PIM
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)").click()
    time.sleep(1)
    # click on add employee
    driver.find_element(
        By.CSS_SELECTOR, "header[class='oxd-topbar'] li:nth-child(3) a:nth-child(1)").click()
    time.sleep(2)

    # enter employee name

    # Using CSS Selector to locate the input field
    css_selector = "input[placeholder='First Name']"

    # Use WebDriverWait to wait for the presence of the element

    element_css = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )

    # Now you can interact with the elements

    element_css.send_keys("aditya")

    # empfname = driver.find_element(
    #    By.CSS_SELECTOR, "input[placeholder='First Name']")
   # empfname.click()
   # time.sleep(3)
    # empfname.send_keys('aditya')
    ss_selector = "input[placeholder='Last Name']"

    # Use WebDriverWait to wait for the presence of the element

    element_ss = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ss_selector))
    )

    # Now you can interact with the elements

    element_ss.send_keys("khanal")
    # add employee last name
    # emplname = driver.find_element(
    #  By.CSS_SELECTOR, "input[placeholder='Last Name']")
    # emplname.click()
   # time.sleep(2)
    # emplname.send_keys('khanal')
    # time.sleep(1)

    # clearing and adding employeeid
    empId = driver.find_element(
        By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")

    empId.send_keys(Keys.CONTROL + "a")
    empId.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    empId.send_keys('77497')
    time.sleep(1)

    # Enable Create Login Details
    driver.find_element(
        By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
    time.sleep(1)

    # Scroll down the webpage using ActionChains
    scrollDown = ActionChains(driver)
    scrollDown.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(1)

    # Enter Username
    newUname = driver.find_element(By.XPATH, "//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[1]/div[1]/div[1]/div[2]/input[1]")
    newUname.click()
    newUname.send_keys('aditya47')
    time.sleep(1)

    # Status enabled
    enable = driver.find_element(
        By.XPATH, "//label[normalize-space()='Enabled']").click()
    # disable = driver.find_element(By.XPATH, "//label[normalize-space()='Disabled']").click()
    time.sleep(1)

    # Enter Password
    newPass = driver.find_element(
        By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']")
    newPass.click()
    newPass.send_keys('ak47@134')
    time.sleep(1)

    # Confirm Password
    confirmPass = driver.find_element(
        By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']")
    confirmPass.click()
    confirmPass.send_keys('ak47@134')
    time.sleep(1)
    # save data
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(2)
