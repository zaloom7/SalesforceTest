import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import openpyxl
import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Record:

    def __init__(self, driver):
        self.driver = driver

    def clickAppLauncher(self):
        self.driver.execute_script('arguments[0].click();',
                                   self.driver.find_element(by=By.XPATH, value="//div[@class='slds-icon-waffle']"))

        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='slds-icon-waffle']"))).click()

    def serviceConsole(self):
        self.driver.execute_script('arguments[0].click();',
                                   self.driver.find_element(by=By.XPATH, value="//a[@data-label='Service Console']"))

    def dropdown(self):
        self.driver.execute_script('arguments[0].click();',
                                   self.driver.find_element(by=By.XPATH, value="//div[@class='slds-context-bar__icon-action']"))
        # self.driver.find_element(by=By.XPATH, value="//div[@class='slds-context-bar__icon-action']").click()

    def clickContacts(self):
        self.driver.execute_script('arguments[0].click();',
                                   self.driver.find_element(by=By.XPATH, value="//a[@title='Contacts']"))

    def clickNew(self):
        self.driver.execute_script('arguments[0].click();',
                                   self.driver.find_element(by=By.XPATH, value="//a[@title='New']"))

    def closeContact(self):
        self.driver.find_element(by=By.XPATH, value="//button[@title='Close New Contact']").click()

    # def newContact(self):
    #     driver.execute_script('arguments[0].click();',
    #                                driver.find_element(by=By.XPATH, value="//a[@title='New Contact']"))

    def lastName(self, lastname):
        self.driver.find_element(by=By.XPATH, value="//input[@name='{}']").send_keys(lastname)

    def searchAccount(self):
        self.driver.find_element(by=By.XPATH, value="//input[@placeholder='Search Accounts...']")

    def accountName(self, accname):
        self.driver.find_element(by=By.XPATH, value="//input[@placeholder='Search Accounts...']").send_keys(accname)

    def enterButton(self):
        self.driver.find_element(by=By.XPATH, value="//input[@placeholder='Search Accounts...']").send_keys(Keys.RETURN)

    def leadSource(self):
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(by=By.XPATH, value="//button[@aria-label='Lead Source, --None--']"))

    def selectPicklist(self):
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(by=By.XPATH, value="//lightning-base-combobox-item[contains(.,'Web')]"))

    def email(self, email):
        self.driver.find_element(by=By.XPATH, value="//input[@name='Email']").send_keys(email)

    def save(self):
        self.driver.find_element(by=By.XPATH, value="//button[@name='SaveEdit']").click()

    def discardChanges(self):
        self.driver.find_element(by=By.XPATH, value="//button[@class='slds-button slds-button_neutral discardBtn']").click()

    def searchClick(self):
        self.driver.execute_script('arguments[0].click();',
                                   self.driver.find_element(by=By.XPATH, value="//li/lightning-base-combobox-item"))

    def screenshot(self, savename):
        self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")

    def blankfield(self):
        self.driver.find_element(by=By.XPATH,
                                 value="//a[@data-index='0']").click()

    def error(self):
        # error =
        error= "We hit a snag."
        self.driver.find_element(by=By.XPATH,
                                 value="//h2[@title='{}']".format(error))

    def duplicate(self):
    #     # self.driver.find_element(By.CSS_SELECTOR, "h2")
        self.driver.find_element(by=By.XPATH,
                                 value="//h2[@title='Similar Records Exist']")
    #
    # def viewDuplicates(self):
    #     self.driver.find_element(by=By.XPATH, value="//a[contains(text(),'View Duplicates')]")

        # /ActionChains(self.driver).move_to_element(error)
# ele = driver.find_element(by=By.XPATH, value="//input[@placeholder='Search Accounts...']")
# ele.click()
# ele.send_keys("yes")
# time.sleep(3)
# ele.send_keys(Keys.RETURN)
# driver.find_element(by=By.XPATH, value="//a[@title='yes']").click()
# time.sleep(2)