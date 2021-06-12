import time
from selenium import webdriver
import os

cwd = os.getcwd()
os.environ["PATH"] = cwd


driver = webdriver.Chrome()
driver.get('https://www.justetf.com/uk/etf-profile.html?3-1.0-overviewPanel&'
           'query=LU0290355717&groupField=index&from=search&'
           'isin=LU0290355717&_=1622968422668');
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
