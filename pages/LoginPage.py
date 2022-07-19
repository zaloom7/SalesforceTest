from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        user = self.driver.find_element(by=By.XPATH, value="//input[@id='username']")
        user.clear()
        user.send_keys(username)

    def setPassword(self, password):
        user = self.driver.find_element(by=By.XPATH, value="//input[@id='password']")
        user.clear()
        user.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(by=By.XPATH, value="//input[@class='button r4 wide primary']").click()
