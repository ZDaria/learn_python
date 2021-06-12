from selenium import webdriver
import time

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        #self.wd.implicitly_wait(40)

# TODO: add instrument into this function

    def open_instrument_page(self):
        wd = self.wd()
        url_str = "https://www.justetf.com/uk/etf-profile.html?3-1.0-overviewPanel&query=LU0290355717&groupField=index&from=search&isin=LU0290355717"
        wd.get(url_str)

    def destroy(self):
        self.wd.quit()

if __name__=="__main__":
    app = Application()
    app.open_instrument_page()
    time.sleep(30)
    app.destroy()