from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up the webdriver (make sure ChromeDriver is installed and available in PATH)
driver = webdriver.Chrome()

# Open the URL
url = 'https://www.rei.com/used/shop/all?size=11&department=Men%27s%20Footwear'
driver.get(url)

# Allow time for the page to fully load
time.sleep(5)

# Extract the shoe listings
shoes = []
shoe_elements = driver.find_elements(By.CLASS_NAME, 'your-shoe-class')

for item in shoe_elements:
    title = item.find_element(By.TAG_NAME, 'h2').text.strip()
    price = item.find_element(By.CLASS_NAME, 'your-price-class').text.strip()
    size = item.find_element(By.CLASS_NAME, 'your-size-class').text.strip()

    if 'Size 11' in size:
        shoes.append({'Title': title, 'Price': price, 'Size': size})

# Store the data in a pandas DataFrame
df = pd.DataFrame(shoes)
df.to_csv('rei_used_size11_shoes.csv', index=False)

print("Scraping complete! Data saved to H:\REI DATA\rei_used_size11_shoes.csv")

# Close the browser
driver.quit()
