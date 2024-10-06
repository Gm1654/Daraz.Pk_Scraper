from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

url = "https://www.daraz.pk/#?"

s=Service("C:/Users/Ghulam e Mustafa/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(url)

# Search for Ear Buds
search = driver.find_element(By.CLASS_NAME, "search-box__input--O34g")
search.send_keys('Ear Buds')
driver.find_element(By.CLASS_NAME, "search-box__button--1oH7").click()

time.sleep(3)


Names = []
Prices = []
Discounts = []
Solds = []


for page in range(1, 5):
    time.sleep(3)  # Allow time for page to load
    data = driver.find_elements(By.CLASS_NAME, "buTCk")
    
    for item in data:
        try:
            Name = item.find_element(By.CLASS_NAME, "RfADt").text.strip()
            Names.append(Name)
        except:
            Names.append("")
        
        try:
            Price = item.find_element(By.CLASS_NAME, "aBrP0").text.strip()
            Prices.append(Price)
        except:
            Prices.append("")
        
        try:
            Discount = item.find_element(By.CLASS_NAME, "IcOsH").text.strip()
            Discounts.append(Discount)
        except:
            Discounts.append("")
        
        try:
            Sold = item.find_element(By.CLASS_NAME, "_1cEkb").text.strip()
            Solds.append(Sold)
        except:
            Solds.append("")
    
    
    try:
        next_button = driver.find_element(By.CLASS_NAME, "ant-pagination-next")
        next_button.click()
    except:
        print("No more pages available or failed to navigate.")
        break

# Save data to CSV
pd.DataFrame({
    'Name': Names,
    'Price': Prices,
    'Discount': Discounts,
    'Sold': Solds
}).to_csv('daraz_data.csv', index=False)

driver.quit()


