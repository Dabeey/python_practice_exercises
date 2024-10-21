# selenium modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

# Access your environment variables


# beautiful soup modules
from bs4 import BeautifulSoup
import requests
import time


zillow_url = 'https://appbrewery.github.io/Zillow-Clone/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

response = requests.get(zillow_url,headers=headers)
soup = BeautifulSoup(response.text,'html.parser')


listings_addresses = soup.select('.StyledPropertyCardDataWrapper address')
listings_prices = soup.select(".StyledPropertyCardDataArea-fDSTNn span")
listings_link = soup.select('.StyledPropertyCardDataWrapper a')#a['href']


addresses = [address.text.replace('\n','').replace(' ','') for address in listings_addresses]
price_list = [price.text.split('+')[0].split('/')[0].replace(',','') for price in listings_prices]
links = [link['href'] for link in listings_link]



# ###### fill the form automatically
firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)

for i in range(len(links)):
    form_url = os.getenv('FORM_URL')
    driver.get(form_url)
    time.sleep(1)
    property_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_address.send_keys(addresses[i])
    time.sleep(1)
    price_per_month = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_per_month.send_keys(price_list[i])
    time.sleep(1)
    link_to_the_property = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_to_the_property.send_keys(links[i])
    time.sleep(1)
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

    print(f'Successfully created form number {i}')
time.sleep(1)

print(f'Successfully created {i} forms')



