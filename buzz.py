from config import *
from Employee import *
from loginlogout import *


def postOnBuzz():
    # Click On Buzz
    Buzz = driver.find_element(
        By.CSS_SELECTOR, ":nth-child(8) > .oxd-main-menu-item")
    Buzz.click()
    time.sleep(3)

    # writing  on text area
    buzzPost = driver.find_element(By.TAG_NAME, "textarea")
    buzzPost.click()
    buzzPost.send_keys("how are you")
    time.sleep(2)

    # Click On Post Button
    post = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    post.click()
    time.sleep(2)

def adminActionOnbuzz():
    # Click on Buzz
    driver.find_element(
        By.CSS_SELECTOR, ":nth-child(12) > .oxd-main-menu-item").click()
    time.sleep(5)

    # Click Heart Button(like post)
    driver.find_element(
        By.XPATH, "//div[@class='orangehrm-buzz-newsfeed']//div[1]//div[1]//div[3]//div[1]//div[1]//*[name()='svg']//*[name()='g' and @id='Group']//*[name()='path' and @id='heart']").click()
    time.sleep(5)

    # Comment
    comment = driver.find_element(
        By.XPATH, "//div[@class='orangehrm-buzz-newsfeed']//div[1]//div[1]//div[3]//div[1]//button[1]//i[1]")
    comment.click()
    time.sleep(2)
    textBox = driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Write your comment...']")
    textBox.send_keys("fine")
    textBox.send_keys(Keys.ENTER)
    time.sleep(2)

    # Scroll down to the webpage using ActionChains
    scrollDown = ActionChains(driver)
    scrollDown.move_by_offset(0, 500).perform()
