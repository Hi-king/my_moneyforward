from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MoneyForward:
    def __init__(self, config):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://id.moneyforward.com/sign_in/email')
        mail_form = self.driver.find_element_by_name("mfid_user[email]")
        mail_form.send_keys(config['user'])
        mail_form.submit()

        password_form = self.driver.find_element_by_name("mfid_user[password]")
        password_form.send_keys(config['pass'])
        password_form.submit()

        self.driver.get("https://moneyforward.com/sign_in")
        self.driver.find_element_by_class_name('submitBtn').submit()

    def download_csv(self, year, month):
        self.driver.get(f'https://moneyforward.com/cf/csv?month={month}&year={year}')
