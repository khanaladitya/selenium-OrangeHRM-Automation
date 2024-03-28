from config import *
from Employee import *
from loginlogout import *
from buzz import *
from myinfo import *

BrowserCall()
time.sleep(3)

AdminLogin()
time.sleep(2)

addEmployee()
time.sleep(2)

Logout()
time.sleep(2)

empLogin()
time.sleep(2)

personalDetails()
time.sleep(2)
# posting on buzz
postOnBuzz()
time.sleep(2)

# logout of employee account
Logout()
time.sleep(1)

# login by admin
AdminLogin()
time.sleep(1)

# like and comment on employee post
adminActionOnbuzz()
time.sleep(2)

driver.quit()
