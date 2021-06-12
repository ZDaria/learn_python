import requests
from bs4 import BeautifulSoup
import json
from selenium.webdriver.support.ui import Select

url_str = "https://www.justetf.com/uk/etf-profile.html?3-1.0-overviewPanel&query=LU0290355717&groupField=index&from=search&isin=LU0290355717&_=1622968422668"
#url_str = "https://www.justetf.com/uk/etf-profile.html?3-1.1-&query=LU0290355717&groupField=index&from=search&isin=LU0290355717"
r = requests.get(url_str)
soup = BeautifulSoup(r.content, features="lxml")
#print(soup.prettify())
# <span>
#   of Xtrackers Eurozone Government Bond UCITS ETF 1C
# </span>
# id="id43"
print(soup.find(class_='table'))


