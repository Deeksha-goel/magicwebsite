from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the WebDriver and open the HTML page
service = Service(executable_path='/usr/local/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)

# URL of your webpage
URL = 'https://deeksha-goel.github.io/magicwebsite/'

try:
    # Open the webpage
    driver.get(URL)

    # Wait for the h1 element with text containing "Magic Website" to be present
    h1_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(., 'Simple Website')]"))
    )

    # If the element is found, print success message
    print("Test Passed: Found h1 tag containing 'Simple Website'")
except Exception as e:
    # If the element is not found, print failure message
    print("Test Failed:", e)
finally:
    # Close the WebDriver
    driver.quit()