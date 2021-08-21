from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MoneyForward:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://google.com')
