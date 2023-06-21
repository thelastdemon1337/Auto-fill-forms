import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


# Instantiate ChromeOptions
options = Options()
# extension_path = './auto_clicker_autoFill.crx'
# options.add_extension(extension_path)
options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
options.add_argument("--user-data-dir=C:/Users/Tarun/AppData/Local/Google/Chrome/User Data")  # Path to the user profile directory
options.add_argument("--profile-directory=Profile 1")
options.add_argument("--remote-debugging-port=9222")
# options.add_argument("--headless")  # Run Chrome in headless mode (without opening a browser window)

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome(options=options)

links = [
    "https://forms.gle/LaFvmK2nSgy7jE4a6",
     "https://forms.gle/9HZ7EGjpCHw88rQy7",
    "https://forms.gle/oSEXb4x6eQSFwNiz9",
]

tabCounter = 1

def fillForm(shortened_form_link):
    global tabCounter
    driver.execute_script("window.open('{}', '_blank');".format(shortened_form_link))
    driver.switch_to.window(driver.window_handles[tabCounter])
    if links[0] == shortened_form_link:
         time.sleep(2)
    else:
        time.sleep(1)
    form_url = driver.current_url

    # #paste form url
    driver.switch_to.window(driver.window_handles[0])
    # select 2nd configuration list 
    dropdown_element = driver.find_element(By.XPATH, "//*[@id=\"configuration-list\"]")
    dropdown = Select(dropdown_element)
    dropdown.select_by_index(1)
    config_url = driver.find_element(By.XPATH, "//*[@id=\"config-url\"]")
    config_url.clear()
    config_url.send_keys(form_url)
    # time.sleep(1)
    bar = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div[1]/main/div[1]/div[1]/h6/div/div[1]")
    bar.click()
    # time.sleep(1)
    # //*[@id="root"]/div/div[1]/main/div[1]/div[1]/h6/div/div[1]

    #go back to form page and reload
    driver.switch_to.window(driver.window_handles[tabCounter])
    # time.sleep(2)
    driver.refresh()

    #wait for it to fill and submit
    # time.sleep(2)
    submit = driver.find_element(By.XPATH, "//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]/div[1]/div")
    try:
        submit.click()
    except:
        print("Submit button not parsed!")
    
    tabCounter += 1

def setAutoFiller():
    driver.get('https://stable.getautoclicker.com/')
    

#driver code
setAutoFiller()
time.sleep(1)

for link in links:
       fillForm(link)


input("Press Enter to quit the browser...")

# Close the WebDriver and quit the browser
driver.quit()