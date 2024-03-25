from config import *


def AdminLogin():
    # Locate the input element
    # Send keys to the input element
    username = driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Username']")
    username.click()
    username.send_keys(Gname)
    time.sleep(2)
    password = driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Password']")
    password.click()
    password.send_keys(Gpass)
    time.sleep(2)
    loginbutton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    loginbutton.click()
    time.sleep(1)


def Logout():
    dropdown = driver.find_element(
        By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    dropdown.click()
    logoutbutton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, " body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)")))
    logoutbutton.click()
    time.sleep(2)


def empLogin():
    # Finding Username
    Username = driver.find_element(By.NAME, "username")
    Username.click()
    Username.send_keys(EmpUname)
    time.sleep(1)

    # Finding Password
    findPassword = driver.find_element(By.NAME, "password")
    findPassword.click()
    findPassword.send_keys(EmpPass)
    time.sleep(1)

    # Finding Button
    Login = driver.find_element(By.TAG_NAME, "button")
    Login.click()
    time.sleep(2)
