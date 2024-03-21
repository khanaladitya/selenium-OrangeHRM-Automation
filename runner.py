from config import *
from dashboard import *
from loginlogout import *
from buzz import *
from myinfo import *

BrowserCall()
time.sleep(6)
AdminLogin()
time.sleep(5)


addEmployee()
time.sleep(2)

Logout()
time.sleep(5)

empLogin()
time.sleep(5)

personalDetails()
time.sleep(5)
# posting on buzz
postOnBuzz()
time.sleep(2)

# changeEpass()
# time.sleep(2)

# logout of employee account
Logout()
time.sleep(5)

# login by admin
AdminLogin()
time.sleep(5)

# like and comment on employee post
adminActionOnbuzz()
time.sleep(5)

driver.quit()
