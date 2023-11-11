from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

driver = webdriver.Chrome()

dmURL = "https://www.instagram.com/direct/t/xxxxxxxxxxxxxxxxx/"

instaUser = "yourusername"
instaPass = "yourpassword"

randomString = False # set to true for random characters to be added to the end of your message
randomLength = 5 # the random string length 
message = "test" # message being sent
amount = 10 # amount of messages to send
delay = 0.5 # delay between each message being sent in seconds

wait = WebDriverWait(driver, timeout=30)

driver.get(dmURL)

usrField = wait.until( # waiting until the fields are visible
    EC.visibility_of_element_located((By.NAME, "username"))
)

usrField.send_keys(instaUser)
driver.find_element(by=By.NAME, value="password").send_keys(instaPass)
driver.find_element(by = By.XPATH, value='//button[@type="submit"]').click() # log in button

notNow = wait.until( # theres two prompts asking about notifications and this clicks not now on both
    EC.visibility_of_element_located((By.XPATH, "//*[text()='Not Now']"))
)
notNow.click()

notNow = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[text()='Not Now']"))
)
notNow.click()

# waiting until the message field is visible
wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p")))

def sendMessage(): 
    msg = message # making a local variable so we can add random data

    if randomString:
        generated = ''.join(random.choices(string.ascii_letters, k=randomLength))
        msg = f"{message} [{generated}]"
    
    msgField = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p")
    sendButton = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]")
    # you have to relocate the two elements so you dont get a stale element error

    msgField.send_keys(msg)
    sendButton.click()

for i in range(amount):
    sendMessage()
    time.sleep(delay)