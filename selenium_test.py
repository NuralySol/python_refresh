from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

# Ensure ChromeDriver is installed
chromedriver_autoinstaller.install()

try:
    # Initialize WebDriver
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

    # Open Amazon
    driver.get("https://www.amazon.com/")

    # Find the search box
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")

    # Enter a search query
    search_box.send_keys("Selenium with Chrome WebDriver")
    search_box.submit()

    # Wait for results to load
    driver.implicitly_wait(10)

    # Extract and print titles of search results
    results = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")
    for result in results:
        print(result.text)
finally:
    # Close the browser
    driver.quit()