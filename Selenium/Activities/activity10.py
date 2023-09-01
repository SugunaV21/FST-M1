from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
service = FirefoxService(GeckoDriverManager().install())
with webdriver.Firefox(service=service) as driver:
    driver.get("https://v1.training-support.net/selenium/dynamic-controls")
    # Print the title of the page
    print("Page title is: ", driver.title)
    wait = WebDriverWait(driver, 10)
    # Find the checkbox div
    checkbox = driver.find_element(By.ID, "dynamicCheckbox")
    # Find the checkbox toggle button
    checkbox_toggle = driver.find_element(By.ID, "toggleCheckbox")
    # Verify if the checkbox is displayed or not
    print("Checkbox is visible: ", checkbox.is_displayed())

    # Click the checkbox_toggle button to hide checkbox
    checkbox_toggle.click()
    # Wait till the checkbox disappears
    wait.until(expected_conditions.invisibility_of_element(checkbox))
    # Verify again if the checkbox is displayed or not
    print("Checkbox is visible: ", checkbox.is_displayed())
