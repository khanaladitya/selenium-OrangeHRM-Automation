from config import *
from Employee import *
from loginlogout import *
from buzz import *


def personalDetails():
    # Click On MyInfo, Personal Details
    myInfo = driver.find_element(
        By.CSS_SELECTOR, ":nth-child(3) > .oxd-main-menu-item")
    myInfo.click()
    time.sleep(3)

    # Filling Personal Details - Driver's Liscense Number
    license_num = driver.find_element(By.XPATH, "//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]")
    driver.execute_script(
        "arguments[0].removeAttribute('disabled')", license_num)
    license_num.send_keys('122222')
    time.sleep(1)

    # Filling Personal Details  (Nationality)

    nationality = driver.find_element(
        By.CSS_SELECTOR, ":nth-child(5) > :nth-child(1) > :nth-child(1) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text-input")
    nationality.click()
    nepalese = driver.find_element(
        By.XPATH, "//span[normalize-space()='Nepalese']").click()
    time.sleep(1)

    #  (Marital Status)
    maritalStatus = driver.find_element(
        By.CSS_SELECTOR, ":nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text-input")
    maritalStatus.click()
    single = driver.find_element(
        By.XPATH, "//span[normalize-space()='Single']").click()
    time.sleep(1)

    # select license date
    try:
        dateOfBirth = driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='yyyy-mm-dd']")
        driver.execute_script(
            "arguments[0].value = '2020-01-11';", dateOfBirth)
        time.sleep(1)

    except Exception as e:
        print(e)

    time.sleep(1)

    #  Gender selection
    male = driver.find_element(By.XPATH, '//label[normalize-space()="Male"]')
    male.click()
    time.sleep(1)

    # Click on Save Button
    driver.find_element(
        By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()
    time.sleep(4)
    print('Click Submit Button To Save Personal Info')

    # Scrollling to the webpage using ActionChains
    scrollDown = ActionChains(driver)
    scrollDown.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)

    #  Blood type
    bloodType = driver.find_element(By.XPATH, "//div[@class='orangehrm-custom-fields']//div[@class='orangehrm-card-container']//form[@class='oxd-form']//div[@class='oxd-form-row']//div[@class='oxd-grid-3 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//div[@class='oxd-select-text-input'][normalize-space()='-- Select --']")
    bloodType.click()
    Aposi = driver.find_element(
        By.XPATH, "//span[normalize-space()='A+']").click()
    time.sleep(1)

    # Clicking Save Button For BloodType
    driver.find_element(
        By.CSS_SELECTOR, "div[class='orangehrm-custom-fields'] button[type='submit']").click()
    time.sleep(5)

    # Scroll top of the webpage using ActionChains
    scrollUp = ActionChains(driver)
    scrollUp.send_keys(Keys.HOME).perform()
    time.sleep(2)
