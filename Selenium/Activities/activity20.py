from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
service = FirefoxService(GeckoDriverManager().install())
with webdriver.Firefox(service=service) as driver:
    # Navigate to the URL
    driver.get("https://v1.training-support.net/selenium/javascript-alerts")
    # Print the title of the page
    print("Page title is: ", driver.title)
    wait = WebDriverWait(driver, 10)
    prompt_wait = wait.until(expected_conditions.visibility_of_element_located((By.ID, "prompt")))
    prompt_wait.click()
    prompt_alert = driver.switch_to.alert
    print(prompt_alert.text)
    prompt_alert.send_keys("Python")
    driver.implicitly_wait(15)
    prompt_alert.accept()

