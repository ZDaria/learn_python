import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.justetf.com/uk/'
                 'etf-profile.html?query=LU0290355717&groupField=index&from=search&'
                 'isin=LU0290355717#listing')
soup = BeautifulSoup(r.content)
print(soup.prettify())
# <span>
#   of Xtrackers Eurozone Government Bond UCITS ETF 1C
# </span>

