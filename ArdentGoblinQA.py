from selenium import webdriver
#Adjust per browser; sample is written for Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException

from time import sleep


#Set options for not prompting DevTools information
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--headless")

URL1 = "https://theardentgoblin.wordpress.com/"

print("testing started")
driver = webdriver.Chrome(options=options)
driver.get(URL1)
sleep(3)

#Get page title
title = driver.title

# Test if title is correct
assert "Goblin" in title
print("Title test passed")

#Test that menu options on home page are working properly
#Wait for the page to fully load
sleep(3)
#Test elements in about page
print("Testing About Page")
sleep(3)
try:
    driver.find_element(By.CSS_SELECTOR, "#modal-1-content > ul > li:nth-child(2)").click()
    sleep(3)
    print("About Page loaded successfully, testing elements")
#testing to confirm correct content block is loaded
    text_element = driver.find_element(By.CSS_SELECTOR, "#wp--skip-link--target > div > div > div > div > div")
    assert "I’m the Ardent Goblin, your socially awkward and sometimes funny mom friend. Welcome to my journey into the world of game development." in text_element.text
    sleep(2)
    print("Confirmed Text is present, testing image")
#testing to confirm image is loaded
    image_element = driver.find_element(By.CSS_SELECTOR, "#wp--skip-link--target > div > div > figure")
    assert image_element.is_displayed()
    sleep(2)
    print("Confirmed Ardent Image is present")
    sleep(2)
except NoSuchElementException:
    print("An error occurred: No Such Element")
except TimeoutException:
    print("The page has timed out, please check connection")
except JavascriptException:
    print("An error occured: JavaScript Exception")
except ElementNotVisibleException:
    print ("An error occured: Element Not Visable")
except ElementNotInteractableException:
    print("An error occured: Element Not Interactable")

#Continue Checking menu buttons
print("Testing menu buttons")
try:
    driver.find_element(By.CSS_SELECTOR, value="#modal-1-content > ul > li:nth-child(3) > a").click()
    print("Coding Cove loaded successfully, Loading Goblin Thoughts")

except NoSuchElementException:
    print("An error occurred: No Such Element")
except TimeoutException:
    print("The page has timed out, please check connection")
except JavascriptException:
    print("An error occured: JavaScript Exception")
except ElementNotVisibleException:
    print("An error occured: Element Not Visable")
except ElementNotInteractableException:
    print("An error occured: Element Not Interactable")
try:
    driver.find_element(By.CSS_SELECTOR, value="#modal-1-content > ul > li:nth-child(4) > a").click()
    print("Goblin Thoughts loaded successfully, Loading Goblin Doodles")
    sleep(3)
except NoSuchElementException:
    print("An error occurred: No Such Element")
except TimeoutException:
    print("The page has timed out, please check connection")
except JavascriptException:
    print("An error occured: JavaScript Exception")
except ElementNotVisibleException:
    print ("An error occured: Element Not Visable")
except ElementNotInteractableException:
    print("An error occured: Element Not Interactable")
try:
    driver.find_element(By.CSS_SELECTOR, value="#modal-1-content > ul > li:nth-child(5) > a").click()
    print("Goblin Doodles loaded successfully")
    sleep(3)
except NoSuchElementException:
    print("An error occurred: No Such Element")
except TimeoutException:
    print("The page has timed out, please check connection")
except JavascriptException:
    print("An error occured: JavaScript Exception")
except ElementNotVisibleException:
    print ("An error occured: Element Not Visable")
except ElementNotInteractableException:
    print("An error occured: Element Not Interactable")
sleep(2)
print("Testing completed, closing browser")

# Close the driver
driver.quit()