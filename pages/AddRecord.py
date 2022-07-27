import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import openpyxl
import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Record:
    App_Launcher = "//div[@class='slds-icon-waffle']"
    App_search = "//input[@placeholder='Search apps and items...']"
    App_click = "//a[@data-label='{}']"
    new_Button = "//a[@title='New']"
    select_AllRecords = "//span[contains(.,'All {}')]"
    pin_List = "//button[@title='Pin this list view']"
    lastname_textbox = "//input[@name='lastName']"
    enter_values = "//input[@id=//label[text()='{}']/@for]"
    clear_Lookup = "//button[@title='Clear Selection']"
    search_Lookup = "//input[@placeholder='Search {}...']"
    add_Lookup = "//li/lightning-base-combobox-item"
    click_Picklist = "//button[@id=//label[text()='{}']/@for]"
    select_Picklist = "//lightning-base-combobox-item[contains(.,'{}')]"

    def __init__(self, driver):
        self.driver = driver

    def clickAppLauncher(self):
        self.driver.execute_script('arguments[0].click();',
                                   self.driver.find_element(by=By.XPATH, value=self.App_Launcher))

    def searchTab(self, search):
        self.driver.implicitly_wait(10)
        # self.driver.execute_script('arguments[0].send_keys(search);',
        self.driver.find_element(by=By.XPATH, value=self.App_search).send_keys(
            search)
        time.sleep(2)
        self.driver.execute_script('arguments[0].click();',
                                   self.driver.find_element(by=By.XPATH, value=self.App_click.format(search)))
        time.sleep(5)

    def pinAllRecords(self, search):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.CSS_SELECTOR, value=".triggerLinkText").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,
                                 value=self.select_AllRecords.format(search)).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH,
                                 value=self.pin_List).click()
        time.sleep(5)

    def clickNew(self):
        self.driver.execute_script('arguments[0].click();',
                                   self.driver.find_element(by=By.XPATH, value=self.new_Button))

    def closeContact(self):
        self.driver.find_element(by=By.XPATH, value="//button[@name='CancelEdit']").click()

    # def newContact(self):
    #     driver.execute_script('arguments[0].click();',
    #                                driver.find_element(by=By.XPATH, value="//a[@title='New Contact']"))

    def lastName(self, lastname):
        self.driver.find_element(by=By.XPATH, value=self.lastname_textbox).clear()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.lastname_textbox).send_keys(lastname)

    def enterValues(self, fieldname, value):
        time.sleep(2)
        self.driver.implicitly_wait(10)
        # self.driver.find_element(by=By.XPATH, value="//input[@id=//label[text()='{}']/@for]".format(y)).send_keys(val)
        self.driver.find_element(by=By.XPATH,
                                 value=self.enter_values.format(fieldname)).clear()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,
                                 value=self.enter_values.format(fieldname)).send_keys(value)
        time.sleep(2)

    def selectLookup(self, lookup, value):
        try:
            time.sleep(2)
            self.driver.find_element(by=By.XPATH,
                                     value=self.clear_Lookup).click()
        except NoSuchElementException:
            pass
        self.driver.find_element(by=By.XPATH,
                                 value=self.search_Lookup.format(lookup)).send_keys(value)
        time.sleep(2)
        self.driver.implicitly_wait(4)
        self.driver.execute_script('arguments[0].click();',
                                   self.driver.find_element(by=By.XPATH, value=self.add_Lookup))

        time.sleep(1)

    def selectPicklist(self, fieldname, val):
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(by=By.XPATH,
                                                                                     value=self.click_Picklist.format(
                                                                                         fieldname)))
        time.sleep(1)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(by=By.XPATH,
                                                                                     value=self.select_Picklist.format(
                                                                                         val)))
        time.sleep(2)

    def email(self, email):
        self.driver.find_element(by=By.XPATH, value="//input[@name='Email']").send_keys(email)

    def save(self):
        self.driver.find_element(by=By.XPATH, value="//button[@name='SaveEdit']").click()

    def discardChanges(self):
        self.driver.find_element(by=By.XPATH,
                                 value="//button[@class='slds-button slds-button_neutral discardBtn']").click()

    def screenshot(self, savename):
        self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")

    def error(self):
        # error =
        error = "We hit a snag."
        self.driver.find_element(by=By.XPATH,
                                 value="//h2[@title='{}']".format(error))

    def duplicate(self):
        #     # self.driver.find_element(By.CSS_SELECTOR, "h2")
        self.driver.find_element(by=By.XPATH,
                                 value="//h2[@title='Similar Records Exist']")

    def searchName(self, lastname):
        element = self.driver.find_element(by=By.XPATH,
                                           value="// input[@placeholder='Search this list...']")
        element.clear()
        time.sleep(4)
        element.send_keys(lastname)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        time.sleep(4)

    def editDetails(self, lastname):
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value="//a[@title='{}']".format(lastname)).click()
        time.sleep(5)

        self.driver.find_element(by=By.XPATH, value="//a[contains(text(),'Details')]").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,
                                 value="//button[@title='Edit Name']").click()
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
