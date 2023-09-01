from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Set up the Firefox Driver with WebDriverManager
service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    # Navigate to the URL
    driver.get("https://v1.training-support.net/selenium/popups")
    # Print the title of the page
    print("Page title is: ", driver.title)

    # Find the "Sign In" button
    driver.implicitly_wait(7)
    signin_button = driver.find_element(By.CLASS_NAME, "orange")
    # Move the cursor over the button to show tooltip
    ActionChains(driver).move_to_element(signin_button).perform()
    # Print the tooltip text
    tooltip_text = signin_button.get_attribute("data-tooltip")
    print("Button tooltip text: ", tooltip_text)
    # Click the button
    signin_button.click()

    # Find the username and password fields
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("password")

    # Click login
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/button").click()

    # Print the confirmation message
    message = driver.find_element(By.ID, "action-confirmation")
    print("Confirmation message: ", message.text)
