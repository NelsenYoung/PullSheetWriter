from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
import time

desired_macchine_id = input("Please enter the machine you are servicing: ")
conf = 0
machine_ids = ['0100101', '01002013', '01003014', '01005020', '010060210', 
               '0101012', '0200103', '0200204', '0200305', '0200315', '0200416', 
               '020102', '020123', '020210', '020222', '030106', '030207', '0303011',
               '040108', '040109', '040317', '040318', '236237']

# Check for valid input
while(conf != 1):
    for machine in machine_ids:
        if(machine == desired_macchine_id):
            conf = 1
            break
    if(conf == 0):
        desired_macchine_id = input("Please enter the machine you are servicing: ")


# Greenlite Credentials
username = ""
password = ""

#install the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Go to Greenlite login page
URL = "https://greenlite.mycantaloupe.com/login/" 
driver.get(URL)

# login to Greenlite
driver.find_element("id", "UserName").send_keys(username)
driver.find_element("id", "Password").send_keys(password)
button = driver.find_element("id", "signInButton")

time.sleep(2)

button.click()

# Find the desired machine
view_container = driver.find_element(By.ID, "viewContainer")
machine_id = view_container.find_element(By.LINK_TEXT, desired_macchine_id)
machine_id.click()


time.sleep(0.25)


machine_container = driver.find_element(By.ID, "machineDetailTabControl")

print("coil - item count")
# Parse the levels of the current machine
level_string = "ctl00_mainContentPlaceHolder_machineDetailInventory_currentPlanogramViewer_dgGeneralInventoryView_ctl02_LblLevel"
sales_string = "ctl00_mainContentPlaceHolder_machineDetailInventory_currentPlanogramViewer_dgGeneralInventoryView_ctl02_sinceLastRestockQuantityLabel"
coil_string = "ctl00_mainContentPlaceHolder_machineDetailInventory_currentPlanogramViewer_dgGeneralInventoryView_ctl02_LblCoil"
items = machine_container.find_elements(By.CLASS_NAME, "itemDetailLink")

i = 2
for item in items:

    if(i >= 10):
        count = machine_container.find_element(By.ID, level_string.replace("02", str(i)))
        sales = machine_container.find_element(By.ID, sales_string.replace("02", str(i)))
        coil = machine_container.find_element(By.ID, coil_string.replace("02", str(i)))
    else:
        count = machine_container.find_element(By.ID, level_string.replace("2", str(i)))
        sales = machine_container.find_element(By.ID, sales_string.replace("2", str(i)))
        coil = machine_container.find_element(By.ID, coil_string.replace("2", str(i)))
    

    if(int(count.text) < 2 or int(sales.text) > 1):
        if(int(count.text) == 0):
            print(coil.text, " - ", item.text, " Empty Coil")
        else:
            print(coil.text, " - ", item.text, int(sales.text) + 1)
    
    i = i + 1
